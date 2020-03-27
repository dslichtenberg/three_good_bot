# three_good_bot

## Client Setup in Slack
1. setup in slack: go to [api.slack.com/apps](https://api.slack.com/apps)
2. **Click Create an App**
![Step 1](/images/step1.png)
3. Create the Slack App: 
    * Fill in App Name: **Three Good for Slack** 
    * Under Development Slack Workspace, choose your company slakc workspace (you may have to log in)
    * Click **Create App**
![Step 2](/images/step2.png)
4. **On the next screen click Bot Users on the left hand menu.**
![Step 3](/images/step3.png)
5. **Create the Bot User:**
   * Display name = three_good_bot
   * default username = three_good_bot
   * Click **Add Bot User**
![Step 4](/images/step4.png)
6. **Click *Install App to Your Team***
![Step 5](/images/step5.png)
7. **Review the permissions of the Three Good Slack App and click *Allow* when you are ready.**
![Step 6](/images/step6.png)
8. **Copy the *OAuth Access Token* and the *Bot User OAuth Access Token***.
![Step 7](/images/step7.png)
9. **Send the OAuth Tokens to Three Good (via email or phone)*


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
