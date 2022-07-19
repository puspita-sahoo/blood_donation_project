# blood_donation_project

- Developed a Blood Match Maker Website where people who needs blood can raise request.
- The platform will broadcast the request to all people registered on this platform via mail.
- The matchmaking is done via many filters like pin code, blood group and time slot availability.


## Run Locally for windows


### Clone the project


```bash
  git clone https://github.com/puspita-sahoo/blood_donation_project
```

### Create Environment

```bash
  python -m venv env
```
### Activate Environment(env)

```bash
  env/Scripts/activate
```


## Install all Dependencies


```bash
 pip install -r requirements.txt
```

## Database Migrations


```bash
 python manage.py makemigrations

```
```bash
 python manage.py migrate
```

## Run Server

```bash
python manage.py runserver
```

















