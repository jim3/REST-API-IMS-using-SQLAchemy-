## RESTful API for a Inventory Management System

### Description

A RESTful API for an inventory management application for parts (fasteners). Flask handles the routing and server-side logic. SQLAchemy ORM is used to interact with a SQLite3 database.
The focus of the project is to learn more about the Python/Flask ecosystem as I've gained more interest in Python as a language. I am using a previously developed RESTful API as a starting point. The plan is to develop this project while also developing the same application using Node.js, Express and the Sequelize ORM. At least, that is the plan! :D

### Features

-   Create, Read, Update and Delete parts (CRUD)

---

### Tech Stack

-   Python
-   Flask
-   SQLAlchemy ORM
-   SQLite3


--- 

### API Endpoints

| Endpoint    | HTTP Method | Description       |
| ----------- | ----------- | ----------------- |
| /parts      | GET         | Get all parts     |
| /parts      | POST        | Create a new part |
| /parts/{id} | GET         | Get a part        |
| /parts/{id} | PUT         | Update a part     |
| /parts/{id} | DELETE      | Delete a part     |


----

### Installation

-   Create a virtual environment `python3 -m venv {project_name}`
-   Clone the repository `git clone {repository_url}`
-   `python3 -m venv {project_name}`
-   `source {project_name}/bin/activate`


----

### Example API Call `${localhost}/api/parts`

```json
[
    {
        "id": 1,
        "partName": "Screws",
        "partType": "Socket",
        "price": 0.15,
        "quantity": 100
    }
]
```



### Things to do (really soon)

-   Add more endpoints (CRUD)
-   Add a `index.html` page with a form to create a new part
-   Create an Account model and add authentication with login and logout
-   ...
