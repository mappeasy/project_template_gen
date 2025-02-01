A Python script that creates the project structure (without Docker files) and writes the basic file contents for both the FastAPI backend and the ReactJS frontend.

>> python project_template_gen.py

It will create a folder called prj_tmpl with the following structure:
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
