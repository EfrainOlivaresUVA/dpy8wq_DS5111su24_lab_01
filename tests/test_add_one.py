import sys
sys.path.append('./src')

import dpy8wq as pkg


def test_add_one():
    assert 5 == pkg.add_one(4)
