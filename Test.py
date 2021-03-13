from TwitterScraper import main
import unittest

def clean():
    tweets_file = open("tweets.txt", "w")
    tags_file = open("count_tags.txt", "w")
    hash_file = open("count_hash.txt", "w")
    word_file = open("count_words.txt", "w")
    tweets_file.truncate(0)
    tags_file.truncate(0)
    hash_file.truncate(0)
    word_file.truncate(0)
    tweets_file.close()
    tags_file.close()
    hash_file.close()
    word_file.close()

def amount_of_tags():
    count = 0
    tags_file = open("count_tags.txt", "r")
    for line in tags_file.readlines():
        list_of_line = line.split()
        for word in list_of_line:
            if word.isdigit():
                count += int(word)
    tags_file.close()
    return count
    
    
def amount_of_hashtag():
    count = 0
    hash_file = open("count_hash.txt", "r")
    for line in hash_file:
        list_of_line = line.split()
        for word in list_of_line:
            if word.isdigit():
                count += int(word)
    hash_file.close()
    return count


def amount_of_words():
    count = 0
    words_file = open("count_words.txt", "r")
    for line in words_file:
        list_of_line = line.split()
        for word in list_of_line:
            if word.isdigit():
                count += int(word)
    words_file.close()
    return count

class Test(unittest.TestCase):
    def test_tags(self):
        total_tags = amount_of_tags()
        self.assertEqual(total_tags, 2, "Should be 1")

    def test_hashtag(self):
        total_hash = amount_of_hashtag()
        self.assertEqual(total_hash, 3, "Should be 1")
    
    def test_words(self):
        total_words = amount_of_words()
        self.assertEqual(total_words, 13, "Should be 7")


if __name__ == '__main__':
    clean() #open the files and clear the content
    url = "https://twitter.com/BarBenEzra2"
    main(url)
    unittest.main()