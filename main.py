import json,os,sys,urllib.error,urllib.request
E=os.environ.get("MAKEFUN_ENV_URL")or sys.exit("MAKEFUN_ENV_URL")
V={"p":1,"n":3,"b":3,"r":5,"q":9,"k":100}
P=[100,-3,-4,-5,-6,-7,-8,-9,0]*2
D={}
for i in range(120):D[i]=0
for r in range(8):
 for f in range(8):D[21+r*10+f]=1
S=[-10,-1,1,10,-11,-9,9,11]
K=[-21,-19,-12,-8,8,12,19,21]
PST={"p":[0]*120,"n":[0]*120,"b":[0]*120,"r":[0]*120,"q":[0]*120,"k":[0]*120}
for i in range(120):
 if not D[i]:continue
 r=i//10-2;fl=i%10-1
 if r<0 or r>7 or fl<0 or fl>7:continue
 PST["p"][i]=r*5 if r<7 else 0
 PST["n"][i]=5 if 2<=r<=5 and 1<=fl<=6 else 0
 PST["b"][i]=3 if abs(r-3.5)+abs(fl-3.5)<4 else 0
 PST["r"][i]=10 if r in(0,7)or fl in(0,7)else 0
 PST["q"][i]=2 if abs(r-3.5)+abs(fl-3.5)<5 else 0
 PST["k"][i]=-10 if r in(0,7)and fl in(0,7)else 0
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
def E(w,a=-9999,b=9999,d=3):
 if d==0:return sum((V[p]+PST[p.lower()][sq]if p.isupper()else-V[p]-PST[p.lower()][sq])for sq in range(21,99)if D[sq]and(p:=M[sq]))
 if w:
  for sq in range(21,99):
   if not D[sq]:continue
   p=M[sq]
   if not p or not p.isupper():continue
   for f,t in G(True):
    U(f,t);s=E(False,a,b,d-1);U(t,f)
    if s>=b:return b
    if s>a:a=s
 else:
  for sq in range(21,99):
   if not D[sq]:continue
   p=M[sq]
   if not p or p.isupper():continue
   for f,t in G(False):
    U(f,t);s=E(True,a,b,d-1);U(t,f)
    if s<=a:return a
    if s<b:b=s
 return a if w else b
M=[0]*120
g=J("/game",b"{}")
while g["status"]!="done":
 while g["status"]=="your_move":
  w=g["colour"]=="w"
  B(g["fen"])
  b=-9999;m=(0,0)
  for f,t in G(w):
   U(f,t);s=E(not w);U(t,f)
   if s>b:b=s;m=(f,t)
  if m==(0,0):break
  f,t=m
  s=f"{chr(97+(f%10-1))}{10-f//10}{chr(97+(t%10-1))}{10-t//10}"
  g=J("/move",json.dumps({"game":g["game"],"move":s}).encode())
  if g["status"]=="over":break
print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=sys.stderr)