import pytest

from foo_bar_baz import foo_bar_baz

#Add testcases Here
def test_foo_bar_baz():
    from foo_bar_baz import foo_bar_baz
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert foo_bar_baz(-1) == ""

def test_error():
    from foo_bar_baz import foo_bar_baz
    with pytest.raises(TypeError):
        foo_bar_baz("div ranch")
    with pytest.raises(TypeError):
        foo_bar_baz(67.67)

def test_empty():
    from foo_bar_baz import foo_bar_baz
    with pytest.raises(TypeError):
        foo_bar_baz()
    with pytest.raises(TypeError):
        foo_bar_baz(None)

def test_type():
    from foo_bar_baz import foo_bar_baz
    assert isinstance(foo_bar_baz(15), str)
    assert isinstance(foo_bar_baz(0), str)
    assert isinstance(foo_bar_baz(-1), str)

def test_more():
    from foo_bar_baz import foo_bar_baz
    assert (foo_bar_baz(0) != foo_bar_baz(1))
    assert (foo_bar_baz(6767) != foo_bar_baz(67))
    assert (foo_bar_baz(42) != foo_bar_baz(2))
