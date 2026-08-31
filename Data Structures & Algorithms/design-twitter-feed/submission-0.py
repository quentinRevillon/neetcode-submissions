class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = []

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        i=-1
        while len(feed)<10 and abs(i)<=len(self.tweets):
            if self.tweets[i][0] in self.following[userId] or self.tweets[i][0]==userId:
                feed.append(self.tweets[i][1])
            i-=1
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
