def two_sum(values, target):
    found_diffs = dict()
    for i, v in enumerate(values):
        if v in found_diffs:
            return (found_diffs[v], i)
        diff = target - v 
        found_diffs[diff] = i
    return None
    
    
if __name__ == "__main__":
  result = two_sum([2, 1, 4, 6, 3, 10], 6)
  print(result)
  result = two_sum([2, 1, 4, 6, 3, 10], 20)
  print(result)
  result = two_sum([2, 1, 4, 6, 3, 10], 5)
  print(result)
  result = two_sum([2, 1, 4, 6, 3, 10], 7)
  print(result)
  result = two_sum([2, 1, 4, 6, 3, 10], 14)
  print(result)
