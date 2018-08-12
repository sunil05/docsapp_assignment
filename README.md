# docsapp_assignment
</br>To run on local:
</br>	1) Checkout the code
</br>	2) cd src
</br>	3) python3.7 manage.py runserver <port|default 8000>
</br>	4) access following urls:
</br>		a) customerapp - http://localhost:8000/customerapp.html
</br>		b) driverapp - http://localhost:8000/driverapp.html?id= <driver_id [1,2,3,4,5]>
</br>		c) operations - http://localhost:8000
</br>		d) django-admin - http://localhost:8000/admin
</br>
NOTE:
</br>	1) [hack] Auto completion of ride is currently triggered from driverapp after 5minutes of time interval but will not 		work if drivers app is reloaded, although it mocks actual product behaviour as completion API should be triggered 	     by driver only
</br>	   Robust solution would be to do asynchronously on backend.
</br>	2) [OPTIMISATION SCOPE] drivers app fetches bookings periodically from backend, a Realtime DB could be used to avoid polling. 
