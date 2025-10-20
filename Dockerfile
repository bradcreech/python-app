FROM python:3.10-alpine

COPY ./requirements.txt .

# Install pip packages with trusted hosts to bypass SSL issues
RUN pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --upgrade pip
RUN pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r ./requirements.txt

COPY ./src /src

EXPOSE 5000

CMD ["python3", "/src/app.py"]
