FROM python:alpine3.7
COPY pack.txt test2.py /app/
WORKDIR /app
RUN pip install -r pack.txt
EXPOSE 5000
CMD ["python","./test2.py"]
