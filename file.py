def  function(n):
    if n == 0:
        retrun 0 
    if n == 1:
        return 1
    return  function(n-1) + function(n-2)
