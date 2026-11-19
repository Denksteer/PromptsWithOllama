# PromptsWithOllama
### Assignment 2
Running the test several times gave the same results all of the 10 times we tested them. Because Generative AI is non-deterministic, 
we increased the number of test repetitions to 100 and set the criteria to 100% correct answers to better test the consistency 
of the AI model used (gemma4). Even so, the pass rate was 100%, which indicates high reliability and consistency for this type of prompt with this AI model.

However, if a consistency test would fail, it would not be immediately clear whether the mistake came from the model 
being tested or from the LLM-judge. Therefore, two separate tests of both the model and LLM-as-judge were implemented as a 
safeguard when testing. 

To test the hallucinations of the AI, a hallucination test was implemented with a given answer containing a non-existent
country and capital. To determine whether the LLM judge could handle hallucinations, we set the expected answer to 
`There is no such country, so it has no capital.`, the judge would always answer NO, meaning it could correctly identify 
that the made up country did not meet the expected output. 

However, a more fascinating and telling observation was made in the contradiction test, where the LLM-as-Judge was assigned 
the string `The capital of Australia is not Canberra, it is Sydney.` as the answer. The expected answer was set to `Canberra`, 
to see whether the LLM-as-Judge would accept the answer just because Canberra is mentioned or if the LLM-as-Judge would 
follow the criteria about `It needs to contain the expected answer, but more text is fine as long as it does not contradict 
the expected answer`. In each run of the test, the judge responded with NO, meaning the input did not match the expected 
output just because the word Canberra was mentioned. This indicates that this AI model followed the given evaluation 
criteria to validate the output generated from the prompt.


### Assignment 1
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
