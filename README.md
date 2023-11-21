### :raising_hand: **BiciMAD Planner** 
This app's goal is to  help you navigate through Madrid's MADness with one of the best transport options available for tourism, BiciMAD bicicles.

### :rocket: **Status**
This is the first project for Mardrid Ironhack bootcamp.

### :running: **One-liner**
This app will help you create a **personalized tour plan** based on a given starting and finishing location and some **monuments you want to visit**. It will ccreate an **interactive map** with information about the monument you want to visit and an **optimized route** between the bicimad stations with information about bike availability. For convenience, **other interest places and restaurants** have been added to the map

![Image](data/origin/Example_map.png)

[Give it a try!](https://tour-planner.fly.dev/)

### :computer: **Technology stack**
This app is hosted in a fly.io server as a docker container. The interface for uthe user is composed of a webapp made up with Flask library which executes a python script(main). Main libraries used are requests, pandas, numpy and folium

### :boom: **Core technical concepts and inspiration**
In this project I was asked to do something with Madrid's monuments dataset and BiciMAD's dataset. So my main idea was to create something that would help tourists combine both things, monuments and BiciMAD


### :wrench: **Configuration**
For testing and personal usage you can use the link given above. To run the script in your own system just clone, create a virtual enviroment, install python and then just `pip install -r requirements.txt` on the project folder.

### :file_folder: **Folder structure**
```
└── project
    ├── __wip__
    ├── .venv
    └── data
    │    ├── origin
    │    └── output
    ├── modules
    │   ├── argparser.py
    │   └── dataframe_creation.py
    │   └── email_generator.py
    │   └── main_operations.py
    │   └── map_generator.py
    │   └── route_generator.py
    ├── notebooks
    │   ├── dev_notebook.ipynb
    ├── templates
    ├── .dockerignore
    ├── .env
    ├── .gitignore
    ├── Dockerfile
    ├── install-docker.sh
    ├── LICENSE
    ├── main.py
    ├── README.md
    ├── requirements.txt
    ├── webapp.py    
---
