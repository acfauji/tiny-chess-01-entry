import json,os,sys,urllib.error,urllib.request
E=os.environ.get("MAKEFUN_ENV_URL")or sys.exit("MAKEFUN_ENV_URL")
V={c:v for c,v in zip("pnbrqkPNBRQK",[1,3,3,5,9,100]*2)}
P=[100,-3,-4,-5,-6,-7,-8,-9,0]*2
D={}
for i in range(120):D[i]=0
for r in range(8):
 for f in range(8):D[21+r*10+f]=1
S=[-10,-1,1,10,-11,-9,9,11]
K=[-21,-19,-12,-8,8,12,19,21]
def J(p,b):
 try:
  with urllib.request.urlopen(urllib.request.Request(E+p,data=b,headers={"content-type":"application/json"}))as r:return json.load(r)
 except urllib.error.HTTPError as e:sys.exit(f"{p}: {e.code} {e.read().decode()}")
def B(f):
 for i in range(120):M[i]=0
 for i,r in enumerate(f.split()[0].split("/")):
  q=0
  for c in r:
   if c.isdigit():q+=int(c)
   else:M[21+i*10+q]=c;q+=1
 return f.split()[1]=="b"
def U(f,t):
 p=M[f];M[f]=0;M[t]=p
def V(f,t):
 p=M[t];M[t]=M[f];M[f]=0;return p
def G(w):
 L=[]
 for sq in range(21,99):
  if not D[sq]:continue
  p=M[sq]
  if not p:continue
  c=p.isupper()
  if c!=w:continue
  if p.lower()=="p":
   d=-10 if w else 10
   if D[sq+d]:L.append((sq,sq+d))
   if (w and sq//10==6)or(not w and sq//10==3):
    if D[sq+d]and D[sq+2*d]:L.append((sq,sq+2*d))
   if sq%10>0 and M[sq+d-1]and M[sq+d-1].isupper()!=w:L.append((sq,sq+d-1))
   if sq%10<9 and M[sq+d+1]and M[sq+d+1].isupper()!=w:L.append((sq,sq+d+1))
  elif p.lower()=="n":
   for d in K:
    if D[sq+d]and(M[sq+d]==0 or M[sq+d].isupper()!=w):L.append((sq,sq+d))
  elif p.lower()=="b":
   for d in(-11,-9,9,11):
    t=sq
    while D[t+d]:
     if M[t+d]==0:L.append((t,t+d))
     elif M[t+d].isupper()!=w:L.append((t,t+d));break
     else:break
     t+=d
  elif p.lower()=="r":
   for d in(-10,-1,1,10):
    t=sq
    while D[t+d]:
     if M[t+d]==0:L.append((t,t+d))
     elif M[t+d].isupper()!=w:L.append((t,t+d));break
     else:break
     t+=d
  elif p.lower()=="q":
   for d in(-11,-10,-9,-1,1,9,10,11):
    t=sq
    while D[t+d]:
     if M[t+d]==0:L.append((t,t+d))
     elif M[t+d].isupper()!=w:L.append((t,t+d));break
     else:break
     t+=d
  elif p.lower()=="k":
   for d in S+K:
    if D[sq+d]and(M[sq+d]==0 or M[sq+d].isupper()!=w):L.append((sq,sq+d))
 return L
def H(w):
 for sq in range(21,99):
  if not D[sq]:continue
  p=M[sq]
  if not p:continue
  if p.isupper()!=w:continue
  if p.lower()=="k":return sq
 return 0
def I(w):
 k=H(w)
 for sq in range(21,99):
  if not D[sq]:continue
  p=M[sq]
  if not p:continue
  if p.isupper()==w:continue
  if p.lower()=="p":
   d=10 if w else -10
   if sq+d in (k-1,k+1):return 1
  elif p.lower()=="n":
   for d in K:
    if sq+d==k:return 1
  elif p.lower()=="b":
   for d in(-11,-9,9,11):
    t=sq
    while D[t+d]:
     if M[t+d]:
      if M[t+d].isupper()!=w and M[t+d].lower()in"bq":return 1
      break
     t+=d
  elif p.lower()=="r":
   for d in(-10,-1,1,10):
    t=sq
    while D[t+d]:
     if M[t+d]:
      if M[t+d].isupper()!=w and M[t+d].lower()in"rq":return 1
      break
     t+=d
  elif p.lower()=="q":
   for d in(-11,-10,-9,-1,1,9,10,11):
    t=sq
    while D[t+d]:
     if M[t+d]:
      if M[t+d].isupper()!=w:return 1
      break
     t+=d
  elif p.lower()=="k":
   for d in S:
    if sq+d==k:return 1
 return 0
def E(w):
 s=0
 for sq in range(21,99):
  if not D[sq]:continue
  p=M[sq]
  if not p:continue
  v=P["pnbrqk".index(p.lower())]
  if p.isupper()!=w:s-=v
  else:s+=v
 return s
M=[0]*120
g=J("/game",b"{}")
while g["status"]!="done":
 while g["status"]=="your_move":
  w=g["colour"]=="w"
  B(g["fen"])
  d=3
  L=G(w)
  b=-9999;m=L[0]if L else(0,0)
  for f,t in L:
   c=V(f,t)
   v=-E(not w)
   if v>b:b=v;m=(f,t)
   U(f,t)
  if m==(0,0):break
  f,t=m
  s=f"{chr(97+(f%10-1))}{10-f//10}{chr(97+(t%10-1))}{10-t//10}"
  g=J("/move",json.dumps({"game":g["game"],"move":s}).encode())
  if g["status"]=="over":break
print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=sys.stderr)