FROM python:3.9

LABEL maintainer="frfrey@student.42lyon.fr"

WORKDIR /usr/app

COPY requirements.txt .
COPY src ./src

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["uvicorn","src.main:app","--host", "0.0.0.0", "--port", "8080", "--reload"]
