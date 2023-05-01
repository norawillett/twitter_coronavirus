# Coronavirus twitter analysis

## Project Overview

The aim of this project is to summarize tweets that mentioned coronavirus in various languages and other related words in the year 2020. The dataset used for my analysis comes from the lambda server’s /data/Twitter dataset folder and contains roughly 1.1 billion tweets. One interesting quality of this data set is that some of the tweets are geotagged, meaning they contain the location information from where the tweet was sent. My analysis incorporates this geotagged location to grasp where these tweets are sent from. Furthermore, my analysis looks at tweets in other languages, including Korean, Japanese, and Chinese. 

## Background

**Process**

This project required using shell scripts, navigating the lambda server, as well as learning and implementing libraries for visualizing data. To parse through all 1.1 billion tweets, I followed the MapReduce procedure and uses parallel processing. To parse through all of the files in the dataset, I used my map.py file, which kept track of the hashtags as well as the language and country code for each file. To put all of this information into two simplified files (one file for the languages and the other for the country code), my reduce.py file merged all of the outputs into a dictionary. I could then use these two files to graph and visualize the output. The shell script can be found in my run_maps.sh file. 

## Findings

I have included 4 graphs to show my findings from the project. The first image shows the top ten languages #coronavirus was mentioned, and my second image shows the top 10 languages #코로나바이러스 (this is #coronavirus in Korean) was mentioned. My graphs show that English and Spanish were the top 2 languages #coronavirus was tweeted in, and Korean was by far the top language #코로나바이러스 was tweeted in. My third and fourth images show the top ten countries #coronavirus and #코로나바이러스 were mentioned in. #coronavirus was mentioned most in the United States, India, and Great Britain. #코로나바이러스 was tweeted the most by South Korea. 


**Figure 1: #Coronavirus in English by Language**

<img src=figure1.png width=400px/>

**Figure 2:# 코로나바이러스 by Language**

<img src=figure2.png width=400px/>


**Figure 3: #Coronavirus in English by Country**

<img src=figure3.png width=400px/>

**Figure 4:# 코로나바이러스 by Country**

<img src=figure4.png width=400px/>


## Analysis Over Time

To look at tweets over the course of 2020, I used my alternative_reduce file. This took in multiple hashtags as input and creates a plot with the number of tweets sent in 2020 that mention those tweets (with the date on the x-axis). This is a helpful graphical tool to see the number of tweets that change over the course of 2020 relative to other hashtags. I looked at #coronavirus and #corona and found that they followed a similar trend (coronavirus_corona.png). My graph showed that #corona was used more than #coronavirus, which I found surprising. Other graphs can be used by changing the input (—keys). I compared the syntax of #covid19 vs. #covid-19 and found that #covid19 was far more popular than #covid-19. I also found that #coronavirus was tweeted more at the start of the pandemic, then #covid19 became more popular towards the end.

**Figure 5: #Coronavirus vs. #Corona**

<img src=coronavirus_corona.png width=400px/>


**Figure 6: #Covid-19 vs. #Covid19**

<img src=covid-19_covid19.png width=400px/>


**Figure 7: #Coronavirus vs. #Covid19**

<img src=coronavirus_covid19.png width=400px/>



## Conclusion


Overall, this project utilized the power of glob to go through hundreds of files, as well as tools to run programs in the background (even when I am not on my computer). I learned how to utilize the matplotlib library and manipulate inputs and datasets to better understand data. Surprisingly, the biggest challenge I faced in this project was manipulating my graphs. Before completing this project, I imagined that going through all 1.1 billion tweets would be the most difficult part! Going forward, I hope to learn more about visualization methods and how to show data in new, unique forms. 



