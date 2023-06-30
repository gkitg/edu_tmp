# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# https://py.checkio.org/
# 1 Password security check module

def checkio(data):
    if len(data)>9:
        return (
            any(i.isupper() for i in data)
            and any(i.islower() for i in data)
            and any(i.isdigit() for i in data)
        )
    else:
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print('Completed!')


# 2 Find the most frequent letter in the text

def checkio(text):
    text=text.lower()
    d={i: text.count(i) for i in text if i.isalpha()}
    return max(sorted(d.keys()),key=lambda k:d[k])


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")


# 3 Return a list consisting of only the non-unique elements in this list

def checkio(data):
    return [i for i in data if data.count(i)>1]


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert not list(checkio([1, 2, 3, 4, 5])), "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good.")