import os
from openai import OpenAI
from env.environment import CodeReviewEnv
from models.action import Action

client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

def run():
    env = CodeReviewEnv()
    obs = env.reset()

    done = False
    total_reward = 0

    while not done:
        prompt = f"""
        You are a code reviewer.

        Code:
        {obs.code_diff}

        Give review comment and approve True or False.
        """

        response = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=[{"role": "user", "content": prompt}]
        )

        text = response.choices[0].message.content.lower()

        approve = "true" in text

        action = Action(
            review_comment=text,
            approve=approve
        )

        obs, reward, done, _ = env.step(action)
        total_reward += reward

    print("Total Reward:", total_reward)

if __name__ == "__main__":
    run()