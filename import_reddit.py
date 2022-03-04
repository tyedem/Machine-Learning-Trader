import praw
import psaw
import pandas as pd
import datetime as dt
import csv
from pathlib import Path

def search_comments(search_term,start_date, end_date):
    """Date needs to be in "yyyy-mm-dd format" """

    r = praw.Reddit("BASE")
 
    subreddits_to_search = ['wallstreetbets']

    start_epoch=int(dt.datetime.strptime(start_date,'%Y-%m-%d').timestamp())
    end_epoch=int(dt.datetime.strptime(end_date,'%Y-%m-%d').timestamp())

    api = psaw.PushshiftAPI()

    generator = list(api.search_comments(q = search_term, limit = 500, after = start_epoch, before = end_epoch, subreddit = subreddits_to_search))

    search_results = pd.DataFrame([submission.d_ for submission in generator])
    pd.set_option('display.max_columns', None)
    search_results = search_results[['author','subreddit','body','id','link_id','created_utc','created','permalink']]
    search_results['body'] = search_results['body'].str.upper()  
    print(search_results.head())
    save_path = Path("./reddit_output/" + search_term + ".csv")
    search_results.to_csv(save_path)

issue = ["Tesla", "QQQ","AMC"]
for i in issue:
    search_comments(i,"2020-01-01","2020-01-31")