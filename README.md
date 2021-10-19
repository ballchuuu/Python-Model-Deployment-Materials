# PYTHON FOR MODEL DEPLOYMENT

The following repository contains the materials (i.e. codes and guide) for an introduction to model deployment using Python

### Materials available:

<b> |- 01_Intro_to_API_Model_Deployment.pdf </b>: Slides on the overview of APIs (theory) can be found in the [Materials](Materials) folder

<b> |- Lab02_Flask_Model_Deployment </b>
<br>&nbsp;&nbsp;&nbsp;&nbsp;
        |- <b> 02_Guide_for_API_Creation.pdf </b>: Guide to explain more indepth on the API creation using Flask framework 
<br>&nbsp;&nbsp;&nbsp;&nbsp;
        |- <b> app_vader_completed.py </b>: Completed version of app.py
<br>&nbsp;&nbsp;&nbsp;&nbsp;
        |- <b> app_vader_bert_completed.py </b>: Completed pytohn code which deploys both bert and vader model
<br>&nbsp;&nbsp;&nbsp;&nbsp;
        |- <b> Workshop </b>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> requirements.txt </b>: List of packages that need to be installed before lab can be run (the packages can be installed via `pip install -r requirements.txt`)
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> app.py </b>: Main app python file that contains blanks for own hands-on learning in coding out the endpoints to deploy the vader model
            |- <b> utils.py </b>: Utility functions for model inference
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> static </b>: Contains static assets such as model weights and frontend css files
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> templates </b>: Contains the frontend HTML file

<b> |- Lab03_Flask_Containerised_Deployment </b>
        |- <b> 03_Guide_for_Containerised_Deployment.pdf </b>: Guide to explain more indepth on the containerising Flask applications using Docker and Azure Kubernetes Service
<br>&nbsp;&nbsp;&nbsp;&nbsp;
        |- <b> Workshop </b>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> requirements.txt </b>: List of packages that need to be installed before lab can be run (the packages can be installed via `pip install -r requirements.txt`)
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> app.py </b>: Main app python file 
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> utils.py </b>: Utility functions for model inference
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> Dockerfile </b>: Dockerfile to containerise the application
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> mloe_flask_workshop </b>: Yaml file for Azure Kubernetes Service
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            
            |- <b> nvidia-device-plugin-ds </b>: Yaml file to configure GPU in Azure Kubernetes Service
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> static </b>: Contains static assets such as model weights and frontend css files
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> templates </b>: Contains the frontend HTML file
            
<b> |- Lab04_Flask_Database_Integration </b>
        |- <b> 04_Guide_for_Database_Integration.pdf </b>: Guide to explain more indepth on the database integration for Flask applications
<br>&nbsp;&nbsp;&nbsp;&nbsp;
        |- <b> Workshop </b>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> requirements.txt </b>: List of packages that need to be installed before lab can be run (the packages can be installed via `pip install -r requirements.txt`)
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> app.py </b>: Main app python file 
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> utils.py </b>: Utility functions for model inference
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> manage.py </b>: App Flask Manager file
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> models.py </b>: Contains all the database classes
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> static </b>: Contains static assets such as model weights and frontend css files
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            |- <b> templates </b>: Contains the frontend HTML file

<i> Note For the BERT Model weights, please download them from the following [Google Drive Link](https://drive.google.com/drive/folders/1TZUOcuM29V4hq3MIjVKSAwzARJTl79sn?usp=sharing) and unzip them into the respective static/models folder in the Lab folders. </i>

<br>
<b> Have fun with the materials! </b>
<br>
<img src="i-love-learning.jpg" width="350" height="200">
