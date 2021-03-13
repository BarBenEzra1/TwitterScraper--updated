# TwitterScraper - updated
This is a Twitter Scraper project based Selenium Python.
My IDE : Visual Studio Code.
The code logs in to Amit Segal's twitter, takes the last 100 tweets and provides the following output files:
1. **Tweets List** - tweets.txt file
2. **Hashtag list**- count_hash.txt file
3. **Mention list**- count_tags.txt file
4. **Word statistics** - count_words.txt file

**The functions in the code:**
1. **scroll(browser)** - this function gets the open browser as a parameter and scrolls it down. The browser will try to scroll at most 3 times in case it fails to (might happen if the page wasn't loaded yet, so the new and last positions are equals). The scrolling lasts till the main function runs over 100 tweets.
2. **tweet_scraper(post, count)** - this function gets a new tweet element from the HTML code and the count variable (used for the printing). The function extracts the text part from the given tweet element and prints it in the tweets.txt file.
4. **tags_scraper(tags_dict, post, user, browser, posted_name)** - this function gets a dictionary used for counting the occurences of each tag mention, a tweet element from the HTML code, the user, the browser and the user that posted the given tweet. The function looks for all the tag mentions (@somename), creates the count_tags.txt file and prints the counting results in it.
5. **count_words()** - this function opens the tweets.txt file and counts the amount of occurences of each word in Amit's last 100 tweets. The function creates the count_words.txt file and prints the counting results in it.
6. **hash_scraper(hash_dict, post, user, browser, posted_name)** - this function gets a dictionary used for counting the occurences of each hashtag, a tweet element from the HTML code, the user, the browser and the user that posted the given tweet. The function looks for all the hashtags (#somehashtag), creates the count_hash.txt file and prints the counting results in it.
7. **main(url)** - this functions opens the browser and sets its page to the given URL (of Amit Segal's Twitter page). Then, it calls the above functions to create the required files.

**Run the code:**
In order to run the code, download the TwitterScraper.zip to your computer and read the README.md file (😜).
Open the code in your IDE and make sure you have Selenium installed in your pc, otherwise, use the "pip install selenium" command.
Now, run the code in terminal from the path to the TwitterScraper directory (command: python (or python3) TwitterScraper.py) and wait (!) for the Chrome browser that has been opened at the beginning to get **closed** by itself. Selenium basically sends queries to the HTTP server for each Selenium command and interupting the process, such as, changing the URL of the Chrome browser or scroll the page by yourself (etc.) may cause errors.
The running process might take approximately 5 minutes since waiting for the HTTP server to send its answers takes time.

**The test:**
In order to test the code, I have created my own input- a twitter user @BarBenEzra2, and uploaded 10 tweets, so after executing the code, the test will compare the outputs with the expected results. I run the test on a "static" twitter page, that is foretold, since the outputs of another user's page might change and so- can not be checked with this test.
You can run the test (command: python (or python3) Test.py) and checks if OK.
