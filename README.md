# Download-Sudoku

This program downloads Samurai Sudoku puzzles off the internet using a web scraper and outputs a single, easy-to-print PDF file.

The process followed is as such - 
  1. The program uses input prompts to ask the user the number of puzzles they wish to download, and the name of the PDF file.
  2. The program then scrapes the web and downloads the desired number of random Samurai Sudoku puzzles as PNG files into the folder containing the program.
  3. The PNG files are added to a NumPy Array and are then fed into a makePDF function.
  4. The function adds each PNG file to a single PDF document and then immediately deletes the PNG file that has been added.
  5. Therefore, the output is a simple PDF file instead of multiple PNG files, which makes the folder less cluttered and makes it easier to print out the document. 


How to use:
  1. Download the .py file and save it in your desired folder. **Remember, the PDF file will be downloaded in this folder itself.** 
  2. Edit the code. In Line 43, change the path name, imageFolder, to indicate the folder in which the code is saved.
  3. Run the code. 
  4. Navigate to the folder where the code is saved, find the compiled PDF, which is ready for printing and happy solving! :)
