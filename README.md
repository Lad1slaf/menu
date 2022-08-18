## Connecting

In docker-compose change POSTGRES_PASSWORD and POSTGRES_USER (if needed) 

In source folder run commands

```bash
docker-compose build
docker-compose up
```

In new terminal

```bash
docker ps
```
Copy CONTAINER ID of menu_web IMAGE

```bash
docker exec -t -i <CONTAINER ID> bash
python manage.py makemigrations
python manage.py migrate
```

## About project
There are two types of users: Employee and Restaurant. You can register ' /api/v1/register/ ' and choose one of those types.

For get JWT token ' /api/token/ ' and ' /api/token/refresh/ ' for refresh

As Restaurant you can:
- Create restaurant ' /api/v1/restaurant/create/ ', but only one for user
- See restaurant details and/or change it ' /api/v1/restaurant/pk '
- Upload menu ' /api/v1/restaurant/add_menu/ ' in PDF, but only one for day
- Change menu ' /api/v1/restaurant/menu/pk/ '

As Employee you can:
- Vote for day menu ' /api/v1/employee/vote/ '
- Change your vote ' /api/v1/employee/change_vote/pk/ '

For getting current day menu with current vote count: ' /api/v1/results/ '