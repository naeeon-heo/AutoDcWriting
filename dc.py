import asyncio
import dc_api
import random
import requests
from faker import Faker
import colorama
from colorama import Fore, Back, Style

def input_user():
 global bid
 global tt
 global ct
 global mr

 bid = input("갤러리 ID : ")
 tt = input("제목 : ")
 ct = input("내용 : ")
 mr = input("마이너 갤 유무 : ")

 if mr == "True":
  return True
 if mr == "False":
  return False

def faker():
 global fake
 fake = Faker('ko-KR')

def request():
 global txt
 global txt2
 res = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt")
 res2 = requests.get("https://raw.githubusercontent.com/HeoNaeEon/AutoDcWriting/refs/heads/main/ip.txt")
 txt = res.text.split("\n")
 txt2 = res2.text.split("\n")

def pp_sort():
 global pp
 pp = []
 i=0
 while i < len(txt)-1:
  nk = txt[i].split(".")
  if str(nk[0])+"."+str(nk[1]) in txt2:
   kk = ".".join(nk)
   pp.append(kk)
  i=i+1
  random.shuffle(pp)

def zz_sort():
 global zz
 zz = []
 z=0
 while z < len(pp):
  nk2 = pp[z].split(":")
  if nk2[1] == "80":
   kk2 = ":".join(nk2)
   zz.append(kk2)
  z=z+1

async def write_document():
 jj=0
 while jj < len(zz):
  try:
   #print(str(jj)+"/"+str(len(zz))+" "+"("+str(zz[jj])+")")
   proxy="http://"+zz[jj]
   api = dc_api.API()
   doc_id = await api.write_document(board_id=bid, title=tt, contents=ct, name=fake.name(), password=fake.password(),pr=proxy,is_minor=mr)
   await api.close()
   if doc_id.headers["Set-Cookie"] != "":
    print(Fore.GREEN+"글쓰기 성공! ip: ("+str(zz[jj])+")"+Style.RESET_ALL)
   jj=jj+1
  except:
   jj=jj+1
   await api.close()

count = 0

while True:
 if count == 0:
  input_user()

 request()

 faker()

 pp_sort()

 zz_sort()

 if count == 0:
  print("")
  print("디시 자동 글쓰기 프로그램 시작 (CTRL + C 를 눌러 종료)")

 asyncio.run(write_document())

 count += 1