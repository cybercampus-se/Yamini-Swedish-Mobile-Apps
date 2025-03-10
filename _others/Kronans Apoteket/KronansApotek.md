Kronans Apotek:

1.  RZ8R708YP9D → physical mobile device.

    emulator-5554 → emulator.

2.  Attempted to send an **intent** to open the **BankID app** on the mobile device using the provided link "https://app.bankid.com/?autostarttoken=90bdb700-0bfc-4de1-a7e2-2e4a6a0e083d&redirect=kronansapotek://"

![A screen shot of a phone AI-generated content may be incorrect.](media/c0c3b2349606ce8c80ef5680af2c511c.png)

-   I tried intercepting the traffic using Frida and Objection.

![A screenshot of a computer AI-generated content may be incorrect.](media/ae68f81197a4409689dcfbcc1205cb19.png)

![A screenshot of a computer AI-generated content may be incorrect.](media/7905badd666e5d7b5b86845d5b1a1ae3.png)

![A black and white screen AI-generated content may be incorrect.](media/9f2db66e78ae8e68d21ffbafe5bf8411.png)

Attempted to add products, increase their quantities, and modify prices directly in the local cache files (/data/data/se.kronansapotek.kronan/cache/http-cache).

These changes were **visible locally** (in the modified files) but **did not reflect in the app**.![A screen shot of a computer AI-generated content may be incorrect.](media/a013fe8e01b1bebb300d41c9e63bb755.png)  
Edited the cartId in local files to see if the app is vulnerable to unauthorized cart modifications.

The new cartId was saved locally, but **no changes were observed** in the app.

The app likely **syncs data with a remote server** and **validates cart information server-side** during each session.

Local modifications to cache files are not affecting the actual cart contents displayed in the app, indicating effective server-side validation and security mechanisms.
