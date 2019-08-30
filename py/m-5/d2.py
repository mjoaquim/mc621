INT_SIZE = 20
def ORsum(arr, n): 

    zerocnt = [0 for i in range(INT_SIZE)] 
  
    for i in range(INT_SIZE):     
        for j in range(n):     
            if not (arr[j] & (1 << i)): 
                zerocnt[i] += 1            
    ans = 0
    for i in range(INT_SIZE): 
        ans += ((2 ** n - 1) - (2 ** zerocnt[i] - 1)) * 2 ** i 
  
    return ans 
  
# Driver code 
  
arr= [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,6513,123123512,4123214,2421,4214,215,12512,3412,51,34,123,213,124021421931231232312,321321,321321,35,6,6,3,123,15,21,123,213,123,4,13,12,3] 
size = len(arr) 
print(ORsum(arr, size)) 