# docsapp_assignment
To run on local:
	1) Checkout the code
	2) cd src
	3) python3.7 manage.py runserver <port|default 8000>
	4) access following urls:
		a) customerapp - http://localhost:8000/customerapp.html
		b) driverapp - http://localhost:8000/driverapp.html?id= <driver_id [1,2,3,4,5]>
		c) operations - http://localhost:8000
		d) django-admin - http://localhost:8000/admin

TODO:
	1) Deployment Pending (My aws account is suspended for some reason..Will resolve/create and then deploy
	2) Currently using sqlite instead mysql as db for simplicity, No code change is required to use mysql except settings
	3) Version 2 solution
