from models.observation import Observation
from models.action import Action
from env.tasks import tasks
from env.grader import grade

class CodeReviewEnv:

    def __init__(self):
        self.current_task = None
        self.step_count = 0

    def reset(self):
        self.current_task = tasks[0]
        self.step_count = 0

        return Observation(
            pr_title="Fix bug",
            pr_description="Review this PR",
            code_diff=self.current_task["code_diff"],
            file_name="main.py",
            previous_comments=[]
        )

    def step(self, action: Action):
        self.step_count += 1

        score = grade(action, self.current_task)

        done = True

        observation = Observation(
            pr_title="Done",
            pr_description="Completed",
            code_diff="",
            file_name="",
            previous_comments=[action.review_comment]
        )

        return observation, score, done, {}

    def state(self):
        return {
            "task_id": self.current_task["id"],
            "steps": self.step_count
        }