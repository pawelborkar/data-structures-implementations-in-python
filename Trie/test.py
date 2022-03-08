from trie import Trie
import random
import string


CHARS = string.ascii_letters + string.punctuation


def generate_random_string(str_size: int):
    return  ''.join(random.choice(CHARS) for _ in range(str_size))



def main() -> None:
    trie = Trie()
    myset = set()
    passed = True
    
    for _ in range(5000):

        randsize = random.randint(1, 12)
        s = generate_random_string(randsize)

        trie.insert(s)
        myset.add(s)

    for s in myset:
        if not trie.contains(s):
            passed = False

    for _ in range(10000):

        randsize = random.randint(1, 12)
        s = generate_random_string(randsize)

        bool1 = trie.contains(s)
        bool2 = s in myset

        if bool1 != bool2:
            passed = False

    if not passed:
        print('FAILED')
    else:
        print('PASSED')



if __name__ == '__main__':
    main()