FROM windows10







RUN python



# We copy just the requirements.txt first to leverage Docker cache

COPY ./requirements.txt /app/requirements.txt



WORKDIR /app



RUN pip install -r requirements.txt



COPY . /app



ENTRYPOINT [ "python" ]





CMD ["run.py","--host=0.0.0.0:5000" ]