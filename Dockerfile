
FROM python:3.12-slim
WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install streamlit pandas
EXPOSE 8501
CMD ["streamlit", "run", "src/dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
