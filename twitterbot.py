# -*- coding:utf-8 -*-
import tweepy
import schedule
import timeset

CONSUMER_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
CONSUMER_SECRET = "XXXXXXXXXXXXXXXXXXXXXXX"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

ACCESS_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
ACCESS_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
def tweet(tweetcontent):
	api.update_status(status=tweetcontent)

def zero():
	tweet("12           1212121212\n  12       12  12    12\n    12   12    12    12\n      1   2      12    12\n    12   12    12    12\n  12       12  12    12\n12          1212121212時だにゃ!")
def one():
	tweet("1時だよー")
def two():
	tweet("2時だよー")
def three():
	tweet("3時だよー")
def four():
	tweet("4時だよー")
def five():
	tweet("5時だよー")
def six():
	tweet("6時だよー")
def seven():
	tweet("7時だよー")
def eight():
	tweet("8時だよー")
def nine():
	tweet("9時だよー")
def ten():
	tweet("10時だよー")
def eleven():
	tweet("11時だよー")
def twelve():
	tweet("12           1212121212\n  12       12  12    12\n    12   12    12    12\n      1   2      12    12\n    12   12    12    12\n  12       12  12    12\n12          1212121212時だにゃ!")
def thirteen():
    tweet("13時だよー")
def fourteen():
    tweet("14時だよー")
def fifteen():
    tweet("15時だよー")
def sixteen():
    tweet("16時だよー")
def seventeen():
    tweet("17時だよー")
def eighteen():
    tweet("18時だよー")
def nineteen():
    tweet("19時だよー")
def twenty():
    tweet("20時だよー")
def twentyone():
    tweet("21時だよー")
def twentytwo():
    tweet("22時だよー")
def twentythree():
    tweet("23時だよー")

schedule.every().day.at("0:00").do(zero)
schedule.every().day.at("1:00").do(one)
schedule.every().day.at("2:00").do(two)
schedule.every().day.at("3:00").do(three)
schedule.every().day.at("4:00").do(four)
schedule.every().day.at("5:00").do(five)
schedule.every().day.at("6:00").do(six)
schedule.every().day.at("7:00").do(seven)
schedule.every().day.at("8:00").do(eight)
schedule.every().day.at("9:00").do(nine)
schedule.every().day.at("10:00").do(ten)
schedule.every().day.at("11:00").do(eleven)
schedule.every().day.at("12:00").do(twelve)
schedule.every().day.at("13:00").do(thirteen)
schedule.every().day.at("14:00").do(fourteen)
schedule.every().day.at("15:00").do(fifteen)
schedule.every().day.at("16:00").do(sixteen)
schedule.every().day.at("17:00").do(seventeen)
schedule.every().day.at("18:00").do(eighteen)
schedule.every().day.at("19:00").do(nineteen)
schedule.every().day.at("20:00").do(twenty)
schedule.every().day.at("21:00").do(twentyone)
schedule.every().day.at("22:00").do(twentytwo)
schedule.every().day.at("23:00").do(twentythree)

while True:
	schedule.run_pending()
	time.sleep(1)

## thanks @raspi0124
