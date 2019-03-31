import numpy as np
from operator import itemgetter
import copy


def state_space_tree(info):
    Matrix=info[0]
    Cost=info[1]
    Visited=info[2]
    Root=info[3]

    if len(Visited)==len(vertices):
        #print(matrices)
        return Visited,Cost
        
    for x in range(len(leaf)):
        if np.allclose(Matrix,leaf[x][0]) and Cost==leaf[x][1] and Visited==leaf[x][2] and Root==leaf[x][3]:
            leaf.pop(x)
            break
        
    for node in graph[Root]:
        cost=0
        if node not in Visited:
            root=copy.deepcopy(Root)
            visited=copy.deepcopy(Visited)
            matrix=copy.deepcopy(Matrix)
            cost=copy.deepcopy(Cost)

            visited.append(node)
            for v in visited:
                matrix[node][v]=np.inf
            matrix[root,...]=[np.inf]*len(matrix)
            matrix[...,node]=[np.inf]*len(matrix)

            matrix,cost=reduce(matrix)
            matrices.append(matrix)
            cost=cost+Cost+int(Matrix[Root][node])
            info=[matrix,cost,visited,node]
            leaf.append(info)

    info=min(leaf,key=itemgetter(1))
    return state_space_tree(info)

def reduce(matrix):
    cost=0
    row_min=np.min(matrix,axis=1).reshape(-1,1)
    row_min[row_min==[np.inf]]=[0]
    cost=cost+int(sum(row_min))
    matrix=matrix-row_min

    col_min=np.min(matrix,axis=0)
    col_min[col_min==np.inf]=0
    cost=cost+int(sum(col_min))
    matrix=matrix-col_min

    return matrix,cost

def user_input():
    matrix=[]
    graph={}
    print("Graph nodes should be numbered 1 to n")
    n=int(input("Enter n number of nodes"))
    print("Enter the Cost matrix\nEnter inf for infinity\n")
    
    matrix.append([np.inf]*(n+1))
    for i in range(n):
        print("Enter for node",i+1)
        str_matrix=list(input().split(' '))
        t_matrix=[np.inf if a=='inf' else int(a) for a in str_matrix]
        matrix.append([np.inf]+t_matrix)
    matrix=np.array(matrix)
    #print(matrix)
    
    print("\nEnter adjacency Matrix")
    for i in range(1,n+1):
        print("Enter nodes adjacent to node",i)
        str_nodes=input().split(' ')
        nodes=[int(a) for a in str_nodes]
        graph[i]=nodes
    #print(graph)
    
    s=int(input("Enter start node"))
    vertices=list(graph.keys())
    
    return matrix,graph,s,vertices


#start=1
#matrix=np.array([[np.inf,np.inf,np.inf,np.inf,np.inf,np.inf],[np.inf,np.inf,20,30,10,11],[np.inf,15,np.inf,16,4,2],[np.inf,3,5,np.inf,2,4],[np.inf,19,6,18,np.inf,3],[np.inf,16,4,7,16,np.inf]])
#matrix=np.array([[np.inf,np.inf,np.inf,np.inf,np.inf,np.inf],[np.inf,np.inf,2,np.inf,12,5],[np.inf,2,np.inf,4,8,np.inf],[np.inf,np.inf,4,np.inf,3,3],[np.inf,12,8,3,np.inf,10],[np.inf,5,np.inf,3,10,np.inf]])
#graph={1:[2,3,4,5],2:[1,3,4,5],3:[1,2,4,5],4:[1,2,3,5],5:[1,2,3,4]}
#graph={1:[2,4,5],2:[1,3,4],3:[2,4,5],4:[1,2,3,4],5:[1,3,4]}
#vertices=list(graph.keys())
     
leaf=[]
matrices=[]

matrix,graph,start,vertices=user_input()
matrix,cost=reduce(matrix)
info=[matrix,cost,[start],start]
leaf.append(info)
Visited,Cost=state_space_tree(info)
path=[str(a) for a in Visited]
print("Path taken","->".join(path))
print("Cost=",Cost)
