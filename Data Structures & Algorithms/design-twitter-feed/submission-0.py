
class Twitter:
    def __init__(self):
        self.tweets = []
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []

        following = self.followMap[userId]

        following.add(userId)

        for i in range(len(self.tweets) - 1, -1, -1):
            
            user, tweet = self.tweets[i]

            if user in following:
                res.append(tweet)

            if len(res) == 10:
                break

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        
        self.followMap[followerId].add(followeeId)



    def unfollow(self, followerId: int, followeeId: int) -> None:
        
       if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)