path = ["Flashcards/NET3101/CM", "Flashcards/NET3101/TD1"]

import os, random, time

import markdown
from IPython.display import HTML

import cv2

ideal_width, ideal_height = 2000, 1400
screen_width, screen_height = (2560, 1600)
def openThisScreenshot(file) :

	image = cv2.imread(str(file))
	image_width, image_height = image.shape[1], image.shape[0]
	#print(image_width, image_height)

	# Calculate the position to center the image
	x_pos = (screen_width - image_width) // 4
	y_pos = (screen_height - image_height) // 4

	# Create a named window with a specific position

	# Display the image
	cv2.imshow('Centered Image', image)
	cv2.moveWindow('Centered Image', x_pos, y_pos)

	cv2.waitKey(0)
	time.sleep(0.1)
	cv2.destroyAllWindows()
	#print("test")

while True:
	weights = [len(os.listdir(lst)) for lst in path]

	chosen_index = random.choices(range(len(path)), weights=weights)[0]

	chosen_path = path[chosen_index]

	folder = random.choice(os.listdir(chosen_path))
	print(str(folder))
	specificFile = random.choice(os.listdir(chosen_path + "/" + folder))
	if specificFile.lower().endswith(".txt"):
		with open(str(chosen_path + "/" + folder + "/" + folder + "Q.txt"), 'r', encoding='utf-8') as file:
		# Read and print the entire file content
			content = file.read()
			print(content)
			file.close()
			print("\n")
		input()
		with open(str(chosen_path + "/" + folder + "/" + folder + "A.txt"), 'r', encoding='utf-8') as file:
		# Read and print the entire file content
			content = file.read()
			print(content)
			file.close()
		print("\n\n")
	elif specificFile.lower().endswith(".png"):
		openThisScreenshot(str(chosen_path + "/" + folder + "/" + folder + "Q.png"))
		openThisScreenshot(str(chosen_path + "/" + folder + "/" + folder + "A.png"))
	else:
		pass
