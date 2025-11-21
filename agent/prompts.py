def agent_prompt(user_prompt):
    prompt = f"""
    You are a planner agent. Convert the user prompt into a complete engineering project plan:
    User prompt: {user_prompt}
    """
    return prompt
