

import pandas as pd
import zipfile
import os


with zipfile.ZipFile(R"C:\Users\Lenovo\Downloads\Healthcare.zip", 'r') as zip_ref:
    zip_ref.extractall('.')


df = pd.read_csv("kidney_disease_dataset.csv")
df.head()


x=df.drop(columns="Dialysis_Needed")
y=df["Dialysis_Needed"]



from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=10)
print(x_train)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)



y_train_pred=model.predict(x_train)
y_test_pred=model.predict(x_test)
y_train_pred



from sklearn.metrics import accuracy_score,confusion_matrix
acc=accuracy_score(y_train,y_train_pred)
acc2=accuracy_score(y_test,y_test_pred)
print(acc)
print(acc2)
cm=confusion_matrix(y_train,y_train_pred)
cm2=confusion_matrix(y_test,y_test_pred)
print(cm)
print(cm2)
trial=model.predict([[34,0.3,5,1,1,30.4,1723,1]])
if trial==0:
    print("Dialysis not needed")
else:
    print("Dialysis needed")