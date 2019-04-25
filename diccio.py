import os
reset="\033[0;37m"

def bann():
 print ("***** ******  **  ** **  ** ** ***   ** ******")
 print ("**    **  **  **  ** ** **  ** ****  ** **  **")
 print ("****  *****   **  ** ****   ** ** ** ** **  **")
 print ("**    **  **  **  ** ** **  ** **  **** **  **")
 print ("***** **   ** ****** **  ** ** **   *** ******")
 print ("______________________________________________")
 print ("____________Diccionario Numerico______________")
 print ("_____________Creado por Erukino_______________")
 print ("_____________Telegram @3rukin0x_______________")
 print ("______________________________________________")


def adios():
    os.system("clear")
    bann()
    print ("")
    print ("ADIOS")
    str(input("Presione enter para salir"))
    os.system("clear")
    exit()

def menu():
  os.system("clear")
  bann()
  print (reset)
  print ("")
  print ("1- Crear un diccionario numerico")
  print ("2- Salir\n")
  while True:
   try:
     rta = int(input('Opcion deseada: \n'))
     break
   except:
     print ("¡¡¡Ops entrada erronea!!!")
  if rta == 1:
    inicio_num()
  elif rta == 2:
    adios()
  else:
    menu()

def inicio_num():
  os.system("clear")
  bann()
  print ("----------------------------------")
  print (" Iniciando creacion de ciccionario")
  print ("     gracias por tu espera")
  print ("------------–---------------------")
  print ("")
  print ("")
  print ("1 Cantidad de digotos")
  print ("2 Cantidad especifica")
  print ("3 De ---> hasta ")
  print ("4 Salir")
  while True:
   try:
     rt = int(input("Opcion desea:  "))
     break
   except:
     print ("Ops opcion invalida")
     inicio_num()
  if rt == 1:
    os.system("clear")
    digit()
  elif rt == 2:
    os.system("clear")
    cantid()
  elif rt == 3:
    os.system("clear")
    dicci()
  elif rt == 4:
    adios()

def dicci():
  bann()
  nomb = str(input('Nombre de el diccionario:\n'))
  while True:
   try:
     x =int(input('Porfavor ingrese el numero inicial: \n'))
     break
   except:
     print ("Ops entrada erronea")
  while True:
   try:
     fin = int(input('Porfavor ingrese el numero limite:\n'))
     break
   except:
     print ("Ops entrada erronea")
  y =len(str(fin))
  dicc= open(nomb+".txt","w")
  os.system("clear")
  bann()
  print ("Creando diccionario porfavor espere\n")
  print ("podria tardar un tiempo ...\n")
  for x in range(fin+1):
      f=str(x)
      d=f.zfill(y)
      dicc.writelines(str(d)+"\n")
  print ("Finalizo corrextamente")
  adios()

def digit():
  bann()
  nomb = str(input('Nombre de el diccionario:\n'))
  while True:
   try:
     x = int(input('Ingrese la cantidad de digitos que deseas:\n'))
     break
   except:
     print ("Ops entrada invalida")
  y ='9'
  a = 0
  z = y*x
  dicc= open(nomb+".txt","w")
  os.system("clear")
  bann()
  print ("Creando diccionario porfavor espere\n")
  print ("podria tardar un poco ...\n")
  for a in range(int(z)+1):
    b=str(a)
    c=b.zfill(x)
    dicc.writelines(str(c)+'\n')
  print ("Finalizo correctamente")
  adios()

def cantid():
  bann()
  nomb=str(input("Ingrese nombre de diccionario:\n"))
  while True:
   try:
    x=int(input("Ingrese cantidad limite:\n"))
    break
   except:
    print ("Ops entrada invalida")
  a=0
  dicc=open(nomb+".txt","w")
  os.system("clear")
  bann()
  print ("Creando diccionario podria tardar\n")
  print ("un poco porfavor espere\n")
  for a in range(x+1):
     b=len(str(x))
     c=str(a)
     d=c.zfill(b)
     dicc.writelines(str(d)+"\n")
  adios()

menu()
