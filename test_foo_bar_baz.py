import pytest

from foo_bar_baz import foo_bar_baz

#Add testcases Here
def test_foo_bar_baz():
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

def test_error():
    with pytest.raises(TypeError):
        foo_bar_baz("div ranch")
    with pytest.raises(TypeError):
        foo_bar_baz(67.67)

def test_empty():
    with pytest.raises(TypeError):
        foo_bar_baz()
