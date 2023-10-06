### <b> Access to a repository
<b> Scroll up, click the ```Request access``` text, that tells the owner of this repository that you like to work him, e.g. try some changes. 
<br>
<br>  

### <b> Security key generation with a terminal
In this terminal you run a little progamm, to create and write a ssh-key in a file in your home directory:<br>
<b> Just copy the following line into it, type a commend and type the enter key. <br>
```ssh-keygen -t ed25519 -C " <comment here, without(<>) > " ```
<br>
<b>Hit three times enter (no filename, no password).<br>
Then read the created file with the command ```cat```. <br>
<b>Copy the next line into the terminal and hit enter.<br>
Notice the path /home/jovyan/.ssh/ befor the file name, that might be different on an other machine.<br> 
<br>
```cat /home/jovyan/.ssh/id_ed25519.pub ```
<br>
The content of the textfile (a line) will be displayed in the terminal.<br>
<b> copy the key to your clipboard (mark the line, right-click): <br>

(a line like this ```ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGF8kUr4+FGznEDVgyWurIaMeZQv4REQ/GfpDqWCozQI <comment>```)
<br> 
<br>

### <b> Security key adding at your gitlab profile
<b> Then swítch to the browser-tab with this repository (https://gitlab.gwdg.de/<repository name>...) <br> 
<b> Go to "Edit profile → SSH keys" <br>
<b> Or, klick on your accountsymbol (top right, old navigation, now left...).<br>
<b> In the hang out you klick Preferences and then you see far left in the List SSH KEYS (key simbol)<br>
<b> Klick there and then you paste the copied ssh-key from your GWDG-Jupyter-Terminal in the field and click the add key button somewhere below.<br>
(You will get an email when access was granded.)<br>
<br>
