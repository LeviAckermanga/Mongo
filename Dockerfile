FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install Flask pymongo

# RUN apt-get update && apt-get install -y \
#    curl zip # 
# CMD /bin/bash
# RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

EXPOSE 5000

CMD ["python", "app.py"]