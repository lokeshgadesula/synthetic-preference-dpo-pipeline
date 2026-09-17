FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install .
CMD ["python","-m","preference_dpo.generate","--count","100","--out","data/preferences.jsonl"]
