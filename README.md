
Hello !<br/>

Welcome<br/>

Here you find two folders:<br/>
1. model-building:<br>
This folder contains my .ipynb code for the 
LSTM models I created for the dataset

2. docker-name-gender:<br/>
This folder contains the docker build source for 
the Flask app I build to host, query and retrain
the LSTM model. The app can be interacted with using 
REST api calls. You can find them at 
'Requests code.ipynb'. Alternatively, you can look 
at the endpoint method docstrings in app.py to understand
the details, and assumptions and limitations for the
designed service.

<u>Few Caveats:</u><br/>
1. The Flask API contains an endpoint to retrain 
the model, plus a dummy dataset already. You can choose
to add new data using the postData endpoint, or 
retrain the model directly. This data is stored under
`docker-name-gender / assets / data/ name_gender.csv`.<b> However, if you 
choose to retrain the mode, it may loose performance. 
In this case please replace the model file with the one
provided in `model-building / assets / models /`</b>.

2. There are 2 ways to run the Flask API service.<br/>
    * <u>Via a docker container:</u><br/>
     >to build a container, simply navigate to the 
      `docker-name-gender / ..`, and run<br/><br/>
      `docker build --tag python-name-gender .`<br/>
      then check<br/>
      `docker images`<br/>
      for the "latest" image. Finally, run<br/>
      `docker run --publish 8000:5000 python-name-gender`   <br/>
      <b>NOTE: The build was tested on linux containers (WSL hypervizor). The build may fail in a windows container.<br/><br/>
     * <u>Via you favourite IDE:</u><br/>
     >simply open `docker-name-gender` and run app.py.<br/>
      <u>NOTE: you would need to change the port to 5000 in 'Requests code.ipynb'</u>
                                                                                             
Lastly, let me know in case of any issues.<br/>                                                                           <b>- sabrish89@gmail.com</b>
