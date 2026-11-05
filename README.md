# PromptsWithOllama

For assignment 1 the group decided to use **phi3** and **smollm2** as the two models to process the shared prompt.
The prompts are sent to both models using a Python script that implements a `for loop` to iterate through the list containing
the two models to sequentially send the prompt to each model via `Ollama`. The `for loop` captures the response and
appends it to an answer list. Once the outputs from the models are appended, the `for loop` ends, and a `with open` function
implements a `writer` to export and save the output in a CSV file. To execute the code, simply run the `prompter.py` file.
It will automatically handle the models and save the output in the CSV file.

We observed that both models generate output relatively fast and provide relevant och correct answers based on the prompt.
However, the **smollm2** model was slightly slower, while the **phi3** were less detailed in its response. When comparing the
outputs to large commercial models like ChatGPT and Gemini, the answers were highly similar and offered the same amount of 
coverage.  