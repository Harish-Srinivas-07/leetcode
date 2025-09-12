# LeetCode Template & Solutions 📘

This repository helps you generate clean Python stubs for LeetCode problems and also includes your solved answers.

## 📌 Features

### ✅ 1. Auto Template Generator

Using the script `template.py`, you can:

- Enter any LeetCode problem number (`1–3631`)
- Automatically fetch:
  - Problem Title
  - Difficulty
  - Tags
  - Full Description
- Generate a structured Python file like:

```

E:\leetcode\283.move_zeroes.py

````

- If the file already exists, it **appends** the new problem description/code at the end.

### ✅ 2. Solved Answers Included

This repo also contains **my personal solved LeetCode answers**, saved in the same folder.

Each `.py` file follows a clean format with metadata, docstring, and testable function stub.

## 🛠 Requirements

- Python 3.7+
- `requests`
- `beautifulsoup4`

Install dependencies:

```bash
pip install requests beautifulsoup4
````

## 🚀 How to Use
1. Run the fetcher script:

```bash
python template.py
```

2. Enter a LeetCode problem number (e.g., `1`, `283`, `42`)
3. The Python file will be created or updated in the same directory.


## 🧾 Sample File Output (e.g., `283.move_zeroes.py`)

```python
"""
Leetcode 283 - Move Zeroes  
https://leetcode.com/problems/move-zeroes/  
File: 283.move_zeroes.py

Difficulty: Easy  
Tags: Array, Two Pointers

Given an integer array nums, move all 0's to the end...
"""

def move_zeroes(*args):
    pass

if __name__ == "__main__":
    args = ''  
    print("Output:", move_zeroes(args))
```

## 🙌 Author
Maintained by [Harish Srinivas](https://github.com/Harish-Srinivas-07)
