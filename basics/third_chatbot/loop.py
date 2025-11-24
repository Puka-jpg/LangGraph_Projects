from basics.third_chatbot.main import bot
from basics.third_chatbot.schemas import ChatState



state = None
while True:
    in_message = input("You: ")
    if in_message.lower() in {"quit","exit","bye"}:
        break
    if state is None:
        state: ChatState = {
            "messages": [{"role": "user", "content":in_message}]}
    else:
        state["messages"].append({"role":"user","content": in_message})

    state = bot.invoke(state)
    print("Bot:",state["messages"][-1].content)
    # print([msg.content for msg in state["messages"]])