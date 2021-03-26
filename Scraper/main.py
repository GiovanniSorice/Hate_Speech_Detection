from Scweet.Scweet.scweet import scrap
from Scweet.Scweet.user import get_user_information, get_users_following, get_users_followers
from datetime import datetime, date

if __name__ == "__main__":
    # scrape top tweets with the words 'covid','covid19' in proximity and without replies.
    # the process is slower as the interval is smaller (choose an interval that can divide the period of time betwee, start and max date)

    start_date = date(2020,12,1)
    max_date = date(2021,3,24)
    interval = (max_date - start_date).days
    account_username = 'perchetendenza'
    limit_of_tweets = 100
    data = scrap(start_date=start_date.strftime("%Y-%m-%d"), max_date=max_date.strftime("%Y-%m-%d"), from_account=account_username, interval=interval,
                headless=True, display_type="Top", save_images=False, resume=False, filter_replies=True, proximity=False, limit=limit_of_tweets)

    data = data['Text']
    data.to_csv("tweets_{}.csv".format(account_username))
