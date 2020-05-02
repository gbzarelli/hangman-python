from word_creator import LastNameWordGenerator


class TestWordCreator:

    def test_should_be_create_any_word_with_success(self):
        word_creator = LastNameWordGenerator()
        word = word_creator.generate()
        assert word is not None
        assert len(word) > 1

    def test_should_be_create_random_words(self):
        word_creator = LastNameWordGenerator()
        word1 = word_creator.generate()
        word2 = word_creator.generate()
        word3 = word_creator.generate()
        assert word1 != word2
        assert word1 != word3
        assert word2 != word3
