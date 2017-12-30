from fpdf import FPDF
from PIL import Image
import numpy
import glob
import os
import requests

URL_initial = 'http://www.printable-sudoku-puzzles.com/samurai/unsolved.php?d='
URL_final = '&w='

def main():
	def downloadSudoku(level, index):
		sudokuUrl = URL_initial + str(level) + URL_final + str(index)
		r = requests.get(sudokuUrl)
		with open('sudoku'+str(index)+'.png', 'wb') as f:
			for chunk in r:
				f.write(chunk)

	def makePdf(pdfFileName, listImages, dir = ' '):
		nonlocal number
		if (dir):
			dir += "/"

		pdf = FPDF()
		counter = 200
		for image in listImages:
			while counter < number:
				pdf.add_page()
				pdf.image(dir + 'sudoku' + str(counter) + '.png', 13, 30)
				os.remove(dir + 'sudoku' + str(counter) + '.png')
				counter += 1
		pdf.output(dir + pdfFileName + '.pdf', "F")
		print("Thank You for your patience. Your PDF has been saved.")

	print("This program is meant to download Samurai Sudoku puzzles off the internet and combine it into a single PDF.")
	number_input = int(input("How many sudoku puzzles would you like to download? Please enter a number between 1 and 100: "))
	difficulty = input("What level of difficulty would you like your puzzles to be? Please choose a level between 1 to 7 with 1 being the easiest and 7 being the hardest: ")
	number = number_input + 200
	name = input("What would you like to name the PDF file? ")
	print("Please wait while your sudokus get downloaded and saved into one PDF.")
	for i in range(200, number):
		downloadSudoku(difficulty, i)

	imageFolder = '/Users/raaghavgoel/Desktop/GitHub/Sudoku'
	imagePath = glob.glob(imageFolder + '/*.png')
	Image_List = numpy.array( [numpy.array(Image.open(img).convert('L'), 'f') for img in imagePath] )
	makePdf(str(name), Image_List, dir = imageFolder)

	
if __name__ == "__main__":
	main()
