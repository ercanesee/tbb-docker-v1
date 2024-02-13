#from tagi ile hangi base imaj kullanılacaksa belirtilir.
FROM python:3.10-bullseye as ercan

#app adında bir klasör oluşturmak için.

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["flask","run","--host=0.0.0.0"]