INSTRUCTIONS TO USE

1. Install the dependencies by running  `pip install -r requirements.txt`
2. Run the bat file runMe.bat or run the command "streamlit run main.py" in terminal

######################################################


INDEX

1.  main.py is the main python file
2.  Dataset1 is the dataset used to create model1.joblib
3.  Dataset2 is the dataset used to create model2.joblib
4.  trainer.py is python script used to train the models
5.  seedGen.py, goodDataset.py and badDataset.py are python scripts used to create a the datasets


######################################################

How the dataset was created:

seedGen.py is used to a seed data set
The main dataset is picked from the seed dataset
50% of the dataset1 doesn't have any anomaly while other 50% have anomaly
The anomaly distribution of dataset2 follows a binomial distribution. (ie there are 6x more data with 6 amanolies than 1 anomaly)
This is to prevent the model being biased.

