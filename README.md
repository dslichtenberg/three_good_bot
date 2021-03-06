# three_good_bot

## Client Setup in Slack
1. setup in slack: go to [api.slack.com/apps](https://api.slack.com/apps)
2. **Click Create an App**
![Step 1](/images/step1.png)
3. Create the Slack App: 
    * Fill in App Name: **Three Good for Slack** 
    * Under Development Slack Workspace, choose your company slack workspace (you may have to log in)
    * Click **Create App**
![Step 2](/images/step2.png)
4. **On the next screen click OAuth & Permissions on the left hand menu.**
    * Set up the permissions to mirror the below images
![Step 3](/images/scopes.png)
5. **Click *Install App to Workspace***
![Step 5](/images/step5.png)
7. **Note the *OAuth Access Token* and the *Bot User OAuth Access Token***. 
![Step 7](/images/step7.png)



## Set up environment and run code 

1. install docker on your computer: [instructions](https://docs.docker.com/install/)
2. download this repository and unzip it. move/rename the resulting folder to your personal folder : (e.g. `/Users/dan/three_good_bot`)
3. build the docker container: on a mac, first launch the docker application (Applications > Docker). You don't need to log in. then launch the terminal application. type
`cd three_good_bot/docker`
then
`docker build -t three_good_bot .`
4. after this is complete (takes a few minutes) set up is done. 
5. to create and send new messages, open the `slackbot_config.xlsx` spreadsheet to enter new messages.  you can use a slack username to direct a message to one user or leave it blank to send to all slack users. save the file when you're ready to send the messages.
6. to run the application, which will send all unsent messages, double-click "send_slack_messages.sh"
(if this doesn't work, in the terminal type `~/three_good_bot/send_slack_message.sh`)
