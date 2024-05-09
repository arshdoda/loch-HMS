# HMS(Hospital Management System) sample application

## Setup

The first thing to do is to clone the repository:

```shell
git clone https://github.com/arshdoda/loch-HMS.git
cd loch-HMS
```

Create a virtual environment to install dependencies in and activate it:

```shell
python3 -m venv .venv
source .venv/bin/activate
```

Then install the dependencies:

```shell
(.venv)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:

```shell
(.venv)$ cd backend
(.venv)$ python manage.py runserver
```

And navigate to [http://127.0.0.1:8000/admin]()

## Walkthrough

This django project is build using DRF and **BrowsableAPIRenderer** has been enabled to ease the api usage. The project contains 3 apps which are described below

### Doctor

This app contains all the functionality related to doctors and patient assigned.

APIs Avaliable:

* Create Doctor **[POST]**: [http://127.0.0.1:8000/api/doctor/create]()
* List Doctor **[GET]**: [http://127.0.0.1:8000/api/doctor/list]()  (Available query params: *name, gender, specialization*)
* Create Availability **[POST]**: [http://127.0.0.1:8000/api/doctor/availability/create]()
* List Availability **[GET]**: [http://127.0.0.1:8000/api/doctor/availability/list]() (Available query params: *doctor, date*)
* Assign Patient **[POST]**: [http://127.0.0.1:8000/api/doctor/assign/create]()
* List Assigned **[GET]**: [http://127.0.0.1:8000/api/doctor/assign/list]() (Available query params: *doctor, date*)

### Department

This app contains all the functionality related to department and their services.

APIs Avaliable:

* Create Department **[POST]**: [http://127.0.0.1:8000/api/department/create]()
* List Department **[GET]**: [http://127.0.0.1:8000/api/department/list]() (Available query params: *name, doctor, service*)
* Create Service **[POST]**: [http://127.0.0.1:8000/api/department/services/create]()
* List Servoce **[GET]**: [http://127.0.0.1:8000/api/department/services/list]() (Available query params: *service*)

### Patient

This app contains all the functionality related to patients, their medical history and appointment records.

APIs Avaliable:

* Create Patient **[POST]**: [http://127.0.0.1:8000/api/patient/create]()
* List Patient **[GET]**: [http://127.0.0.1:8000/api/patient/list]()  (Available query params: *name, gender*)
* Create Apointment Record **[POST]**: [http://127.0.0.1:8000/api/patient/appointment-record/create]()
* List Apointment Records **[GET]**: [http://127.0.0.1:8000/api/patient/appointment-record/list](http://127.0.0.1:8000/api/patient/appointment-record/list) (Available query params: *patient, date*)
* Create Medical History **[POST]**: [http://127.0.0.1:8000/api/patient/medical-history/create]()
