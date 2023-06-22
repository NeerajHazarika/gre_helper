# GRE HELPER

G.R.E ( Graduate Record Examination ) Helper is a web application that:
1) evaluates your performance based off of G.R.E mock test and gives you a performance report which specifies topics you should focus on to improve your score. 
2) users can opt for another mock test curated to topics that the user is weak in.
3) resources on how to improve your weakness

## Want to Contribute? Great !!

- Select an Issue and get yourself assigned
- Follow the PR guidelines in the file [CONTRIBUTING.md](./CONTRIBUTING.md) to make proper PRs
- want to understand more about this project ? check out these slides [link](https://www.canva.com/design/DAFjhSgmIlM/Ya46ijOR0QfBka927DwEVg/edit?utm_content=DAFjhSgmIlM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Setup local development environment 

### Method 1:

1. open terminal inside the directory you want to clone the repo

2. enter in terminal
``` 
git clone https://github.com/NeerajHazarika/gre_helper.git
cd gre_helper
cd backend 
```

3. create a new virtual environment:
   
check if you have `virtualenv` installed
```
which virtualenv
```
If not, enter command follwing in terminal
```
pip install virtualenv
virtualenv <your_virtualenv_name>
```
replace <your_virtualenv_name> with whatever name you want your virtual environment to be. Eg: myenv

4. install requirements.txt
```
pip install requirements.txt
```

5. start the flask web server
```
flask run
```

6. go to `http://localhost:5000` on your web browser, to see if the web server is successfully started or not