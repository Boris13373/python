
with open("file.txt", 'w') as f:
   while True:
      line = input("Введите строку ")
      if not line:
         break
      print(line, file=f)

