from multiset import Multiset


def main():
    multiset = Multiset[int]()

    for i in range(1, 11):
        multiset.add(i, i + 1)

    for i in range(1, 11):
        print(multiset.contains(i), end=' ')
        print(multiset.get_frequency(i))

    for i in range(1, 11):
        multiset.remove(i, i)

    for i in range(1, 11):
        print(multiset.contains(i), end=' ')
        print(multiset.get_frequency(i))

    for i in range(1, 11):
        multiset.remove(i, 1)

    print(multiset.empty)



if __name__ == "__main__":
    main()