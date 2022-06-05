# Overview

I essentially wanted to create a Google Drive look alike using the Google Storage API and log each of the action taken on it
on the Firebase database. 

[Software Demo Video](https://youtu.be/vwhZ0GuH-04)

# Cloud Database

I don't know how to adequately describe the structure but basically the app allows for file uploads, download and deletes to the 
storage API. The Firebase database has one collection and the document on it will be filled with logs of what has been happening with 
the storage, or in other words how it's being used. 

# Development Environment

I used Visual Studio Code, Pyrebase4 (library), Firebase_admin (library), and os (library)

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Google Cloud](https://cloud.google.com)
* [Pyrebase Tutorial for Python](https://www.youtube.com/watch?v=s-Ga8c3toVY&t=1810s)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Fix authentication for app so that the DB can work
* Improve documentation style in Database
* Make a cooler GUI. 