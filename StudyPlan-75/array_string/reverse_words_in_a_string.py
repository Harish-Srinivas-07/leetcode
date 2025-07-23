"""
Leetcode 75 - 151. Reverse Words in a String  
https://leetcode.com/problems/reverse-words-in-a-string/
reverse_words_in_a_string.py

Difficulty: Medium  
Tags: String, Two Pointers

Given a string `s`, reverse the order of the words.  
A word is defined as a sequence of non-space characters.  
The result should have words separated by a single space with no leading or trailing spaces.

Examples:
- Input: s = "the sky is blue"              → Output: "blue is sky the"
- Input: s = "  hello world  "              → Output: "world hello"
- Input: s = "a good   example"             → Output: "example good a"
"""

def solve(s:str) -> str:
    return ' '.join(s.strip().split()[::-1])


if __name__ == "__main__":
    s = "the sky is blue"
    print("Output:", solve(s))