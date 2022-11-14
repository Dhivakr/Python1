li=[1,2,3,4,5,6,7]
steps=int(input("how many times we rotate elements  : "))
def reverse(li,steps):
   for i in range(1,steps+1):
      c=li[-i]
      li.insert(0,c)
   for i in range(0,steps):
      li.pop()
   print(li)
reverse(li,steps)