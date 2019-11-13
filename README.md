# otp_vulnerable_app

This repository contains the application which will give you the hackable demo environment of OTP Application. You can use your hack technique on this application. Also the scope of this application is very small right now, its just focuses on OTP hack techniques, also you may encounter some XSS scnerios and more which you can ignore them or you can exploit those for getting more view (but those are out of scope).

Stages
======

The stage includes simple method as well as a little difficult method. It includes requests blocking stuffs.


# Pre-Requirements

1. You have to give you **Gmail** Username credentials. For now you need to give your credentials 2 times, in **sendotp.py** in different satges i.e. 1 & 2. I am working on it will updates this soon.

2. You may face some error like below
`(535, b'5.7.8 Username and Password not accepted`. Below is the Solution.

You need to activate Less secure apps in your accounts. Below is the link which will take you on that way.
https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none

3. I tested this application on the PHP server like below
  `x:\> cd otp_vulnerable_app`
  `x:\otp_vulnerable_app\> php -S ip:port` You need to remain open until you are testing.  
  
4. If somehow you are not getting the OTP you may need to debug `sendotp.py` file which you may needs a some python knowledge. 
  
 # Working Environment 
 `Python 2.7/Python 3X Can be Windows, Linux`. In linux I didn't try but I am sure it will run.
  
# Thoughts

If I got a good reaction on this application then I will work more on this to create more vulnerables stages.

# Feedback/Issues

If you encounter any issues please let me know. And also if you have any suggestion regarding this application like how we can create it more advance or something else, I would like to hear those too.

And don't forget to send me a feedback.

# Contact
Twitter [agrawalsmart7](https://twitter.com/agrawalsmart7)
