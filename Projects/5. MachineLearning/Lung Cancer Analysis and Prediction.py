#!/usr/bin/env python
# coding: utf-8

# # <center> <h1> Lung Cancer Analysis and Prediction  </h1> </center>

# # ![Lung-Cancer-1.jpg](attachment:Lung-Cancer-1.jpg)

# ## About Dataset
# <i> I have download this dataset from kaggle. The data is collected from the website online lung cancer prediction system and get a feedback from the user. This site has implemented during period of August 2013 the people who visited this site. </i>
#  
# - <b>Columns</b>  &emsp;	&emsp;&emsp;&emsp;&emsp; &emsp;:16
# - <b>Rows</b> &emsp;   &emsp;&emsp;&emsp; &emsp; &emsp;&nbsp;&emsp;:309
# - <b>Gender</b>    &emsp;&emsp;&emsp;  &emsp;&emsp;&emsp;&emsp;: M(male), F(female)
# - <b>Age</b>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;: Age of the patient
# - <b>Smoking</b>&emsp;&emsp;&emsp;   &emsp;&emsp;&emsp; &nbsp;: YES=1 , NO=0.
# - <b>Yellow fingers</b>&emsp;&emsp;&emsp;&emsp;: YES=1 , NO=0.
# - <b>Anxiety</b>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp; &nbsp; : YES=1 , NO=0.
# - <b>Peer_pressure</b>&nbsp; &nbsp; &nbsp;  &nbsp;  &nbsp;  &nbsp;   &nbsp;: YES=1 , NO=0.
# - <b>Chronic Disease</b>  &nbsp;&nbsp;  &nbsp;  &nbsp;  &nbsp;   &nbsp;: YES=1 , NO=0.
# - <b>Fatigue</b>  &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: YES=1 , NO=0.
# - <b>Allergy</b>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; : YES=1 , NO=0.
# - <b>Wheezing</b> &nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: YES=1 , NO=0.
# - <b>Alcohol</b> &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;: YES=1 , NO=0.
# - <b>Coughing</b> &nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: YES=1 , NO=0.
# - <b>Shortness of Breath  </b> &nbsp; &nbsp;&nbsp;: YES=1 , NO=0.
# - <b>Swallowing Difficulty </b>&nbsp;&nbsp;: YES=1 , NO=0.
# - <b>Chest pain</b> &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: YES=1 , NO=0.
# - <b>Lung Cancer</b> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: YES , NO. 

# ## Import Libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Loading Dataset

# In[2]:


d=pd.read_csv("H:\Courses\EXL_DataAnalytics_Course\DataSets\LungCancer\LungCancerPrediction.csv")


# In[3]:


d


# ### Displaying Top 5 and Bottom 5 Rows 

# In[4]:


d.head()


# In[5]:


d.tail()


# ### Check for null values 

# In[6]:


d.isnull().sum()


# ### Displaying Columns Names 

# In[7]:


d.columns


# - <i> In the above listed column names, we can see there is an extra space in the column name <b>'FATIGUE '</b> and <b> 'ALLERGY '</b>. So we are going to use rename function to eliminate the extra space. </i>

# In[8]:


new_name={'FATIGUE ':'FATIGUE',
            'ALLERGY ':'ALLERGY'}
d.rename(columns=new_name,inplace=True)


# ### Name of the Columns after Renaming

# In[9]:


d.columns


# ### Null Value and Data Types Information 

# In[10]:


d.info()


# ### Descriptive Statistical Information 

# In[11]:


d.describe()


# ###  Correlation and Covariance between the Variables

# In[12]:


d.corr()


# In[13]:


d.cov()


# ## Analysing the Dataset

# In[14]:


df=d.groupby("GENDER")["GENDER"].count()
df.plot.pie(autopct="%.1f%%",colors=["greenyellow","magenta"])
plt.show()


# In[15]:


print(pd.pivot_table(data=d,values='AGE',index='GENDER',columns='SMOKING',aggfunc='count'))

sns.countplot(x="SMOKING", data=d,palette="rocket")
plt.show()


# In[16]:


print(pd.pivot_table(data=d,values='AGE',index='GENDER',columns='YELLOW_FINGERS',aggfunc='count'))

sns.countplot(x="YELLOW_FINGERS", data=d,palette="mako")
plt.show()


# In[17]:


print(pd.pivot_table(data=d,values='AGE',index='GENDER',columns='ANXIETY',aggfunc='count'))

sns.countplot(x="ANXIETY", data=d,palette="Set3")
plt.show()


# In[18]:


print(pd.pivot_table(data=d,values='AGE',index='GENDER',columns='PEER_PRESSURE',aggfunc='count'))

sns.countplot(x="PEER_PRESSURE", data=d,palette="viridis")
plt.show()


# In[19]:


print(pd.pivot_table(data=d,values='AGE',index='GENDER',columns='CHRONIC DISEASE',aggfunc='count'))

sns.countplot(x="CHRONIC DISEASE", data=d,palette="cubehelix")
plt.show()


# In[20]:


print(pd.pivot_table(data=d, values='AGE', index='GENDER', columns='FATIGUE',aggfunc='count'))


sns.countplot(x="FATIGUE",data=d,palette="Spectral")
plt.show()


# In[21]:


print(pd.DataFrame(pd.pivot_table(data=d,values='AGE',index='GENDER',columns='ALLERGY',aggfunc='count')))

sns.countplot(x="ALLERGY",data=d,palette="coolwarm")
plt.show()


# In[22]:


print(pd.pivot_table(data=d,values='AGE',index='GENDER',columns='ALCOHOL CONSUMING',aggfunc='count'))

sns.countplot(x="ALCOHOL CONSUMING",data=d,palette="Set3")
plt.show()


# In[23]:


print(pd.pivot_table(data=d,values='AGE',index='GENDER',columns='COUGHING',aggfunc='count'))

sns.countplot(x="COUGHING",data=d,palette="dark")
plt.show()


# In[24]:


print(pd.pivot_table(data=d,values='AGE',index='GENDER',columns='SHORTNESS OF BREATH',aggfunc='count'))

sns.countplot(x="SHORTNESS OF BREATH",data=d,palette="magma")
plt.show()


# In[25]:


print(pd.pivot_table(data=d,values='AGE',index='GENDER',columns='SWALLOWING DIFFICULTY',aggfunc='count'))

sns.countplot(x="SWALLOWING DIFFICULTY",data=d,palette="crest")
plt.show()


# In[26]:


pd.pivot_table(data=d,values='AGE',index='GENDER',columns='CHEST PAIN',aggfunc='count')

sns.countplot(x="CHEST PAIN",data=d,palette="Set2")
plt.show()


# In[27]:


df=d.groupby("LUNG_CANCER")["LUNG_CANCER"].count()
df.plot.pie(autopct="%.1f%%",colors=["greenyellow","yellow"])
plt.show()


# ## Heatmap to find the correlation between all variables

# In[28]:


result=d.corr()
fig = plt.figure(num=None, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')

sns.heatmap(result, annot=True, annot_kws={"size": 10},fmt='.3f')
plt.show()


# ## Analysis Conclusion 

# 1. Anxitey is highly correlated with yellow fingers and swallowing difficulty. Fatigue is highly correlated with shortness of breath. <br>
# 2. In this survey more than 50% male members were participated that's why more male mebers prediction is possitive.<br>
# 3. The participated members having the habbits of smoking, alcohol consuming and facing issues like allergy,cough,shortness of breath,chest pain,yellow fingers and fatigue.<br>
# 4. 87.4% of people were affected by lung cancer.<br>

# # <center> <h1> Machine Learning </h1> </center>

# ## Converting Gender to Numbers 
# 
# - Since machine learning algorithms does not support string I am converting the gender columns into binary format as follows:
#      - Male&nbsp; &nbsp;&nbsp;:&nbsp;1
#      - Female&nbsp;:&nbsp;0

# In[29]:


d['GENDER'][d['GENDER']== "M"] = 1
d['GENDER'][d['GENDER']== "F"] = 0


# ## Selecting X and Y variables 

# In[30]:


from sklearn.model_selection import train_test_split


# In[31]:


X, y = d.iloc[:,:-1], d.iloc[:, -1]


# ## Splitting the Dataset into train and test 

# In[32]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50, random_state=1)


# In[33]:


print('X_train: ' + str(X_train.shape))
print('Y_train: ' + str(y_train.shape))
print('X_test:  ' + str( X_test.shape))
print('Y_test:  ' + str( y_test.shape))


# ## Train the Model using Data Samples

# #### Now I am going to train my model by using three differenct classificatin algorithms such as KNN, Naive Bayes and Decision Tree

# In[34]:


from sklearn import metrics


# ### Train using K-Nearest Neighbors. 

# In[35]:


from sklearn.neighbors import KNeighborsClassifier


# In[36]:


knn_classifier=KNeighborsClassifier(n_neighbors=2)


# In[37]:


knn_classifier.fit(X_train ,y_train)


# ### Train using Naive Bayes

# In[38]:


from sklearn.naive_bayes import GaussianNB


# In[39]:


gnb = GaussianNB()


# In[40]:


gnb.fit(X_train, y_train)


# ### Train using Decision Tree 

# In[41]:


from sklearn.tree import DecisionTreeClassifier 


# In[42]:


classifier= DecisionTreeClassifier(criterion='entropy', random_state=0)  


# In[43]:


classifier.fit(X_train, y_train) 


# ## Testing the model

# ###  K-Nearest Neighbors.

# In[44]:


prediction=knn_classifier.predict(X_test)


# In[45]:


print("Accuracy:",knn_classifier.score(X_test,y_test))


# ### Naive bayes algorithm 

# In[46]:


y_pred=gnb.predict(X_test)


# In[47]:


print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


# ### Decision Tree Algorithm

# In[48]:


y_pred= classifier.predict(X_test)  


# In[49]:


print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


# # <center> <h1> Dashboard Using Subplots </h1> </center>

# In[50]:


plt.figure(figsize=(35,20))
plt.subplot(4,4,1)
df=d.groupby("GENDER")["GENDER"].count()
df.plot.pie(autopct="%.1f%%",colors=["greenyellow","magenta"])

plt.subplot(4,4,2)
sns.countplot(x="SMOKING", data=d,hue="GENDER",palette="rocket")
plt.xlabel('Smoking')

plt.subplot(4,4,3)
sns.countplot(x="YELLOW_FINGERS", data=d,hue="GENDER",palette="mako")
plt.xlabel('Yellow Fingers')

plt.subplot(4,4,4)
sns.countplot(x="ANXIETY", data=d,hue="GENDER",palette="Set3")
plt.xlabel('Anxiety')

plt.subplot(4,4,5)
sns.countplot(x="PEER_PRESSURE", data=d,hue="GENDER",palette="viridis")
plt.xlabel('Peer Pressure')

plt.subplot(4,4,6)
sns.countplot(x="CHRONIC DISEASE", data=d,hue="GENDER",palette="cubehelix")
plt.xlabel('Chronic Disease')

plt.subplot(4,4,7)
sns.countplot(x="FATIGUE",data=d,hue="GENDER",palette="Spectral")
plt.xlabel('Fatigue')

plt.subplot(4,4,8)
sns.countplot(x="ALLERGY",data=d,hue="GENDER",palette="coolwarm")
plt.xlabel('Allergy')

plt.subplot(4,4,9)
sns.countplot(x="ALCOHOL CONSUMING",data=d,hue="GENDER",palette="Set3")
plt.xlabel('Alcohol Consuming')

plt.subplot(4,4,10)
sns.countplot(x="COUGHING",data=d,hue="GENDER",palette="dark")
plt.xlabel('Coughing')

plt.subplot(4,4,11)
sns.countplot(x="SHORTNESS OF BREATH",data=d,hue="GENDER",palette="magma")
plt.xlabel('Shortness of breath')

plt.subplot(4,4,12)
sns.countplot(x="SWALLOWING DIFFICULTY",data=d,hue="GENDER",palette="crest")
plt.xlabel('Swallowing difficulty')

plt.subplot(4,4,13)
sns.countplot(x="CHEST PAIN",data=d,hue="GENDER",palette="Set2")
plt.xlabel('Chest Pain')

plt.subplot(4,4,14)
plt.hist(d['AGE'])
plt.xlabel('Age')

plt.subplot(4,4,15)
df=d.groupby("LUNG_CANCER")["LUNG_CANCER"].count()
df.plot.pie(autopct="%.1f%%",colors=["greenyellow","yellow"])

plt.subplot(4,4,16)
sns.countplot(x="LUNG_CANCER",data=d,hue="GENDER",palette="coolwarm")
plt.show()


# # Thank You!
