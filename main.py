import json

with open("dataset/code_corpus.json", encoding="utf-8") as f:
    corpus = json.load(f)

with open("dataset/eval_questions.json", encoding="utf-8") as f:
    questions = json.load(f)

with open("dataset/categories.json", encoding="utf-8") as f:
    categories = json.load(f)["categories"]

print(len(corpus))      # 200
print(len(questions))   # 25
print(len(categories))  # 5

func = corpus[0]
print(func["id"])             # func_001
print(func["language"])       # python
print(func["function_name"])  # verify_jwt_token
print(func["category"])       # auth

q = questions[0]
print(q["question_id"])       # q_01
print(q["query"])             # как проверить, истёк ли токен?
print(q["correct_chunk_id"])  # func_001