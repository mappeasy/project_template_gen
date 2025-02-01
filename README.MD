# Project Template Generator 

A Python script that creates a project structure for a web application with a FastAPI backend and a ReactJS frontend. This script generates the necessary folder structure and basic file contents for both parts of the application, **without Docker files**. 

## Overview 

Running the script will generate a folder named `prj_tmpl` with the following structure: 

Features 
FastAPI Backend: 

backend/app/main.py: Entry point for the FastAPI application. 
Routers: Modular routing is implemented in backend/app/routers/. 
Models and Schemas: Basic user model and schema files are provided. 
requirements.txt: Lists all required Python packages for the backend. 
ReactJS Frontend: 

Public Folder: Contains index.html as the main HTML file. 
Source Folder: Contains the main React component (App.js), the entry point (index.js), and a sample component (Dashboard.js). 
package.json: Contains metadata and dependencies for the React application. 
Usage 
Run the Script 

Open your terminal and execute:  

python project_template_gen.py  

The script will create a folder called prj_tmpl in the current directory with the structure outlined above. Each file will be populated with basic boilerplate code to get you started.

Customization
You can customize the generated project template by editing the project_template_gen.py script. Modify the file contents or add additional files and directories as needed for your project.


```plaintext
prj_tmpl/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   └── dashboard.py
│   │   ├── models/
│   │   │   └── user.py
│   │   └── schemas/
│   │       └── user.py
│   └── requirements.txt
└── frontend/
    ├── public/
    │   └── index.html
    ├── src/
    │   ├── App.js
    │   ├── index.js
    │   └── components/
    │       └── Dashboard.js
    └── package.json
