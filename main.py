import json
import pandas 

with open("dataset/code_corpus.json", encoding="utf-8") as f:
    corpus = json.load(f)

with open("dataset/eval_questions.json", encoding="utf-8") as f:
    questions = json.load(f)

with open("dataset/categories.json", encoding="utf-8") as f:
    categories = json.load(f)["categories"]

print(len(corpus))      # 200
print(len(questions))   # 25
print(len(categories))  # 5

