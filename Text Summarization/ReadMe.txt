To run the program, open Terminal inside folder and type

python lexrank.py

and some output would be displayed. These are the summaries generated for files reut1.txt, 096.txt, reut.txt, 018.txt

To obtain summaries for a custom file in the articles folder :

1) Open file lexrank.py
2) Scroll to the end of the file
3) Modify the fileNames array - add the custom file's file name to the end of the array
4) Save the file
5) Run the file as above

Similarly, the size of summaries can be changed. The default is 41% of the document size which is set by assigning 0 to the variable summarySize. To obtain summaries of fixed lengths, assign a value other than 0. For e.g. - assigning the value 10 will generate a summary of 10 sentences.