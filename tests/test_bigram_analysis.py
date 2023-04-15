import unittest
from bigram_analysis_service.bigram_analysis import get_bigram_analysis_result

class TestBigramAnalysis(unittest.TestCase):

    def test_get_bigram_analysis_result1(self):
        text = "The quick brown fox jumps over the lazy dog."
        expected_result = [["the","quick"],["quick","brown"],["brown","fox"],["fox","jumps"],["jumps","over"],["over","the"],["the","lazy"],["lazy","dog"]]
        self.assertEqual(get_bigram_analysis_result(text), expected_result)
    
    def test_get_bigram_analysis_result2(self):
        text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog again and again."
        expected_result = [["the","quick"],["quick","brown"],["brown","fox"],["fox","jumps"],["jumps","over"],["over","the"],["the","lazy"],["lazy","dog"],["dog","the"],["dog","again"]]
        self.assertEqual(get_bigram_analysis_result(text), expected_result)
    
    def test_get_bigram_analysis_result_with_contractions_spl_characters_punctuations(self):
        text = "I'm doing great. I'll be @my house."
        expected_result = [["i","am"],["am","doing"],["doing","great"],["great","i"],["i","will"],["will","be"],["be","my"],["my","house"]]
        self.assertEqual(get_bigram_analysis_result(text), expected_result)
    
    def test_get_bigram_analysis_result_with_empty_input(self):
        text = ""
        expected_result = []
        self.assertEqual(get_bigram_analysis_result(text), expected_result)

    def test_get_bigram_analysis_result_with_one_word_input(self):
        text = "fox"
        expected_result = []
        self.assertEqual(get_bigram_analysis_result(text), expected_result)

    def test_get_bigram_analysis_result_with_two_identical_words_input(self):
        text = "fox fox"
        expected_result = [["fox","fox"]]
        self.assertEqual(get_bigram_analysis_result(text), expected_result)
        
if __name__ == '__main__':
    unittest.main()
