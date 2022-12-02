Testing for fabrique.studio

This project is under development.
To run the project, follow the steps:

    Clone the project to a local machine
    install dependencies from the file requirements.txt
    Open the terminal and go to the /fabrick/fabrick directory
    execute the commands:

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

что работает:
- запускается сервер с API 
- Можно создавать/редактировать/удалять сущности
- при создании рассылки - запускается процедура начала рассылки или постановки в очередь.


К сожалению саму рассылку/постановку в очередь не успел сделать