tasks = [
    {
        "id": 1,
        "difficulty": "easy",
        "code_diff": "for i in range(10): print(i",
        "bug_keyword": "syntax",
        "approve": False
    },
    {
        "id": 2,
        "difficulty": "medium",
        "code_diff": "for i in list: for j in list: print(i,j)",
        "bug_keyword": "inefficient",
        "approve": True
    },
    {
        "id": 3,
        "difficulty": "hard",
        "code_diff": "query = 'SELECT * FROM users WHERE id=' + user_input",
        "bug_keyword": "sql injection",
        "approve": False
    }
]