# 2019-mini-s28

# Project Summary
EC463 Weather Application by Donavan Jones and Justin Morgan

Welcome to our EC463 Software mini project! Upon first navigation to the web app, please answer 'allow' when prompted for your current location. Otherwise the weather functionality will default to getting the weather from somewhere else. Single sign on with a Google account in order to view the user's Google profile picture, email, as well as the Cloud SQL DB data being pulled in to form a javascript graph on the right side of the browser. This data is sitting in the Google Cloud SQL Database for the project, but which rows in the table are taken is decided by randomly generated integers upon loading the page. The data points displayed are for theoretical 'rooms' that the temperature and humidity sensors are in. Hit 'Go' underneath the 'Weather at my Current Location' header in order to view the current forecast and temperature in degrees Celcius (Weather data pulled via the Open Weather Map API). Hit the back button on the web browser in order to navigate to the previous screen, and 'Sign out' to sign out of the Google Account.

# App URL (Cloud Deployment)
https://bookshelfproject-252519.appspot.com

# Video Demonstration (In case the Google Cloud deployment shuts down due to insufficient funds)
Click the image below for the video demo!
<br />
[![Here's the link to my video](https://img.youtube.com/vi/yrRp5hI1XUU/0.jpg)](https://www.youtube.com/watch?v=yrRp5hI1XUU "EC463 Mini Project Demo")

# Sources Used
Weather API used: https://openweathermap.org (Open Weather Map)

HTML5 Geolocation example used for reference: https://www.w3schools.com/html/html5_geolocation.asp

Weather icons used from the following repo: https://erikflowers.github.io/weather-icons/ (Licensed under SIL Open Font License (OFL)) (Open source)

# Tutorials Referenced
Python, Flask, Google Cloud, Open Weather Map Tutorial: https://www.freecodecamp.org/news/how-to-build-a-web-app-using-pythons-flask-and-google-app-engine-52b1bb82b221/

Google Cloud Hello World: https://cloud.google.com/python/getting-started/hello-world

Google Cloud Python Bookshelf App (SQL): https://cloud.google.com/python/getting-started/tutorial-app

# Project Timeline (Ongoing and Subject to Change)
Wednesday 9/11: Get the repo up and running with a basic template. Division of work and code management. Work on Single Sign on, pulling from SQL DB, have ‘app’ testable via localhost (gcloud).

Thursday 9/12: Meet up after sr design, check in regarding project work, review project requirements. Finalize division of work and code management (branching, etc.) Agile sprints? Weather API? Review timeline.

Friday 9/13: Continue respective project parts.

Saturday 9/14: Work day. Finish SSO, geolocation, and weather API.

Sunday 9/15: Integrate SSO, geolocation, and weather API. Begin working on SQL dummy data for temperature/humidity.
Update timeline, begin Agile Sprint 1.

Monday 9/16: Complete Sprint 1 by midnight. COMPLETED.

Tuesday 9/17: Start Sprint 2. Complete by Wednesday midnight.

Wednesday 9/18: Hard deadline for sprint 2 at midnight. Project fully completed and tested. ONLY cosmetic changes allowed after this

Thursday 9/19: Complete sprint 2. Finalize cosmetic changes. Deploy to google cloud. Have everything fully deployed and tested (multiple users in particular) by midnight.

Friday 9/20: Project due. Keep app deployed.

# Sprints
Sprint 1: Starting 9/15 until midnight 9/16. Integrate SSO and the geolocation/weaather pages into a web app using
Python (flask). Test sign in, page navigation, weather and geolocation. Release version 1.0 COMPLETED.

Sprint 2: Starting 9/17 until midnight 9/18. Integrate Google Cloud SQL database in order to hold dummy temperature
and humidity data. Pull and display this data on a chart. Allow capability for different data sets to be shown. 
Finalize all cosmetic changes and deploy to google cloud. Test multiple user accesses. Release version 2.0 COMPLETED


