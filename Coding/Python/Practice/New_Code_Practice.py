def has22(nums):
  for i in range (len(nums)):
      if (nums[i]==2 and nums[i+1]==2):
          return True
  return False
    
has22([4, 2, 4, 2, 2, 5]) 