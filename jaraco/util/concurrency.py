import functools
import threading


def atomize(f, lock=None):
    """
    Decorate a function with a reentrant lock to prevent multiple
    threads from calling said thread simultaneously.

    >>> import time
    >>> checkpoints = []
    >>> @atomize
    ... def sleep_and_save_time():
    ...     time.sleep(.1)
    ...     checkpoints.append(time.time())
    >>> threads = [
    ...     threading.Thread(target=sleep_and_save_time)
    ...     for x in range(2)
    ... ]
    >>> for thread in threads:
    ...     thread.start()
    >>> for thread in threads:
    ...     thread.join()
    >>> abs(float.__sub__(*checkpoints)) >= .1
    True
    """
    lock = lock or threading.RLock()

    @functools.wraps(f)
    def exec_atomic(*args, **kwargs):
        lock.acquire()
        try:
            return f(*args, **kwargs)
        finally:
            lock.release()

    return exec_atomic


class AtomicGuard:
    """
    A decorator that can be applied to multiple functions/methods to
    prevent more than one of them from being entered at any one time.

    >>> guard = AtomicGuard()
    >>> @guard
    ... def func1(): pass
    >>> @guard
    ... def func2(): pass
    """

    def __init__(self):
        self.lock = threading.RLock()

    def __call__(self, f):
        return atomize(f, lock=self.lock)
