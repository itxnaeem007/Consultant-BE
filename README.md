# Setup #

### Clone this project ###

```
 https://github.com/Naeem-source/Ch-Consultant-Service-BE.git
 ```
 ```
 cd Ch-Consultant-Service-BE
 ```

 ## Development Environment
To develop or run the application locally, there are several dependencies and
build steps that need to be taken care of:
- [Environment Dependencies]
  - [Python]
  - [Git]
- [Database]

### Environment Dependencies

#### Python
Install Python v3.8.
A list of releases can be found [here](https://www.python.org/downloads/)

Installation can be verified by running the command
`python` in a terminal.

## Virtual Environment
Once Python is installed, create a virtual environment to store any 
Python-specific dependencies. If the default
version of Python is the appropriate version, this can be done with `python -m
venv venv`. If multiple versions of Python are installed, a more specific
command is required:

With an alias:
```
python3 -m venv venv
```
or with a path to the executable: 
```
/usr/bin/python3 -m venv venv
```

Once created, activate the venv with the `activate` script:

On Linux:
```
source venv/bin/activate
```

On Windows (Git Bash):
```
source venv/Scripts/activate
```

On Windows (Powershell):
```
.\venv\Scripts\activate
```

On Windows (Command Prompt):
```
venv\Scripts\activate
```

An indicator (something like `(venv)`) should appear before the terminal
prompt. If this is missing, the venv has not been activated.

_Creating_ the venv only needs to be done once, unless it is removed.
_Activating_ the venv should be done whenever running code or installing
dependencies, if it is not already active. It can be deactivated with the command `deactivate`.

## Install required packages ##
```
pip install -r requirements.txt

```

## Migration ##
```
python manage.py makemigrations && python manage.py migrate
```
## Run ##
```
python manage.py runserver host:port
```
(Host and port are optional by default it starts at port 8000) 

## Creating Account

### Superuser ###
```
python manage.py createsuperuser
```

### Accessing Admin Panel ###
```
http://127.0.0.1:8000/admin

provide superuser credentials you created above
```


## API Usage 

# BLOG API #

- Blog List API: http://127.0.0.1:8000/api/blog/list

    -   Paginated list:
        - Use query params `page` (10 items will be returned)
            ```
            host:port/api/blog/list?page=1
            ```
        

    -   Filter by using query param `search`:
        -  E.g. to return list by  `Author Name`(you can filter list by `Title`,`Author's Username`,`overview`.)
        ```
        host:port/api/blog/list?search=azhar
        ```
- Blog Create API: ```http://127.0.0.1:8000/api/blog/create/```
  -{
    "title":"",
    "overview": "",
    "content":"",
    "author":1,
    "thumbnail": file
  }
  
  Here ```<id>``` refer's to id of user.
- Blog Detail API:
  - ```http://127.0.0.1:8000/api/blog/detail/<id>```

- Blog Update API:
  - ```http://127.0.0.1:8000/api/blog/update/<id>```

- Blog Delete API: 
  -```http://127.0.0.1:8000/api/blog/delete/<id>```

- Author List API:
  - ```http://127.0.0.1:8000//api/blog/author/list```

- Author Blog List API:
  - ```http://127.0.0.1:8000/api/blog/author/blogs/<id>``` 
# Services API
- Service List API
  - ``` http://127.0.0.1:8000/api/service/list ```


# Team API
- Team List API
  - ``` http://127.0.0.1:8000/api/team/list ```


# Auth API
- Login API
  -```http://127.0.0.1:8000/api/auth/token/login/```
  This will return token. You can use that token to access protected content. 
  
- Logout API
  -``` http://127.0.0.1:8000/api/auth/token/logout/ ```
