# GRE HELPER

![PROJECT COVER](./PROJECT_COVER.png)

G.R.E ( Graduate Record Examination ) Helper is a flask web application connected with sqlite database and powered by react frontend that:
1) Evaluates your performance based off of G.R.E mock test and gives you a performance report which specifies topics you should focus on to improve your score. 
2) Users can opt for another mock test curated to topics that the user is weak in.
3) Resources on how to improve your weakness

## Want to Contribute? Great !!

- Select an Issue and get yourself assigned
- Follow the PR guidelines in the file [CONTRIBUTING.md](./CONTRIBUTING.md) to make proper PRs
- Want to understand more about this project ? check out these slides [link](https://www.canva.com/design/DAFjhSgmIlM/Ya46ijOR0QfBka927DwEVg/edit?utm_content=DAFjhSgmIlM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Setup local development environment 

### Method 1:

1. Open terminal inside the directory you want to clone the repo

2. Enter in terminal
``` 
git clone https://github.com/NeerajHazarika/gre_helper.git
cd gre_helper
cd backend 
```

3. Create a new virtual environment:
   
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

4. Install requirements.txt
```
pip install requirements.txt
```

5. Start the flask web server
```
flask run
```

6. Go to `http://localhost:5000` on your web browser, to see if the web server is successfully started or not