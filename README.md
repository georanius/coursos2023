# <b> Digitale Techniken - With Python
Johanna Kerch (since WiSe 2021/22), 
Göran Liebs (since WiSe 2023/24)
    
<b> This workshop takes place from 9.-13. october from 9.00h until 15.00h in MN 13 und MN 13b.<br>
    
## <b> Welcome to the project
This course likes to introduce modern programming technics to every one, with learning by doing.<br>
This course is a development project on the cloud-based service for software development and version control from the Gesellschaft für wissenschaftliche Datenverarbeitung mbH Göttingen (gitlab, GWDG).<br>
Those git-projects might be cloned and forked by other users, to improve or to use them for new projects, respectivaly.
There are many more of such platforms in the world wide web, working similarly.<br>
Like for every git-repositories in such platforms, this text your are reading is automaticaly displayed from the file README.md and should explain well the project.<br>
```Git``` is a version control programm that tracks changes in any folder (directory) with an hidden folder. <br>
The course uses Jupyter Notebooks, an open source web application that can be used to create and share documents that contain live code, equations, visualizations, and text. The code cells are executable with costumized kernels for several programming languages.<br>

## <b> Settings
- A real computer with internet connection and a browser<br>
- An user account at gitlab https://gitlab.gwdg.de/ to access, store and manages programming projects<br>
https://docs.gwdg.de/doku.php?id=en:services:email_collaboration:gitlab:start <br>
- An user account at https://jupyter-cloud.gwdg.de, a virtual computer with jupyterlab, used via your local browser<br>
- Or Anaconda installed on a real computer that, runs a jupyter lab that you use with your browser.

## <b> Prerequisites

- How to use a web-browser<br>
- Basic listening/reading comprehension in English<br>
- The lectures (B.Geo.211 Digitale Techniken)<br>

## <b> Content

- Forking/Cloning a Git-Repository
- Jupyter Notebook
- Some shell commands in Bash and Git, change and track
- Python
    - basics: data types, strings, lists, dictionaries
    - control flow and functions, list comprehension
    - distribution/environment, package manager/pip
    - read data from txt, numpy, pandas, missing data, data access via api (DIGIS/GEOROC example)
    - visualise data, datetime
    - data analysis: interpolation, regression, polynomial fit, filter
    - object-oriented programming, class example
    - IDE (PyCharm/Spyder), VScode, Vim, Emacs, etc. 
    - code testing/unit tests
    - and some phantastic real live applications

# Installation, let's go...   

<b> Please follow bold instructions: <br>

### <b> Start your own developer jupyter-computer in the cloud
<b> In your Web-browser go to https://jupyter-cloud.gwdg.de/ and click login.<br>
<b> Use your gwdg account, choose the default jupyterlab.<br>

That starts your developer-computer (jupyterlab) in the data center of the GWDG (cloud, many connected computers or servers, ...). <br>
Changing your homecomputer or laptop to a programmers-computer can be hard and all your work might just run at your machine but not necessarily on others. <br>
Or install Anaconda, and use the jupyterlab of this python distribution.
<br>
<b> When your jupyterlab is running, click: File -> New -> Terminal.<br>

This is a bash shell, a commando based userinterface of your developermachine.<br>
<br>
    
### <b> Forking gitlab-projects
    
As we like to integrate this course as a real-live-development-project, you have two possibilities:<br>
    
<b> First, Preferred: Log in to your gitlab account (if not done already), search this project with the search bar and by clicking the magnifying glass symbole. Than click the fork-symbole at the right of the star symbol. And follow the following pages. <br>
You will see a massage that the project was forked. Now you own a project with the content of this course in your account.<br>
Now if you like to run this project, you will copy a version including the hidden git-file (saves changes and origin) to your computer, that is what we call a clone.  

Second: In a repository you may ask the owner for permissions. And then a generated access key is requiered, to work at this project with an owner-defined role (i.e. developer, distributer,...). Consult the file 'Securitykey2bDevOfProject.md' if you like to do so. This  allows you to suggest changes to the original repository directly.<br>
    
### <b> Copy the URL of the repository 
<b> Now switch between profile view to the project view at your gitlab home page (account).
<b> You should see this file and others...<br>
<b> Now click the clone-button and click the little clipboard button (under cloning with ssh), to copy the URL (internetadress).<br>
<br>
<br>

### <b> Cloning the repository
<b> In the web-browser-tab with your jupyter-computer-terminal you run following command, with pasting the copied URL of your 
repository fork.  <br>

```git clone << past here copied URL from YOUR FORK! >> ```
<br>

A clone is not just a copy, there is still a connection between this git-repositories. Knowing each other, there can be exchanges of changes between them.
E.g. a clone can update changes from his origin (```git pull```), or ask to upload (```git push```) his changes to the origin. 
<br>
If you have been successfull, you see a new folder (digitale-techniken-wise2324) in the filebrowser list at the left, in your GWDGjupytercloud-maschine, in your browse, on your sreen... 

<br>
<b>Now click on the folder (digitale-techniken-wise2324-pre). Then open the file Go_here_after_README_done.ipynb.

A jupyter notebook with the extention .ipynb.
<br>


  
