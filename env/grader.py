def grade(action, task):
    score = 0.0

    comment = action.review_comment.lower()

    # check if issue identified
    if task["bug_keyword"] in comment:
        score += 0.4

    # check decision
    if action.approve == task["approve"]:
        score += 0.4

    # bonus for explanation
    if len(comment) > 20:
        score += 0.2

    return min(score, 1.0)