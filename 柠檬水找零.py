class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                # 如果顾客使用的是5元 不用找零 5元数量+1
                five += 1
            elif bill == 10:
                # 如果顾客使用的是10元 需要找他5元 所以5元数量-1 10元数量+1
                five -= 1
                ten += 1
            else:
                if ten > 0:  # 顾客使用的是20元 如果我们有10元的 要尽量先给他10元的 再给他5元的 5元和10元都要-1
                    ten -= 1
                    five -= 1
                else:  # 顾客使用的是20元 而店员没有10元的 就只能给他找3个5元的 所以5元的数量要-3
                    five -= 3
            # 这里判断5元的数量 如果5元的数量<0 说明上面某一步找零的时候5元不够了 即没法给顾客找零 直接返回false
            if five < 0:
                return False
        return True
