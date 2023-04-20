# MANU-465-EEG4

Repository for MANU 465 Capstone Project - Group #9

## Project Description

<p>The goal of this project was to be able to accurately predict if a person was using their dominant
or non-dominant hand from EEG data. Participants were fitted with the Muse 2 device and
asked to perform the same writing task with both hands sequentially. EEG data was recorded
from the Muse2 (“Muse 2”) sensor using a third-party application, Mind Monitor (“Mind Monitor”).</p>

<p>Participants performed 4 tasks in total and a .csv file for each task was recorded. Additional
information including Task ID, Participant ID, gender and if english was their first language was
added to each .csv file. Over 90 participants generated more than 360 csv files of various
lengths. Evident from the collected writing samples, some participants had a more significant
hand dominance which was demonstrated by the differences in both time to complete the writing
sample, and quality of penmanship with the non-dominant hand. For the purpose of this study,
participants self-identified as right or left handed and no ranking or gradient was applied.</p>

## Data Collection

The experiment consisted of subjects completing a complex and simple test using their
dominant and non dominant hands. For these tests, subjects were asked to reprint a provided
sentence, requiring some level of care, and scribble in a circle for 10 seconds, a much simpler task. We also recorded each subject’s gender, dominant hand, and whether english was their first language in the event that these parameters had an impact on our results. The testing of each subject took roughly five minutes to complete, including time for COVID-19 screening, cleaning the Muse 2 headset, and adding the additional features to each csv file. In total, roughly 90 participants were tested, totaling 365 unique csv files.

## Results

<p>The results of the experiment were mixed.  The accuracy of each model was determined using accuracy_score from the SKlearn.metrics library. The accuracy of each machine learning classifier is summarized in Table 6 below:</p>

| Classifier | Accuracy |
|------------|----------|
| KNN        | 59.68 %     |
| SVM        | 77.42 %    |
| SVM Non-Linear | 80.65 %    |
| Random Forest | 74.19 %    |
| Decision Tree | 75.81 %    |
| Naive Bayes | 72.58 %    |
| Logistic Regression | 72.58 %    |
| ANN | 69.35 %    |

<p>From the results above, the classifier with the highest accuracy was the Non-Linear Support
Vector Machine model with an accuracy of 80.65%. In general, all models performed decently
well and we are satisfied with the outcome of the SVM Non-Linear classifier. However, further work may be conducted that could possibly increase the accuracy of our model.</p>

## Future Work

<p>The nature of our experiment requires a large dataset to make a machine learning model with a
high accuracy. Future work on this project can include increasing the volume of data by
conducting more tests on individuals. However, we already collected four samples from nearly
100 subjects and reached the limit on the amount of data we could collect for the scope of this
project.</p>

<p>In our preliminary literature review, we also reviewed a study by M.Z Baig et al. (Baig #) that
implemented a Single-Organized-Map (SOM) algorithm. This article used a pre-existing dataset
that required more advanced components to collect data than the MUSE headset we are
provided. The SOM based algorithm is an advanced unsupervised model that does not exist
with the pre-existing Python tools we have learned in class and achieved an 84.17%
classification accuracy according to the study, which is similar to the results that we achieved.
However, it would still be worthwhile in the future to build this classifier with our dataset and
compare its accuracy with the results of the SVM Non-Linear model.</p>


