# Simple Flask/React App
This sets up full-stack application using flask & react

## Description
This will serve the web-app and server off of the same host and port. 
The project after checking out should have the structure below. 
```
$ tree
.
├── README.md
├── package-lock.json
├── package.json
├── public
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
├── run.py
├── simple_app
│   ├── __init__.py
│   └── __pycache__
│       └── __init__.cpython-37.pyc
└── src
    ├── App.css
    ├── App.js
    ├── App.test.js
    ├── index.css
    ├── index.js
    ├── logo.svg
    └── serviceWorker.js
```

## Installation
```
$ npm install           # install web-app dependencies
$ npm run build         # build web-app
$ pip install flask     # install our framework
```

## Development
TODO 
```

```

## Running
```
$ python3 run.py 
 * Serving Flask app "simple_app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 311-207-644
```
The application should now be available at `http://localhost:5000/`