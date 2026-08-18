class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        l1 = len(sentence1)
        l2 = len(sentence2)

        if l1 != l2:
            return False
        
        for i in range(l1):
            if sentence1[i] == sentence2[i]:
                continue

            found = False

            for pair in similarPairs:
                if sentence1[i] in pair and sentence2[i] in pair:
                    found = True
                    break

            if not found:
                return False
        
        return True