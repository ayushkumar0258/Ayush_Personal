
def centered_average(nums):
  smallest=nums[0]
  largest=nums[0]
  for i in nums:
    if(i<smallest):
      smallest=i
    if(i>largest):
      largest=i

    rs=0
    rl=0
    s=0
    co=0
  for r in nums:
    if (r==smallest):
      rs=rs+1 ####1
    if(r==largest):
      rl=rl+1
    if((r!=smallest and r!=largest)):
      s=int(s+r)
      print (s)
      co=int(co+1)###1
      print(co)
    if(r==smallest and r>=2):
      s=int(s+r)
      co=int(co+1)
    if(r==largest and r>=2):
      s=int(s+r)
      co=int(co+1)
  print(co)
  print(s)              
  avg=int(s/co)
  print (avg)

centered_average([1, 2, 3, 4, 100])