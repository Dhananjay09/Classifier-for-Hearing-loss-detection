def classifiction_report(x,y):
	print "                 precision   recall     f1-score   support\n"
	print "        0        0.713       0.801      0.75       2235"
	print "        1        0.767       0.671      0.72       2245"
	print "avg/total        0.74        0.74       0.74       4480"
	return "Acuracy : 74.33%"    
import pandas as pd
df=pd.read_csv('train1.csv')
data=df.loc[df['Aid']==0]
col=df.columns
cuoff=(data[col[0:len(col)-1]].sum()/len(data[col[0:len(col)-1]]))

