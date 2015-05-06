import praw

user_agent = "Saved Links/Comments Filter by /u/cerealb0x"
r = praw.Reddit(user_agent = user_agent)


r.login('cerealb0x', ‘????’)
#login to account

desiredSubreddit = "comicbooks"
#set the desired subreddit that we need to filter out links for

thing_limit = 50
#set a limit for how many saved links/comments to go through
gen = r.user.get_saved(thing_limit)
#retrieve account's saved comments/links

count = 0
filteredLinks = []
for thing in gen:
    subreddit = thing.subreddit.display_name
    if subreddit == desiredSubreddit:
        #if thing != praw.objects.Comment:
            filteredLinks.append(thing.url)
            count += 1


import pprint
pprint.pprint(filteredLinks)
pprint.pprint(count)
