try:
  file = open("example.txt", "r")
  content= file.read
except FileNotFoundError:
  print("File not found!")
else:
  print(content)
finally:
  file.close()
  print( "File closed.")