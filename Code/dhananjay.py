from csv import writer
from dj import classifiction_report
import os
import random
li=['Aid']

'''entries = os.listdir('/home/dhananjay/Desktop/Learing/smni_eeg_data/a_1_co2a0000364')
entries.remove('dhananjay.py')
entries.remove('train.csv')
for p in entries:
	file=open(p,'r').readlines()
	pkjj=[]
	for v in file:
		p=v.split()
		pkjj.append([p[1],p[-1]])
	for i in range(0,5):
		pkjj.pop(0)
	x=[]
	head=[]
	for i in range(0,256):
		y=[]
		head=[]
		for j in range(0,64):
			y.append(pkjj[i+j*256][1])
		x.append(y)
	with open('train.csv', 'a+') as write_obj:
		csv_writer = writer(write_obj)
		for y in x:
			csv_writer.writerow(y)'''
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
dhananjay=pd.read_csv('train1.csv')
print ("Calculation is being Done please Wait......")
temp=dhananjay
Y=dhananjay['Aid']
X=dhananjay.iloc[:,0:63]
x_train,x_test,y_train,y_test=train_test_split(X,Y)
pkjj=LogisticRegression().fit(x_train,y_train)
y_pred = pkjj.predict(x_test)
print classifiction_report(y_test, y_pred)
df=pd.read_csv('train1.csv')
data=df.loc[df['Aid']==0]
col=df.columns
cutoff=(data[col[0:len(col)-1]].sum()/len(data[col[0:len(col)-1]]))
for i in range(0,100):
	temp=(random.randint(1,len(x_test)))
	input=(x_test.iloc[temp])
	gradient=[]
	testing_value=[]
	for i in range(0,len(cutoff)):
		gradient.append(cutoff[-1])
	for i in range(0,len(input)):
	        testing_value.append(input.iloc[i])
	difference=[]
	for i in range(len(testing_value)):
		difference.append(abs(testing_value[i]-gradient[i]))
	count=0
	for i in range(len(difference)):
		if(difference[i]>2):
			count+=1
	if(52>count):
		print ("Person does not have Hearig-Aid")
	else:
		print ("Person is suffering from Hearing-Aid and Need a turing of \n",difference)

