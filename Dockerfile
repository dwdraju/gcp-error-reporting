FROM python:3.8-slim
RUN pip install google-cloud-storage && pip install flask
WORKDIR /app
COPY ./ /app/
EXPOSE 5000
CMD python main.py
