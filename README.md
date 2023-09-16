# Flask-background worker
 
##  use correct version of Python when creating VENV
python3 -m venv venv

##  activate on Unix or MacOS
source venv/bin/activate

##  activate on Windows (cmd.exe)
venv\Scripts\activate.bat

##  activate on Windows (PowerShell)
venv\Scripts\Activate.ps1

##  Activated environment will appear
(venv) D:\Flask-Simple-app>

# Send request below which will execute a long running tasks but the api will give quick response.
<pre>

curl --location --request GET 'http://127.0.0.1:9001/simple_module/long_task_endpoint'
</pre>

# Setting up requirements

## requirement.txt
### -  Create requirements.txt file
### - Add flask as primary requirement
### - celery==5.2.7 , redis

##  install the modules in your requirements.txt file

### pip install -r requirements.txt


# How to use the application 

## STEP 1 : Check api is working 
### http://localhost:9001/simple_module/test

## STEP 2 : Insert sample data into db
### http://localhost:9001/simple_module/db/insert

## STEP 3 : Check inserted data
### http://localhost:9001/simple_module/db/place/all

## STEP 4 : Create index 
### http://localhost:9001/simple_module/db/place/index

## STEP 5 : Search location (Nearby location near thrissur within 3000 m range)
### http://localhost:9001/simple_module/db/place/search
