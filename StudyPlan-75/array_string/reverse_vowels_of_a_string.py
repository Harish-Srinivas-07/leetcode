"""
Leetcode 75 - 345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/
reverse_vowels_of_a_string.py

Difficulty: Easy
Tags: String, Two Pointers

Given a string `s`, reverse only the vowels in the string and return the resulting string.
Vowels include both lowercase and uppercase: 'a', 'e', 'i', 'o', 'u', and their capital forms.

Examples:
- Input: s = "IceCreAm"     → Output: "AceCreIm"
- Input: s = "leetcode"     → Output: "leotcede"
"""


def solve(s: str):
    res = []
    vowels = "aeiouAEIOU"
    vrov = "".join([i for i in s if i in vowels])[::-1]
    i = r = 0
    for c in range(len(s)):
        if s[c] in vowels:
            res.append(vrov[r])
            r += 1
            i += 1
        else:
            res.append(s[c])
            i += 1
    return "".join(res)


if __name__ == "__main__":
    s = "IceCreAm"
    print("Output:", solve(s))


"""
HINT:
make a array of all present vowels in the str
then track the vowels used track variable + normal variable for ans
"""