FROM python:3.9

LABEL maintainer="frfrey@student.42lyon.fr"

WORKDIR /usr/app

COPY requirements.txt .
COPY src ./src

RUN pip install -r requirements.txt
RUN mv src/cron-script.py ./

EXPOSE 5280

ENTRYPOINT ["uvicorn","src.main:app","--host", "0.0.0.0", "--port", "5280", "--reload"]
