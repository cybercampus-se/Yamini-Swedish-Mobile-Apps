Voi App Vulnerabilities:

![](media/977c97e0f36312cc3686fc94d0b22b34.png)

In shared_pref, I can find my email, name , mobile number and userId in plain text.

![A screenshot of a computer AI-generated content may be incorrect.](media/ae62e6d4cb0618b13109fb4d4c37dcaa.png)  
I can intercept the Voi App using Frida and Objection.

![A screenshot of a computer program AI-generated content may be incorrect.](media/0c2aed3e5cc0f97673a55d7f629a9b50.png)  
![A screenshot of a computer AI-generated content may be incorrect.](media/92cd6b2b004a880fca8e50dcc88d61b2.png)

I can see the user-id and session ID is visible.  
  
![A computer screen with white text AI-generated content may be incorrect.](media/cd74f982f462b62ac8edfaad09e3b5d0.png)

These IDs can be exploited by attackers to **replay sessions** or gain unauthorized access and the Logs are stored in plain text.  
The log contains information about **3D Secure (3DS) authentication steps**:

-   Submit authentication pressed
-   Challenge task initialized

If this information is accessible, it could allow an attacker to **bypass or replay authentication**.
