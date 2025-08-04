import requests
from bs4 import BeautifulSoup
import os
import re

# ==== Settings ====
SAVE_DIR = r"E:\leetcode"  # Change this if needed
# leetcode_template_fetcher.py

# ========== Helpers ==========

def build_number_to_slug_map():
    print("[INFO] Fetching LeetCode problem list...")
    url = "https://leetcode.com/api/problems/all/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"[ERROR] Failed to fetch problem list: {response.status_code}")

    problems_data = response.json()
    number_to_slug = {}
    for problem in problems_data['stat_status_pairs']:
        number = problem['stat']['frontend_question_id']
        slug = problem['stat']['question__title_slug']
        number_to_slug[number] = slug

    print(f"[SUCCESS] Found {len(number_to_slug)} problems.")
    return number_to_slug

def fetch_problem_description(slug):
    url = "https://leetcode.com/graphql"
    query = {
        "query": """
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                title
                difficulty
                content
                topicTags { name }
            }
        }
        """,
        "variables": {"titleSlug": slug}
    }

    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{slug}/",
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.post(url, json=query, headers=headers)
    if response.status_code != 200:
        raise Exception(f"[ERROR] Failed to fetch problem data: {response.status_code}")

    data = response.json()
    question = data["data"]["question"]
    soup = BeautifulSoup(question["content"], "html.parser")
    plain_text = soup.get_text()

    # Remove invisible non-breaking spaces (U+00A0)
    plain_text = plain_text.replace('\u00a0', ' ')

    return {
        "id": int(question["questionId"]),
        "title": question["title"],
        "difficulty": question["difficulty"],
        "tags": [tag["name"] for tag in question["topicTags"]],
        "description": plain_text,
        "slug": slug
    }

def slugify_title_for_file(name):
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '_', name)
    return name.strip('_')


def format_python_stub(problem, user_number):
    method_name = slugify_title_for_file(problem["title"])
    file_name = f"{user_number}.{method_name}.py"
    url = f"https://leetcode.com/problems/{problem['slug']}/"

    docstring = f'''"""
Leetcode {problem["id"]} - {problem["title"]}  
{url}  
File: {file_name}

Difficulty: {problem["difficulty"]}  
Tags: {", ".join(problem["tags"])}

{problem["description"]}
"""
'''

    code = f'''{docstring}

def {method_name}(*args):
    pass


if __name__ == "__main__":
    args = ''  
    print("Output:", {method_name}(args))
'''

    return file_name, code


def save_to_file(file_name, code):
    os.makedirs(SAVE_DIR, exist_ok=True)
    file_path = os.path.join(SAVE_DIR, file_name)

    if os.path.exists(file_path):
        mode = 'a'  # append mode
        print(f"[INFO] File exists. Appending to: {file_path}")
        code = "\n\n" + code  # separate blocks with spacing
    else:
        mode = 'w'  # write mode
        print(f"[SUCCESS] Creating new file: {file_path}")

    with open(file_path, mode, encoding='utf-8') as f:
        f.write(code)
    print("-" * 60)

# ========== Main Flow ==========

def main():
    try:
        number_to_slug = build_number_to_slug_map()

        while True:
            try:
                num = int(input("\nEnter a LeetCode problem number (1–3631, or 0 to quit): "))
                if num == 0:
                    print("Exiting. Goodbye!")
                    break

                if num not in number_to_slug:
                    print("[WARNING] Invalid number. Please try again.")
                    continue

                slug = number_to_slug[num]
                print(f"[INFO] Fetching problem #{num}: {slug} ...")
                q = fetch_problem_description(slug)
                file_name, code = format_python_stub(q, num)
                save_to_file(file_name, code)

            except ValueError:
                print("[ERROR] Please enter a valid number.")
    except Exception as e:
        print("[FATAL] An unexpected error occurred:", str(e))

if __name__ == "__main__":
    main()
