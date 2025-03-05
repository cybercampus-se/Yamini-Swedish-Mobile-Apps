1.  Used **ADB Shell** to access the app’s internal storage:

    **adb shell**

    **su**

    **cd /data/data/com.sl.SLBiljetter/shared_prefs/**

    **ls**

    **cat release_remote_config.xml**

2.  Navigated to the app’s **Shared Preferences** directory and found

![A black screen with white text AI-generated content may be incorrect.](media/c9ed3d8181fbf033f957f1f2f4770389.png)

3.  Found **API keys and tokens** inside the release_remote_config.XML.

![A screen shot of a computer screen AI-generated content may be incorrect.](media/d854fffea6d172dda2b5449f47750550.png)

4.  Extracted **sensitive JSON data** from release_remote_config.xml (contained **API keys, secrets, tokens**). And The JSON contains multiple API keys and secrets, which, if valid, could allow unauthorized access to SL services.
5.  If "psa_auth" is an authentication key used for user authorization, an attacker could use it to gain unauthorized access to services.

    ![A screen shot of a computer AI-generated content may be incorrect.](media/acc493200b59f35287fef3ffa7a2ea32.png)

6.  Then **Validated JSON using Python script**

    ![A screenshot of a computer AI-generated content may be incorrect.](media/858af03467a19822046a90942b448e0b.png)

7.  **Then testing API keys and secrets** by sending requests to the **SL APIs**

    ![A screenshot of a computer AI-generated content may be incorrect.](media/479d39cef0b4cd042e0f77dc9a721e7f.png)

    ![A screenshot of a computer AI-generated content may be incorrect.](media/d0e5734bb30bdfc08269815de2a53e33.png)

    ![A screenshot of a computer AI-generated content may be incorrect.](media/d912044463e5dbcf5633c51c439dd443.png)

    \--A**ccessed the /databases folder** of the app then found something interesting in Base64 format

    ![A black screen with white letters AI-generated content may be incorrect.](media/50a0ba49a6405aa7622ea216880383fa.png)

-   And tried debugging it.
-   ![A screenshot of a computer AI-generated content may be incorrect.](media/c268cab35e3f1ddc526495747204d785.png)
-   After thoroughly analyzing the SQLite database stored in the /no_backup/ directory of the Android app, I did not find any direct security vulnerabilities.
-   The database structure, including tables like WorkSpec, WorkProgress, and WorkTag, appears to be functioning normally.
-   Additionally, since the data is stored in an app-private directory (/data/data/com.sl.SLBiljetter/), it is already protected from unauthorized access unless the device is rooted.
-   However, while there are no immediate threats, best practices such as avoiding data exports to /sdcard/, ensuring proper backup before modifications.

    ![A screenshot of a computer AI-generated content may be incorrect.](media/afc3f49fa8e30289c41edfe1b97331c1.png)

    \-During analysis,I found that the Jetpack DataStore (\*.preferences_pb) files contain sensitive information, including authentication tokens (userToken, sertoken_readable), --JWT tokens, UUIDs, and tracking-related data.

    These tokens, if exposed, could potentially be used for unauthorized access, account hijacking, or user tracking.

    \- The fact that they are **stored in plaintext** without encryption poses a serious security risk, especially on rooted devices where an attacker could extract and misuse them
