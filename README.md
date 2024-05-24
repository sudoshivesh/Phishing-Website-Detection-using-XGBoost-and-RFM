# PHISHING WEBSITE DETECTION USING XGBoost and RFM
### MADE BY GROUP 24AI836 - [Sachin Kumar](https://www.linkedin.com/in/isachin2008/), [Satyam Mishra](https://www.linkedin.com/in/satyam091/), [Shivesh Shivam](https://www.linkedin.com/in/sudoshivesh/)
```
import fourthYearProject
import PhishingWebsiteDetectionUsingXGBoostAndRFM
class 24AI836{
    public static void main(String[] args){
        System.out.println("1. Sachin Kumar [Team Leader]");
        System.out.println("1. Satyam Mishra [Team Member]");
        System.out.println("1. Shivesh Shivam [Team Member]");
    }
}
```

### Why This Project?
Phishing poses a significant cybersecurity threat, causing financial losses and data breaches. Traditional methods are inadequate against sophisticated attacks. This project uses advanced machine learning techniques like XGBoost and Random Forests to automate and improve the detection of phishing websites, enhancing user protection and reducing manual identification errors.

Phishing is a major cybersecurity threat, causing significant financial and data losses. Research indicates that over 48% of emails sent in 2022 were spam, with an estimated 3.4 billion spam emails sent daily. In 2021, 323,972 internet users worldwide fell victim to phishing attacks, with an average loss of $136 per attack, amounting to $44.2 million stolen by cybercriminals. This highlights the urgent need for effective phishing detection methods to protect users and reduce manual identification errors.

<hr/>

### Problem Statement 

Problem Statement:

With the exponential growth of digital communication and online transactions, phishing has emerged as a prevalent cybersecurity threat, endangering individuals and organizations alike. 
The challenge lies in effectively detecting and mitigating phishing attacks to safeguard sensitive information and prevent financial losses. 
Traditional methods often fall short in accurately identifying phishing websites, leading to increased vulnerability and risk. 
Therefore, there is a critical need for advanced machine learning-based solutions capable of rapidly and accurately distinguishing between legitimate and malicious URLs. 
The objective of this project is to develop and deploy a robust phishing website detection system using state-of-the-art machine learning algorithms, such as XGBoost and Random Forest, to enhance cybersecurity resilience and protect users from falling victim to phishing scams.

<hr/>

### Introduction

Introduction:

Phishing poses a significant cybersecurity threat, with malicious actors constantly evolving tactics to deceive users and steal sensitive information. 
Traditional detection methods are often ineffective against sophisticated attacks. 
This project aims to develop an advanced machine learning-based solution to accurately detect and mitigate phishing websites, enhancing online security.

The aim of this project is to develop a robust machine learning-based system for the detection of phishing websites. By leveraging advanced algorithms such as XGBoost and Random Forest, the goal is to accurately classify URLs as legitimate or malicious, thereby enhancing cybersecurity and protecting users from potential threats. 

<hr/>

### Approach

• Collect datasets comprising phishing and legitimate websites from the open-source platform PhishTank.

• Develop code to extract essential features from the URL database.

• Utilize exploratory data analysis (EDA) techniques to analyze and preprocess the dataset.

• Segment the dataset into training and testing sets.

• Implement various machine learning and deep neural network algorithms, including Decision Tree, Random Forest, Multilayer Perceptrons, XGBoost, Autoencoder Neural Networks, and Support Vector Machines.

• Create code to display evaluation results based on accuracy metrics.

• Compare the performance of trained models and determine the superior approach.

<hr/>

### Procedure 

#### 1️⃣ Pre-install all the required libraries
        
       1) Tensoflow
       2) Numpy
       3) Pandas
       4) SciKit-Learn
#### 2️⃣ Understand the dataset
• Datasets containing phishing and legitimate websites is collected from open-source platform PhishTank.
[click here!](https://devmesh.intel.com/projects/driver-drowsiness-detection-70c5e4)

• This service provide a set of phishing URLs in multiple formats like csv, json etc. that gets updated hourly.
  From this dataset, 5000 random phishing URLs are collected to train the machine learning models.

• The legitimate URLs are obatined from the open datasets of the University of New Brunswick, [click here!](https://www.unb.ca/cic/datasets/url-2016.html). 
  This dataset has a collection of benign, spam, phishing, malware & defacement URLs. Out of all these types, the benign url dataset is considered for this project.
  From this dataset, 5000 random legitimate URLs are collected to train the ML models.

#### 3️⃣ Feature Extraction
**The below-mentioned category of features are extracted from the URL data: ​**

1. Addressed Bar-based features​

    • In this category, 9 features are extracted.​

2. Domain-based Features​

    • In this category, 4 features are extracted.​

3. HTML & Javascript-based Features​

    • In this category, 4 features are extracted. ​

So, all together 17 features are extracted from the 10,000 URL dataset and are stored in '5.urldata.csv' file in the Data Files folder​
<img src="https://github.com/gangeshbaskerr/DriverDrowsinessDetection-OneAPI/assets/130077430/28e4ac24-b01c-4c8c-a318-6c2a9b0ebb56">
<img src="https://github.com/gangeshbaskerr/DriverDrowsinessDetection-OneAPI/assets/130077430/8e0171b8-7afc-4b0a-a643-55031fe769a2" width="493" height="480"><img src="https://github.com/gangeshbaskerr/DriverDrowsinessDetection-OneAPI/assets/130077430/80e41fef-9aa9-47ad-b696-956d9f63f126" width="493" height="480">
#### 4️⃣ Build and train the model

Before starting the ML model training, the data is split into 80-20, i.e., 8000 training samples & 2000 testing samples. From the dataset, it is clear that this is a supervised machine-learning task.

This data set comes under a classification problem, as the input URL is classified as phishing (1) or legitimate (0). ​

The supervised machine learning models (classification) considered to train the dataset in this project are:

• Decision Tree

• Random Forest

• Multilayer Perceptrons

• XGBoost

• Autoencoder Neural Network

• Support Vector Machines

<img src="https://github.com/gangeshbaskerr/DriverDrowsinessDetection-OneAPI/assets/130077430/5e0336b8-06e9-4943-b879-445193bd53e0.png" width="470" height="500"><img src="https://github.com/gangeshbaskerr/DriverDrowsinessDetection-OneAPI/assets/130077430/9b8b83b6-f122-482f-96ce-9c3d8eb1a696.png" width="470" height="500">
    
<hr/>

### Tesing and Training accuracy
We did 50 epochs, to get a good accuracy from the XGBoost model i.e. 86.7% for training accuracy and 85.8% for testing accuracy.
<p align="middle"><img src="https://github.com/gangeshbaskerr/DriverDrowsinessDetection-OneAPI/assets/130077430/e4a26e24-a536-4d1c-a9a1-0ec9d8e4e67c.png" width="470" height="300"> 

<hr/>

### Result 

From the obtained results of the above models, XGBoost & RFM Classifier has highest model performance of 86.7%. So the model is saved to the file 'XGBoostClassifier.pickle.dat'

<hr/>
