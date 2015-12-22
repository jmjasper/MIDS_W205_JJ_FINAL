# Introduction

Sentiment is an important part of marketing efforts and strategic decision making. Real-time sentiment is becoming increasingly important in damage mitigation plans for firms.

In this project, I've developed and deployed a real-time system to measure the sentiment of incoming tweets and score them. This data can then be displayed and analyzed for it's marketing value and campaign effectiveness measures.

###Architecture

This architecture is a simple but extensible Storm information processing system with an associated Postgres database. Information analysis is done by a Tableau database.

The architecture is specifically designed to be flexible and extensible as the needs of consumers will develop as time goes on and they will want more sophiticated analysis of general twitter sentiment.

###Purpose

The purpose of this project is to explore real-time sentiment analysis and develop a system capable of dealing with streaming text data in real time. A solution should be general enough to implement for any problem, yet provide a relatively accurate picture of user sentiment.

###Setup

To run the program, you'll need to do the following:

1. Start an m3.xlarge EC2 instance with the Berkeley AMI with P2.7 and an assocaited EBS of 30 GB.

2. Access the machine and note the location of the drive with lsblk.

3. Get the easy setup script with: wget https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh

4. Run the script with bash setup_ucb_complete_plus_postgres.sh [path_to_mounted_drive]

5. We now need to get sparse installed with all it's dependencies.

6. Start by upgrading python with sudo yum install python27-devel –y

7. Then change the running version then mv /usr/bin/python /usr/bin/python266, then link with ln -s /usr/bin/python2.7 /usr/bin/python

8. Install with sudo curl -o ez_setup.py https://bootstrap.pypa.io/ez_setup.py

9.Then sudo python ez_setup.py

10. Finally install pip with: sudo /usr/bin/easy_install-2.7 pip

11. Install virtualenv with sudo pip install virtualenv

12. Install lein with wget --directory-prefix=/usr/bin/ https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein

13. Change the accessibility on the file with: chmod a+x /usr/bin/lein

14. Now install streamparse: pip install streamparse

15. We need to install two python packages: tweepy and psycopg2. You can do this with pip install tweepy and pip install psycopg2.

16. Connect to the postgres server with psql -U postgres.

17. Create the database Tcount with: CREATE DATABASE sent;

18. In the db folder of the applicaiton, there's a make table script -- this will make the necessary table. Run it with python maketable.py.

16. You should be good to go! Change directory to tweetwordcount and use sparse run to start. Note: I've turned off all external outputs and limited the incoming tweets to ones about Disney to limit the $

###Additional Components

Two new components that will need to be installed are the NLTK python package and the vaderSentiment package.

These can be installed with pip install nltk and pip install vaderSentiment.

However, once installed, you need to downloard the dictionaries for nltk. You can do this by opening an interpreted python session with python.

Once in the session, import the library with: import nltk.

Then access the downloader with nltk.download(). This will bring up a bunch of options. You can download the entire corpus with d all.

This still will take a bit.


###Final Thoughts

This project was very successful when presented to Disney and they are asking for a framework that provides a similar service for facebook posts. As a result, work on this project will continue.
