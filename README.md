# Authorship Attribution Program
Project developed for Computer Science course and improved upon for Machine Learning presentations

To start the program, run ProjectGUI.py, and the interface will pop up. Across the top, there is a place to type in files, as well as to add the author, genre, and year for those files. The options for genre are short story, fiction, science fiction, horror, poem, or other. Press “Add Document” when you have typed everything in. You can add as many documents as you would like before applying filters and building trees. 

To apply filters, you must first select what filters you want to apply. Click on the button for each filter that you want to apply, one by one. After you have clicked on each filter that you want to use, press “APPLY FILTERS”, and every filter that you have clicked will be applied to all of the documents that you read in.
	
For training, you must first click on one of the nine training methods. Then, click train, and it will train based off of the most recently clicked method using all of the files that are listed at the bottom. Similarly, predict will make a prediction based off of the most recently clicked on method. That method must’ve been trained in order for a prediction to be made. Type in the file that you want to predict, above the prediction button.. The year and the genre are optional if you are not predicting based off a tree that was built using year or genre. All 9 of the methods will print out the prediction in the python shell, as well as add the document and predicted author to the list of documents in the bottom. Additionally, SKPCA will pop-up with a scatter plot with the trained files in blue and the predicted file in red, so that you can see the distance it is from other files.

Also includes sample text files for training and predictions.

