def bm(s):
  root= 100
  while True:
    y= root
    root= 0.5*(root+(s/root))
    if root== y:
      return(root)
      break
s= float(input("Give the number:"))
print(bm(s))
