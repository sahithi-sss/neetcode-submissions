class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = 0
        if (len(s) != len(t)):
            flag = 1
        else :
            s_sorted = ''.join(sorted(s))
            t_sorted = ''.join(sorted(t))
            s_list = []
            t_list = []
            #print(s_sorted)
            #print(t_sorted)
            #print(type(t_sorted))
            flag2 = 0
            for j in range(len(t_sorted)):
                if (flag2 == 0):
                    if (s_sorted[j] != t_sorted[j]):
                        flag2 = 1
                        break
            
            if (flag2 == 1):
                flag = 1
        
        if (flag == 1):
            return False
        else :
            return True
                    
                    
            
