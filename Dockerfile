FROM python:3.11.2-slim-bullseye

WORKDIR /app

# ADD Somenew 
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# With this command I think the server will work with 
# the initial configuration
CMD ["python", "src/app.py"]
