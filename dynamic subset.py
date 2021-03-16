def subset_sum(num, sum):
   t=[[False for x in range(sum+1)]for y in range(len(num)+1)]
   for i in range(len(num)+1):
      for j in range(sum+1):
         if j==0:
            t[i][j]= True
   for i in range(len(num)):
      for j in range(sum+1):
         if num[i-1]<=j:
            t[i][j]=t[i-1][j-num[i-1]]or t[i-1][j]
         else:
            t[i][j]=t[i-1][j]
   return t[len(num)-1][sum]

print(subset_sum([1, 2, 3, 7], 6))
print(subset_sum([1, 2, 7, 1, 5], 10))
print(subset_sum([1, 3, 4, 8], 6))
