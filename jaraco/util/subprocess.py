import queue
import subprocess
import sys
import threading


def enqueue_lines(stream, queue):
    for line in iter(stream.readline, ''):
        queue.put(line)
    stream.close()


def Popen_nonblocking(*args, **kwargs):
    r"""
    Open a subprocess without blocking. Return a process handle with any
    output streams replaced by queues of lines from that stream.

    Usage::

        proc = Popen_nonblocking(..., stdout=subprocess.PIPE)
        try:
            out_line = proc.stdout.get_nowait()
        except queue.Empty:
            "no output available"
        else:
            handle_output(out_line)

    ### import contextlib
    >>> proc = Popen_nonblocking(
    ...     [sys.executable, '-c', 'print("hello world")'],
    ...     stdout=subprocess.PIPE,
    ...     stderr=subprocess.PIPE,
    ... )
    >>> proc.wait()
    0
    >>> proc.stdout.get()
    'hello world\n'
    """
    kwargs.setdefault('close_fds', 'posix' in sys.builtin_module_names)
    kwargs.setdefault('bufsize', 1)
    text_setting = ['universal_newlines', 'text'][sys.version_info > (3, 7)]
    kwargs.setdefault(text_setting, True)
    proc = subprocess.Popen(*args, **kwargs)
    if proc.stdout:
        q = queue.Queue()
        t = threading.Thread(target=enqueue_lines, args=(proc.stdout, q))
        proc.stdout = q
        # thread dies with the parent
        t.daemon = True
        t.start()
    if proc.stderr:
        q = queue.Queue()
        t = threading.Thread(target=enqueue_lines, args=(proc.stderr, q))
        proc.stderr = q
        t.daemon = True
        t.start()
    return proc
