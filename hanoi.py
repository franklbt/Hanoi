import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
from matplotlib.patches import Rectangle

#Parametres
draw_all_step = False
n_disk = 4

#Algorithme
def hanoi(T):
    n=len(T)
    l=len(T[0])
    draw_table(T[:])
    plt.show()
    while True:
        #deplacement du plus petit element
        m=colone_min(T)
        pop(T[m])
        if n_disk%2==0:m=(1+m)%n
        else : m=(m-1)%n
        push(T[m],1)
        draw_step(T)
        #Condition d'arret (marche que pour les nobres pairs)
        if T==[[0]*l,[0]*l,[l-i for i in range(0,l)]] or T==[[0]*l,[l-i for i in range(0,l)],[0]*l]:break
        #Permutation d'un autre element
        c=colone_max(T)
        a=0
        for i in range(0,n):
            if i!=c and i!=m: a=i
        e=first(T[a])[1]
        if e==0:
            e2=first(T[c])[1]
            pop(T[c])
            push(T[a],e2)
        else:
            pop(T[a])
            push(T[c],e)
        draw_step(T)
    draw_table(T[:])
    plt.show()

#fonctions de dessin
def table_init(n): return [[n-i for i in range(0,n)],[0]*n,[0]*n]

def draw_rect(ax,x0,y0,x1,y1):
    bb = Bbox([[x0, y0], [x1, y1]])
    p_bbox = Rectangle((bb.xmin, bb.ymin), abs(bb.width), abs(bb.height), ec="k")
    ax.add_patch(p_bbox)

def draw_disk(ax,Nmax,t,n,P):
    draw_rect(ax, (Nmax+1)*(P-0.5)-0.5*n,t,(Nmax+1)*(P-0.5)+0.5*n,t+1)

def draw_table(T):
    n=len(T[0])
    ax = plt.subplot(1, 1, 1)
    for i in enumerate(T):
        for j in enumerate(i[1]):
            draw_disk(ax,n,j[0],j[1],i[0]+1)
    ax.set_xlim(0., 3*(n+1))
    ax.set_ylim(0., n+1)
    plt.draw()

def draw_step(T):
    if draw_all_step:
        draw_table(T)
        plt.show()
    else: print(T)


#Helpers

#retourne position et valeur du premier disque d'une pile.
def first(C):
    n=len(C)
    f=0,0
    if C[0]==0: return (-1,0)
    if C[n-1]!=0: return (n-1,C[n-1])
    for i in enumerate(C):
        if i[0]<n-1 and C[i[0]+1]==0: return i

# retourne colonne contenant l'element maxi
def colone_max(T):
    v,c=0,0
    for i in enumerate(T):
        if first(i[1])[1] > v:
            v,c= first(i[1])[1],i[0]
    return c

# retourne colonne contenant l'element mini (1)
def colone_min(T):
    m=0
    F=[first(T[i]) for i in range(0,len(T))]
    for i in enumerate(F):
       if i[1][1] == 1: m=i[0]
    return m

#enleve dernier element d'une pile
def pop(C):
    C[first(C)[0]]=0

#ajoute element a une pile
def push(C,e):
    C[(first(C)[0]+1)%len(C)]=e

hanoi(table_init(n_disk))
