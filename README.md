# Hikvision_Events_To_Telegram
Python script developed to receive the alerts of hikvision NVR / DVR / Camera installed in my home directly to my mobile phone and computer at work via telegram

1. Setup FatherBot:
  a. Add Fatherbot to your telegram account - https://t.me/botfather
  b. Use the /newbot command to create a new bot -  The BotFather will ask you for a name and username, then generate an authentication token for your new bot.
  c. Save the token you get - The token is a string along the lines of 116598543:ADDdqTcvCH1vFCJxfSeofERs0K9LALDsaw that is required to authorize the bot.
  ![image](https://user-images.githubusercontent.com/64651645/169857015-bc34de2d-c735-46cf-9f6d-8d548243ab56.png)
  
2. Get your telegram ID:
  a. Add userinfobot to your telegram account - https://telegram.me/userinfobot
  b. Save the id you get 
  ![image](https://user-images.githubusercontent.com/64651645/169857683-deaf853d-c894-4276-99e3-2f176c17b545.png)

3. A new bot must first be set up through FatherBot:
  a. Connect to HIKVISION equipment through the Web interface. 
  b. Navigate to Configruation -> Network -> Advanced settings -> Alram Server
  c. Set the IP of the server running the script.
  ![image](https://user-images.githubusercontent.com/64651645/169856713-d47822bd-7b14-494e-a467-b982b9a0dc43.png)


4. Run the script in this format: ./main.py 'token' '
