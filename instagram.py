from instapy import InstaPy

session = InstaPy(username="python_trying_sabbir", password="sabbir2020hack")
session.login()

session.set_relationship_bounds(enabled=True, max_followers=200)
session.set_do_follow(True, percentage=100)
session.like_by_tags(["bmw", "code"], amount=3)
session.set_dont_like(["nsfw"])
session.end()