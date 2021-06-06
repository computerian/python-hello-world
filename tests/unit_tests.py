from __future__ import print_function
from contextlib import contextmanager
from io import StringIO
import sys
import os
import subprocess


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def test_hello_world():
    # with captured_output() as (out, err):
    #    subprocess.call([sys.executable, 'hello_world.py'], stdout=out, stderr=err)
    # This can go inside or outside the `with` block
    # output = out.getvalue().strip()
    code, out, err = run([sys.executable, 'hello_world.py'])
    assert code == 0
    assert out == [b'hello world!\n']
    assert err == [b'']


def run(cmd):
    os.environ['PYTHONUNBUFFERED'] = "1"
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=False,
                            )
    stdout = []
    stderr = []
    while proc.poll() is None:
        line = proc.stdout.readline()
        if line != "":
            stdout.append(line)
            print(line, end='')

        line = proc.stderr.readline()
        if line != "":
            stderr.append(line)
            print(line, end='')

    return proc.returncode, stdout, stderr
