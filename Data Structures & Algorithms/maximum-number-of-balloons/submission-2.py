class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        cnt_balloon = Counter("balloon")
        r = len(text)
        for key, val in cnt_balloon.items():
            r = min(r, cnt[key]//val)

        return r