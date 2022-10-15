FROM python:3.10-slim

EXPOSE 5000

WORKDIR /api_hcm

COPY . /api_hcm

RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

CMD ["python", "src/run.py"]