import heapq
from collections import deque


class Node:
    def __init__(self, val, order):
        self.val = val
        self.next = None
        self.order = order


class Twitter:
    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = Node(tweetId, self.count)
        else:
            head = self.tweetMap[userId]
            curr = Node(tweetId, self.count)
            curr.next = head
            self.tweetMap[userId] = curr
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        self.followMap[userId].add(userId)
        for u in self.followMap[userId]:
            if u in self.tweetMap:
                curr = self.tweetMap[u]
                heapq.heappush(heap, (-curr.order, curr))
        heapq.heapify(heap)
        while len(heap) and len(res) < 10:
            frst = heapq.heappop(heap)
            node = frst[1]
            res.append(node.val)
            if node.next:
                heapq.heappush(heap, (-node.next.order, node.next))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
