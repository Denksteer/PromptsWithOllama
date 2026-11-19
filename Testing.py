import Assignment2
import unittest

country = "Australia"
model="gemma4"
class TestApp(unittest.TestCase):
    def test_model(self):
        response = Assignment2.ask_for_capital(country, "Not_a_model")
        self.assertEqual(response, "Failure")

    def test_capital(self):
        correct_capital = 0
        for i in range(100):
            answer = Assignment2.ask_for_capital(country, model)
            if "Canberra" in answer:
                correct_capital += 1
        self.assertGreaterEqual(correct_capital, 100, f"The model failed to give the correct answer more than allowed")

    def test_llm_judge(self):
        answer = "The capital of Australia is Canberra."
        response = Assignment2.check_the_verdict(country, answer, "Canberra", model)

        self.assertEqual(response, "yes")

    def test_llm_judge_made_up(self):
        answer = "The capital of Pillowcastla is pilocite."
        response = Assignment2.check_the_verdict("Pillowcastla", answer, "There is no such country, so it has no capital.", model)

        self.assertEqual(response, "no")

    def test_llm_judge_contradiction(self):
        answer = "The capital of Australia is not Canberra, it is sydney."
        response = Assignment2.check_the_verdict(country, answer, "Canberra", model)

        self.assertEqual(response, "no")


if __name__ == "__main__":
    unittest.main()