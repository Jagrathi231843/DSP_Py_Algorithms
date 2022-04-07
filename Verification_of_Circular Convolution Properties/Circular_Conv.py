import numpy as np
import operator as op
def circular_conv(x,h):
  N=max(len(x),len(h))
  x1=np.zeros((N))
  h1=np.zeros((N))
  y=np.zeros((N))
  for i in range(len(x)):
    x1[i]=x[i]
  for i in range(len(h)):
    h1[i]=h[i]
  for i in range(N):
    for j in range(N):
      y[i]=y[i]+x1[j]*h1[op.mod((i-j),N)]
  return y
def comp_array(lhs,rhs):
  cnt=0
  for i in range(len(lhs)):
    if(lhs[i]==rhs[i]):
      cnt+=1
  return len(lhs),cnt
x=input('Enter the input signal=')
a=[int(i) for i in x.split()]
y=input('Enter the input signal=')
b=[int(i) for i in y.split()]
z=input('Enter the input signal=')
c=[int(i) for i in z.split()]
## commutative property
lhs=circular_conv(a,b)
rhs=circular_conv(b,a)
[len1,len2]=comp_array(lhs,rhs)
if(len1==len2):
  print("commutative property is satisfied")
  print("result is",lhs)
else:
  print("not sarisfied1")

##assosiative property a*(b*c)=(a*b)*c
lhs1=circular_conv(a,circular_conv(b,c))
rhs1=circular_conv(circular_conv(a,b),c)
[len1,len2]=comp_array(lhs,rhs)
if(len1==len2):
  print("satisfied")
  print("result is ",lhs1)
else:
  print("not satisfied")

# distributive property a*(b+c)=a*b + a*c
lhs2=circular_conv(a,(b+c))
rhs2=circular_conv(a,b)+circular_conv(a,c)
[len1,len2]=comp_array(lhs2,rhs2)
if(len1==len2):
  print("satisfied")
  print("result is=",lhs2)
else:
  print("not satisfied")
