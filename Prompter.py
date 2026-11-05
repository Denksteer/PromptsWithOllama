import ollama
import csv

models = ["phi3", "smollm2"]
prompt = "Who created the light bulb"
filename = "promptOutput"
answer = []

for model in models:
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])

    model_name = response.model
    model_answer = response['message']['content']
    answer.append([model_name, model_answer])
    print(response['message']['content'])



with (open(filename, "w", newline='', encoding="utf-8") as file):
    writer = csv.writer(file)
    writer.writerow(["MODEL", "OUTPUT"])
    writer.writerows(answer)