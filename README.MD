# Project Template Generator

A Python script that creates a project structure for a web application with a FastAPI backend and a ReactJS frontend. This script generates the necessary folder structure and basic file contents for both parts of the application, **without Docker files**.

## Overview

Running the script will generate a folder named `prj_tmpl` with the following structure:

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
