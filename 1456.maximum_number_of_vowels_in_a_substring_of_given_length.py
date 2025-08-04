"""
Leetcode 1567 - Maximum Number of Vowels in a Substring of Given Length  
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/  
File: 1456.maximum_number_of_vowels_in_a_substring_of_given_length.py

Difficulty: Medium  
Tags: String, Sliding Window

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
 
Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

 
Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length


"""


def maximum_number_of_vowels_in_a_substring_of_given_length(s: str, k: int)-> int:
    vowels = 'aeiouAEIOU'
    maxx = curr = sum([1 for i in s[:k] if i in vowels])
    for i in range (k,len(s)):
        if s[i-k] in vowels: #if the sliding window first element is vowel make remove.
            curr -=1
        if s[i] in vowels: #if upcoming element is vowel count. 
            curr+=1
        maxx = max(curr, maxx)
    return maxx
    
    

if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    print("Output:", maximum_number_of_vowels_in_a_substring_of_given_length(s,k))
