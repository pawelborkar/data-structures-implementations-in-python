from linked_list import LinkedList
import pytest


def test_add_remove():
    ll = LinkedList()
    
    for i in range(0, 10):
        ll.append(i)
        assert ll.size == len(ll) == i + 1
    for i in range(0, 10):
        assert ll[0] == i
        assert ll.pop_front() == i
    assert ll.empty
    with pytest.raises(Exception):
        ll.pop_front()
        
    for i in range(0, 10):
        ll.prepend(i)
        assert ll.size == len(ll) == i + 1
    for i in range(0, 10):
        assert ll[len(ll) - 1] == i
        assert ll.pop_back() == i
    assert ll.empty
    with pytest.raises(Exception):
        ll.pop_back()
        
        
def test_contains_locate():
    ll = LinkedList()
    assert not ll.contains(0)
    for i in range(0, 10):
        ll.append(i)
    assert ll.contains(0)
    assert ll.contains(5)
    assert ll.contains(9)
    assert not ll.contains(-1)
    assert not ll.contains(11)
    assert ll.locate(-1) == -1
    assert ll.locate(11) == -1
    for i in range(0, 10):
        assert ll.locate(i) == i
        
        
def test_iter():
    ll = LinkedList()
    for i in range(0, 10):
        ll.append(i)
    for v1, v2 in zip(ll, [0,1,2,3,4,5,6,7,8,9]):
        assert v1 == v2
    
    
test_add_remove()