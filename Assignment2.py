import ollama

def ask_for_capital(country, model):
    prompt = f"What is the capital of {country}?"
    try:
        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
        return response.message.content
    except Exception as e:
        return "Failure"



def check_the_verdict(country, answer, expected, model):
    prompt = (f"Question: What is the capital of {country}?\n"
              f"Expected answer: {expected}\n"
              f"Given answer: {answer}\n\n"
              f"Does the given answer correspond with the expected answer? "
              f"It needs to contain the expected answer, but more text is fine as long as it does not contradict the expected answer, "
              f"reply with only yes or no")

    verdict = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])

    return verdict.message.content

