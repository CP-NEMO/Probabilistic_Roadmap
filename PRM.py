from matplotlib import pyplot as plt
import math
import random


def Collision_test_cord(x,y):
  if(x>ObsX_max or x<ObsX_min):
    return 1
  else:
    if (y> ObsY_max):
      return 1 
    else:
      return 0
  
def nearest_neighbour(x,y,i):
  for j in range(i+1, len(Xco)):
    d = 0
    d = (((x-Xco[j])**2) + ((y-Yco[j])**2))**0.5
      # print("D = ",d)
    if d>step_size:
      pass
    else:
      X_edge.append([x, Xco[j]])
      Y_edge.append([y, Yco[j]])
      X_edge.append([ Xco[j], x])
      Y_edge.append([Yco[j], y])
      Dis.append(d)
      # print(" x = %s and Xco = %s " %(Xco[j],x))
      # print(" y = %s and Yco = %s " %(Yco[j],y))
      # print("And D = ", d)

def sampeling():
  x = random.uniform(0,100)
  y = random.uniform(0,100)
  a = Collision_test_cord(x,y)
  if a == 0:
    # print("x,y =", x,y)
    return 0
  Xco.append(x)
  Yco.append(y)
  return 0
#========================================Query Phase=================================================================#
def path_finding(sx, sy, gx, gy):
  sums = 0
  for i in range(len(X_edge)):
    lis = []
    index = []
    # print("SX,SY = ", sx,sy)
    for j in range(len(X_edge)):
      if dup_X[j][0] == sx:
        if dup_Y[j][0] == sy:
          lis.append([dup_X[j][1], dup_Y[j][1]])
          index.append(i)
    # print(lis)
    if len(lis) == 1:
      path_nodeX.append([sx,lis[0][0]])
      path_nodeY.append([sy,lis[0][1]])
      sx = lis[0][0]
      sy = lis[0][1]
    if len(lis)>1:
      temp = ((lis[0][0]- gx)**(2)+ (lis[0][1]-gy)**(2))**(0.5)
      a = 0
      for i in range(len(lis)):
        if temp>(((lis[i][0]- gx)**(2)+ (lis[i][1]-gy)**(2))**(0.5)):
          temp = (((lis[i][0]- gx)**(2)+ (lis[i][1]-gy)**(2))**(0.5))
          a = i
        path_nodeX.append([sx, lis[a][0]])
        path_nodeY.append([sy, lis[a][1]])
        sx = lis[a][0]
        sy = lis[a][1]
    if (sx,sy) == (gx,gy):
      return 0

#-----------------------------------------Pre-Defined Characters-----------------------------------------------------#
path_nodeX = []
path_nodeY = []
prev_node = []
X_edge = []
Y_edge = []
Dis = []
Xco = []
Yco = []
step_size = 10
vx= [40,40,60,60]
vy= [ 0,48,48, 0]
ObsX_min = min(vx)-2
ObsX_max = max(vx)+2
ObsY_max = max(vy)+2
ObsY_min = min(vy)-2
Collision_point = 1
steps = int(input("Please Input the no of nodes between 450 - 1000: "))
dup_X = X_edge
dup_Y = Y_edge
#---------------------------------------------------------------------------------------------------------------------#    


def ploting(): 
  
  plt.plot(0,100)
  plt.plot(100,0)
  num = int(len(vx)/4)
  for i in range(1,num+1):
  		plt.plot([vx[4*(i-1)],vx[4*(i-1)+1],vx[4*(i-1)+2],
		vx[4*(i-1)+3],vx[4*(i-1)]],[vy[4*(i-1)],vy[4*(i-1)+1],
		vy[4*(i-1)+2],vy[4*(i-1)+3],vy[4*(i-1)]],color = '#FF8C02',linestyle = '-',lw=3)	
  plt.scatter(Xco,Yco,c = 'blue',s = 100, edgecolor='black', linewidth = 1, alpha= 0.75)
  plt.scatter(start_coordinate[0],start_coordinate[1], c = 'red', s = 200, edgecolor = 'black', linewidth = 1, alpha = 0.75)
  plt.scatter(end_coordinate[0],end_coordinate[1], c = 'green', s = 200, edgecolor = 'black', linewidth = 1, alpha = 0.75)
  for j in range(len(X_edge)):
    #for i in range(len(X_edge[j])):
    plt.plot(X_edge[j], Y_edge[j], color = '#37393d', linestyle = '-', lw = 0.5)
    # print("Edge = {}", j)
  for i in range(len(path_nodeX)):
    plt.plot(path_nodeX[i], path_nodeY[i], color = '#02FFB4',linestyle = '-',lw=4)
  plt.show()

if __name__ == "__main__":
  for i in range(steps):
    sampeling()
  
  for i in range(len(Xco)):
    # print("Sending X, Y")
    nearest_neighbour(Xco[i], Yco[i], i)
  
  start_coordinate = []
  start_coordinate.append(int(input("Give start coordinates x: ")))
  start_coordinate.append(int(input("Give start coordinates y: ")))
  nearest_neighbour(start_coordinate[0], start_coordinate[1],0)
  end_coordinate = []
  end_coordinate.append(int(input("Give end coordinates x: ")))
  end_coordinate.append(int(input("Give end coordinates y: ")))
  nearest_neighbour(end_coordinate[0], end_coordinate[1],0)


  path_finding(start_coordinate[0], start_coordinate[1], end_coordinate[0], end_coordinate[1])
        
  print("Potting")
  ploting()
