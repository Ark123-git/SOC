def show(*number):
    val=1
    for i in number:
        val=val*i
    return val 
        
ans=show(2,3,4,5)
print(ans)

