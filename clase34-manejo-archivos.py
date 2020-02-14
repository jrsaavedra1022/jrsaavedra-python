# -*- coding: utf-8 -*-

def write_file():
	with open("Files-class/file.txt", "w") as f:
		for i in range(10):
			f.write(str(i))

def read_file():
	counter = 0
	with open("Files-class/aleph.txt", "r", encoding="utf-8") as f:
		for line in f:
			counter += line.count('Beatriz')

	print('Beatriz have been to found  {} in the text'.format(counter))		

if __name__ == '__main__':
	write_file()
	read_file()

print("Manejo de archivos")


# with open("Files-class/file.txt", "w") as f:
# 	for i in range(5):
# 		print("Hello") 
