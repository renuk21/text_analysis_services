import unittest
from word_count_analysis_service.word_count_analysis import get_word_count_analysis_result

class TestWordCountAnalysis(unittest.TestCase):

    def test_get_word_count_analysis_result1(self):
        text = "The quick brown fox jumps over the lazy dog."
        expected_result = {"the":2,"quick":1,"brown":1,"fox":1,"jumps":1,"over":1,"lazy":1,"dog":1}
        self.assertEqual(get_word_count_analysis_result(text), expected_result)
    
    def test_get_word_count_analysis_result2(self):
        text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog again and again."
        expected_result = {"the":4,"quick":2,"brown":2,"fox":2,"jumps":2,"over":2,"lazy":2,"dog":2,"again":2,"and":1}
        self.assertEqual(get_word_count_analysis_result(text), expected_result)
    
    def test_get_word_count_analysis_result_with_contractions_spl_characters_punctuations(self):
        text = "I'm doing great. I'll be @my house."
        expected_result = {"i":2, "am":1, "doing":1, "great":1, "will":1, "be":1, "my":1, "house":1}
        self.assertEqual(get_word_count_analysis_result(text), expected_result)
    
    def test_get_word_count_analysis_result_with_empty_input(self):
        text = ""
        expected_result = {}
        self.assertEqual(get_word_count_analysis_result(text), expected_result)

    def test_get_word_count_analysis_result_with_one_word_input(self):
        text = "fox"
        expected_result = {"fox":1}
        self.assertEqual(get_word_count_analysis_result(text), expected_result)

    def test_get_word_count_analysis_result_with_two_identical_words_input(self):
        text = "fox fox"
        expected_result = {"fox":2}
        self.assertEqual(get_word_count_analysis_result(text), expected_result)

if __name__ == '__main__':
    unittest.main()
