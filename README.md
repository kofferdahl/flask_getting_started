# flask_getting_started
Practicing implementing a basic flask webservice 

Running instructions:
Within your local directory after cloning and after installing packages in requirements.txt, run
`python basic_webservice.py`

Then, in a separate command window, start an ipython notebook and import requests.
In that command window, run
`r = requests.get("http://127.0.0.1:5000/name`
and enter
`r.json()` to get the returned data.

To use the hello function, enter
`r = requests.get("http://127.0.0.1:5000/hello/Katelyn`
to get the output of the hello function for the input name Katelyn.

To use the calcDistance function, make a dictionary object with the two points you want to calculate the distance between, e.g.
`data = {
        "a": [1, 2]
        "b": [3, 4]
        }`
to calculate the distance between points (1,2) and (3,4). Then, run
`r = requests.post("http://127.0.0.1:5000/distance", json=data)`

