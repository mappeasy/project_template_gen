import os

def create_file(path, content=""):
    """Helper function to create a file with the given content."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    base_dir = "rsso_taskforce"
    os.makedirs(base_dir, exist_ok=True)

    # ---------------------------
    # Backend Setup
    # ---------------------------
    backend_dir = os.path.join(base_dir, "backend")
    os.makedirs(backend_dir, exist_ok=True)

    # Create the app directory structure inside backend
    app_dir = os.path.join(backend_dir, "app")
    os.makedirs(app_dir, exist_ok=True)
    create_file(os.path.join(app_dir, "__init__.py"), "")

    # main.py: FastAPI entry point
    main_py_content = '''from fastapi import FastAPI
from app.routers import dashboard

app = FastAPI(title="RSSO Taskforce Dashboard API")

# Include the dashboard router under /api/dashboard
app.include_router(dashboard.router, prefix="/api/dashboard")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
'''
    create_file(os.path.join(app_dir, "main.py"), main_py_content)

    # Routers directory for endpoints
    routers_dir = os.path.join(app_dir, "routers")
    os.makedirs(routers_dir, exist_ok=True)
    create_file(os.path.join(routers_dir, "__init__.py"), "")
    dashboard_py_content = '''from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_dashboard():
    """
    Simple endpoint to return a welcome message.
    """
    return {"message": "Welcome to the RSSO Taskforce Dashboard"}
'''
    create_file(os.path.join(routers_dir, "dashboard.py"), dashboard_py_content)

    # Models directory for ORM models
    models_dir = os.path.join(app_dir, "models")
    os.makedirs(models_dir, exist_ok=True)
    user_model_content = '''# Define ORM models here (e.g., for users)
'''
    create_file(os.path.join(models_dir, "user.py"), user_model_content)

    # Schemas directory for Pydantic schemas
    schemas_dir = os.path.join(app_dir, "schemas")
    os.makedirs(schemas_dir, exist_ok=True)
    user_schema_content = '''# Define Pydantic schemas here (e.g., for user data)
'''
    create_file(os.path.join(schemas_dir, "user.py"), user_schema_content)

    # requirements.txt for backend dependencies
    requirements_txt_content = '''fastapi
uvicorn
'''
    create_file(os.path.join(backend_dir, "requirements.txt"), requirements_txt_content)

    # ---------------------------
    # Frontend Setup
    # ---------------------------
    frontend_dir = os.path.join(base_dir, "frontend")
    os.makedirs(frontend_dir, exist_ok=True)

    # Public directory for static files
    public_dir = os.path.join(frontend_dir, "public")
    os.makedirs(public_dir, exist_ok=True)
    index_html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RSSO Taskforce Dashboard</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
'''
    create_file(os.path.join(public_dir, "index.html"), index_html_content)

    # src directory for React source code
    src_dir = os.path.join(frontend_dir, "src")
    os.makedirs(src_dir, exist_ok=True)
    
    # App.js: Main React component
    app_js_content = '''import React from 'react';
import Dashboard from './components/Dashboard';

function App() {
  return (
    <div className="App">
      <h1>RSSO Taskforce Dashboard</h1>
      <Dashboard />
    </div>
  );
}

export default App;
'''
    create_file(os.path.join(src_dir, "App.js"), app_js_content)

    # index.js: React entry point
    index_js_content = '''import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
'''
    create_file(os.path.join(src_dir, "index.js"), index_js_content)

    # Create components directory and Dashboard component
    components_dir = os.path.join(src_dir, "components")
    os.makedirs(components_dir, exist_ok=True)
    dashboard_js_content = '''import React, { useEffect, useState } from 'react';

function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Fetch dashboard data from FastAPI backend
    fetch('/api/dashboard')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error("Error fetching dashboard data:", error));
  }, []);

  return (
    <div>
      {data ? <p>{data.message}</p> : <p>Loading dashboard data...</p>}
    </div>
  );
}

export default Dashboard;
'''
    create_file(os.path.join(components_dir, "Dashboard.js"), dashboard_js_content)

    # package.json for frontend dependencies and proxy configuration
    package_json_content = '''{
  "name": "rsso-taskforce-dashboard",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "proxy": "http://localhost:8000"
}
'''
    create_file(os.path.join(frontend_dir, "package.json"), package_json_content)

    print("Project structure for 'rsso_taskforce' has been created.")

if __name__ == "__main__":
    main()
