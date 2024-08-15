class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        t = 0
        d = {5:0,10:0,20:0}
        for x in range(len(bills)):
            if bills[x] == 5:
                d[5] += 1
            else:
                if bills[x] == 10:
                    if d[5] >= 1:
                        d[5] -= 1
                        d[10] += 1
                    else:
                        return False
                if bills[x] == 20:
                    if (d[5] >= 1 and d[10] >= 1) or d[5] >= 3:
                        if (d[5] >= 1 and d[10] >= 1):
                            d[5] -= 1
                            d[10] -= 1
                            d[20] += 1
                        else:
                            d[5] -= 3
                            d[20] += 1
                    else:
                        return False
        return True

            
           
                
