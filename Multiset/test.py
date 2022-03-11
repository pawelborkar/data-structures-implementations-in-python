from multiset import Multiset
import pytest


def test_multiset():
    multiset = Multiset[int]()

    s = 0
    for i in range(1, 11):
        multiset.add(i, i + 1)
        s += i + 1
        assert len(multiset) == multiset.size == s

    for i in range(1, 11):
        assert multiset.contains(i)
        assert multiset.get_frequency(i) == i + 1
    for i in range(100, 110):
        assert not multiset.contains(i)

    for i in range(1, 11):
        multiset.remove(i, i)
        
    assert multiset.size == len(multiset) == 10

    for i in range(1, 11):
        assert multiset.contains(i)
        assert multiset.get_frequency(i) == 1

    with pytest.raises(Exception):
        multiset.remove(1, 10)

    for i in range(1, 11):
        multiset.remove(i, 1)

    assert multiset.empty
    
    with pytest.raises(Exception):
        multiset.get_frequency(1)
