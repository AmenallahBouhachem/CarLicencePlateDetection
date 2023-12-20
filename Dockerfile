
FROM python:3.11.0



WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    tesseract-ocr \
    libtesseract-dev

ENV PATH="/usr/bin/tesseract:${PATH}"


RUN tesseract --version

EXPOSE 5000


ENV NAME World



CMD ["python", "app.py"]
