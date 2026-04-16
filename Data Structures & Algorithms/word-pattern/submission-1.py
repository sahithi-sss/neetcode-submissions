class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = []
        w = ""
        s += " "
        for c in s:
            if c == " ":
                words.append(w)
                w = ""
            else:
                w = w + c
        #print(words)
        WTP = defaultdict(int) #word to pattern
        for word in words:
            WTP[word] += 1
        
        #print(list(WTP.items()))
        
        PTP = defaultdict(int)
        for c in pattern:
            PTP[c] += 1

        #print(list(PTP.items()))

        
        if list(WTP.values()) == list(PTP.values()):
            return True
        else:
            return False

        