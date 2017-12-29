from fpdf import FPDF
from PIL import Image
import numpy, glob, os, requests

URL = 'http://www.printable-sudoku-puzzles.com/samurai/unsolved.php?d=7&w='

def main():
	def downloadSudoku(index):
		sudokuUrl = URL + str(index)
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
	number = number_input + 200
	name = input("What would you like to name the PDF file? ")
	print("Please wait while your sudokus get downloaded and saved into one PDF.")
	for i in range(200, number):
		downloadSudoku(i)

	imageFolder = '/Users/raaghavgoel/Desktop/GitHub/Sudoku'
	imagePath = glob.glob(imageFolder + '/*.png')
	Image_List = numpy.array( [numpy.array(Image.open(img).convert('L'), 'f') for img in imagePath] )
	makePdf(str(name), Image_List, dir = '/Users/raaghavgoel/Desktop/GitHub/Sudoku/')

	
if __name__ == "__main__":
	main()