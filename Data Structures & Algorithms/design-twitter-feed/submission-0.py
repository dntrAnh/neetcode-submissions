class Twitter:

    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        min_heap = []

        self.follow_map[userId].add(userId)
        for followee in self.follow_map[userId]:
            if followee in self.tweet_map:
                idx = len(self.tweet_map[followee]) - 1
                count, tweet_id = self.tweet_map[followee][idx]
                heapq.heappush(min_heap, [count, tweet_id, followee, idx - 1])
        
        while min_heap and len(result) < 10:
            count, tweet_id, followee, idx = heapq.heappop(min_heap)
            result.append(tweet_id)
            if idx >= 0:
                count, tweet_id = self.tweet_map[followee][idx]
                heapq.heappush(min_heap, [count, tweet_id, followee, idx - 1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
