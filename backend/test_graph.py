from graph import chat_graph

result = chat_graph.invoke({"message": "What services does Fly Your Tech offer?"})
print(result["response"])

result = chat_graph.invoke({"message": "Hello"})
print(result["response"])
