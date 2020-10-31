FROM python:3.8-slim
RUN pip install google-cloud-storage flask google-python-cloud-debugger
WORKDIR /app
COPY ./ /app/
EXPOSE 5000
CMD python main.py
