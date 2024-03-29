# Pronotify

Pronote is a school life management software created in 1999 by Index Education, and used in more than 10 000 high schools. It is initially a fat client, but since 2003, there is an extension that allows to use it as a web application: Pronote.net. Since 2008, Pronote is also available as a mobile application. ([Wikipedia](https://fr.wikipedia.org/wiki/Pronote))

While this application is a great way to access your grades on the internet, there is one thing that all French high school students who stress about their grades will tell you:
It lacks a notification system, a way for everyone to have access to their grades when they normally appear on the application.

That's when Pronotify appeared, which, thanks to the [Pronotepy](https://github.com/bain3/pronotepy) and [Telegram](https://core.telegram.org/) APIs, makes the dream of all French high school students come true. Pronotify is a notification system that contacts (gives the new grade, the subject in which the grade was added, and the user's new average) whoever is using it through Telegram whenever there is a new grade on Pronote.


![Pronotepy](https://camo.githubusercontent.com/3ae516af10d2a609989fece36dda63f4d10ee30cca1dd46564454c5bb07697c9/68747470733a2f2f70726f6e6f746570792e72656164746865646f63732e696f2f656e2f6c61746573742f5f696d616765732f69636f6e2e706e67)

# Installation
To test the app, you may deploy it on Heroku's (a script runner from server) platform, a free version of the subscription is enough to cover around 25 to 31 days of each month.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/elazdi-al/pronote-encrypted)
