from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os
import sys


""" 
This function gets the open browser as a parameter and scrolls it down.
The browser will try to scroll at most 3 times in case it fails to (might happen if the page wasn't loaded yet,
so the new and last positions are equals). The scrolling lasts till the main function runs over 100 tweets. 
"""
def scroll(browser):
    try_to_scroll = 0
    max_tries = 3
    last_pos = browser.execute_script("return window.pageYOffset;")
    i = 0
    while True:
        i += 1
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(1)
        new_pos = browser.execute_script("return window.pageYOffset;")
        if last_pos == new_pos:
            try_to_scroll += 1
            if try_to_scroll >= max_tries:
                return False
            else:
                time.sleep(2) #before new try
        else:
            last_pos = new_pos
            break
    return True


"""
This function opens the tweets.txt file and counts the amount of occurences of each word in Amit's last 100 tweets.
The function creates the count_words.txt file and prints the counting results in it.
"""
def count_words():
    words = []
    words_dict = {}
    tweets_doc = open("tweets.txt", "r")
    lines = tweets_doc.readlines()
    for line in lines[1:]:
        if line.startswith("tweet number"):
            continue
        else:
            words.extend(line.split())
    chars = [',', '.', '!', '?', '״', '"', ':', '(', ')', '*'] #remove chars that arent part of the word
    for word in words:
        for char in chars:
            if char in word:
                word = word.replace(char, "")
        if len(word) != 0:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
    count_word_doc = open("count_words.txt", "a")
    for word in words_dict:
        count_word_doc.write(word + " : " + str(words_dict[word]) + "\n")


"""
This function gets a dictionary used for counting the occurences of each tag mention, 
a tweet element from the HTML code, the user, the browser and the user that posted the given tweet.
The function looks for all the tag mentions (@somename), creates the count_tags.txt file and prints the counting results in it.
"""
def tags_scraper(tags_dict, post, user, browser, posted_name):
    section = post.find_elements_by_css_selector('*[class = "r-18u37iz"]')
    browser.implicitly_wait(2)
    for t in section:
        if t.text[0]=='@' and posted_name == user:
            if t.text in tags_dict:
                tags_dict[t.text] += 1
            else:
                tags_dict[t.text] = 1


"""
This function gets a dictionary used for counting the occurences of each hashtag, 
a tweet element from the HTML code, the user, the browser and the user that posted the given tweet. 
The function looks for all the hashtags (#somehashtag), creates the count_hash.txt file and prints the counting results in it.
"""
def hash_scraper(hash_dict, post, user, browser, posted_name):
    section = post.find_elements_by_css_selector('*[class = "r-18u37iz"]')
    browser.implicitly_wait(2)
    if section is not None:
        for h in section:
            if h.text[0]=='#'and posted_name == user:
                if h.text in hash_dict:
                    hash_dict[h.text] += 1
                else:
                    hash_dict[h.text] = 1


"""
This function gets a new tweet element from the HTML code and the count variable (used for the printing). 
The function extracts the text part from the given tweet element and prints it in the tweets.txt file.
"""
def tweet_scraper(post, count):
    tweets_doc = open("tweets.txt", "a+")
    try: 
        tweet = post.find_element_by_xpath('./div[2]/div[2]/div[1]//span').text #extract text of tweet
    except NoSuchElementException:
        tweets_doc.write("tweet number " + str(count) + ": " + "NO TEXT IN THE TWEET." + "\n")
        return
    if '#' not in tweet and '@' not in tweet:
        tweets_doc.write("tweet number " + str(count) + ":" + "\n" + tweet + "\n")
    tweets_doc.close()



"""
This functions opens the browser and sets its page to the given URL (of Amit Segal's Twitter page). 
Then, it calls the above functions to create the required files.
"""
def main(url):
    webDriverFile = os.path.join(sys.path[0], 'chromedriver')
    os.chmod(webDriverFile, 755) #permissions
    browser = webdriver.Chrome(executable_path = webDriverFile)
    browser.get(url)
    browser.maximize_window()
    browser.implicitly_wait(10)
    name = url[20:]
    user = '@' + name

    tweets_doc = open("tweets.txt", "a+")
    tweets_doc.write("Last 100 tweets of {}: \n".format(user))
    tweets_doc.close()
    count_tags_doc = open("count_tags.txt", "a+")
    count_hash_doc = open("count_hash.txt", "a+")
    count = 1
    scrolling = True #can scroll
    tags_dict = {}
    hash_dict = {}
    posts = set()

    while count <= 100 and scrolling:
        tweets = browser.find_elements_by_xpath('//div[@data-testid="tweet"]') #gather the tweets in Amit Segal's page
        for post in tweets[-25:]:
            if post in posts:
                continue
            posts.add(post)
            posted_name = post.find_element_by_xpath('.//span[contains(text(), "@")]').text #by analyzing the HTML file- looking for the name of the publisher
            if posted_name == user:
                tweet_scraper(post, count)
                count += 1
            tags_scraper(tags_dict, post, user, browser, posted_name)
            browser.implicitly_wait(2)
            hash_scraper(hash_dict, post, user, browser, posted_name)
            if count > 100:
                break
        scrolling = scroll(browser)

    for tag in tags_dict:
        count_tags_doc.write(tag + " : " + str(tags_dict[tag]) + "\n")
    for hashtag in hash_dict:
        count_hash_doc.write(hashtag + " : " + str(hash_dict[hashtag]) + "\n")
    count_words()
    count_hash_doc.close()
    count_tags_doc.close()



if __name__ == '__main__':
    url = "https://twitter.com/amit_segal"
    main(url)
