# 讀取題目
with open("questions.csv", "r", encoding="latin-1") as f:
    lines = f.readlines()[1:6]  # 跳過標題列

answers = []

for line in lines:
    parts = line.strip().split(",", 2)  # 根據每行的,將資料分成 QuestionID, AnswerKey, question三個部分

    qid = parts[0]
    correct_answer = parts[1]
    question = parts[2]

    print(f"Q{qid}: {question}")

    user_ans = input("Your answer (A/B/C/D): ").strip().upper()
    answers.append(f"{qid},{user_ans},{correct_answer}\n")

# 寫入答案檔案
with open("answers.csv", "w", encoding="utf-8") as f:
    f.write("QuestionID, YourAnswer, CorrectAnswer\n")
    f.writelines(answers)
