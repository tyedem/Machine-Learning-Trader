import psaw
import pandas as pd
import datetime as dt
import csv
from pathlib import Path
import os


#Lookup function to run
def search_comments(search_term,start_date, end_date, subreddits_to_search):
    """Date needs to be in "yyyy-mm-dd format" """
 
    start_epoch=int(dt.datetime.strptime(start_date,'%Y-%m-%d').timestamp())
    end_epoch=int(dt.datetime.strptime(end_date,'%Y-%m-%d').timestamp())

    api = psaw.PushshiftAPI()
    generator = []
    for i in search_term:
        holder = list(api.search_comments(q = i, limit = None, after = start_epoch, before = end_epoch, subreddit = subreddits_to_search))
        generator = generator + holder
    search_results = pd.DataFrame([submission.d_ for submission in generator])
    pd.set_option('display.max_columns', None)
    search_results = search_results[['author','subreddit','body','id','link_id','created_utc','created','permalink']]
    search_results['body'] = search_results['body'].str.upper()  
    print(search_results.head())
    joined_term = '-'.join(search_term)
    save_phrase = joined_term + "-" + c[1] + ".csv"
    save_path = Path("./reddit_output/" + save_phrase)
    search_results.to_csv(save_path)

#Set parameter lists for function call, chop into blocks for easier lookup and access in case of timeouts.
# issue = [("AAPL","Apple"),("TSLA","Tesla")]
# periods = [("2020-03-01","2020-03-31"),("2020-04-01","2020-04-30")]
# search_list = ["canadianInvestor"]

issue = [("AAPL","Apple"),("TSLA","Tesla"),("AMZN","Amazon"),("MSFT","Microsoft"),
("Goog","Google"),("TWTR","Twitter"),("FB","Facebook"),("SJM","Smuckers"), ("BMO", "Bank of Montreal"),("TRI", "Thomson Reuters"),("GIL", "Gildean")
]
periods = [("2017-01-01","2017-12-31"),("2018-01-01","2018-12-31"),("2019-01-01","2019-12-31"),("2020-01-01","2020-12-31"),("2021-01-01","2021-12-31"),("2022-01-01","2022-02-28")]
search_list = ["canadianInvestor"]

#if file exists, do not lookup stock/period
file_folder = os.listdir("reddit_output")

#Doesn't handle multiple symbols

for i in issue:
    for c in periods:
        joined_term = '-'.join(i)
        save_phrase = joined_term + "-" + c[1] + ".csv"
        if save_phrase not in file_folder:
            print(save_phrase)
            search_comments(i,c[0],c[1],search_list)
