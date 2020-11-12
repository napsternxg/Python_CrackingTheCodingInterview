"""
Given a digit e.g. 5 and a number put the digit in the number so that the number is maximized. 
E.g. num=268, digit=5
Max is 5268

Should also work for negative numbers:
num=-999, digit=5
Max=-5999

"""

def maximize_num(num, digit=5):
    is_negative = num < 0
    num = -num if is_negative else num
    str_num = str(num)
    possible_nums = []
    for i in range(len(str_num)):
        new_num = int(str_num[:i]+str(digit)+str_num[i:])
        possible_nums.append(new_num)
    best = -min(possible_nums) if is_negative else max(possible_nums)
    return best
    
    
if __name__ == "__main__":
  test_nums = [268, 670, 0, -999]
  print([maximize_num(num, digit) for num in test_nums])



