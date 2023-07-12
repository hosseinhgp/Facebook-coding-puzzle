# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  indexB=[]
  indexP=[]
  for i in range(N):
    if C[i]=='B':
      indexB.append(i)
    elif C[i]=='P':
      indexP.append(i)
  #print(indexB,indexP)
  result=0
  for i,c in enumerate(C):
    if c=='A':
      rightB=righcount(i,indexB,X,Y)
      rightP=righcount(i,indexP,X,Y)
      leftB=leftcount(i,indexB,X,Y)
      leftP=leftcount(i,indexP,X,Y)
      #print(i,rightB,leftP ,leftB,rightP)
      result += rightB*leftP + leftB*rightP
  return result
def righcount(a: int,indexs: list,x: int,y:int):
  count=0
  for o in indexs:
    #print('right',a,o,X,Y)
    if Y>=o-a>=X :
      #print('r if')
      count+=1
  return count
def leftcount(a: int,indexs: list,x: int,y:int):
  count=0
  for o in indexs:
    #print('left',a,o,X,Y)
    if Y>=a-o>=X:
      #print('l if')
      count+=1
  return count
