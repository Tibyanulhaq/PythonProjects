from instabot import Bot

bot=Bot()
bot.login(username="",password="")
bot.follow("")
bot.unfollow("")
bot.upload_photo("",caption="")
bot.send_message("",["",""])

followers=bot.get_user_followers()
for follower in followers:
    print(bot.get_user_info(follower))

following=bot.get_user_following()
for follow in following:
    print(bot.get_user_info(follow))