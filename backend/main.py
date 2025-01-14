from fastapi import FastAPI
import csv
from models.prompt_model import PromptResponse
from models.init_db import init_db, get_db

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"Hello": "World"}

CSV_FILE_PATH = "/app/data/benchmark_llm_monitoring.csv"

def load_csv_to_db(file_path: str, db_session):
    """
    Загружает данные из CSV-файла в базу данных
    """
    try:
        with open(file_path, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                record = PromptResponse(
                    prompt=row.get("prompt"),
                    response=row.get("response"),
                    prompt_label=row.get("prompt_label"),
                    response_refusal_label=row.get("response_refusal_label"),
                    response_label=row.get("response_label"),
                    model=row.get("model"),
                    language=row.get("language"),
                    source=row.get("source"),
                    prompt_length=row.get("prompt_length"),
                    response_length=row.get("response_length"),
                    security_rag_prompt_harm_label=row.get("security_rag_prompt_harm_label"),
                    security_rag_response_refusal_label=row.get("security_rag_response_refusal_label"),
                    security_rag_response_harm_label=row.get("security_rag_response_harm_label"),
                    sec_rag_prompt_label=row.get("sec_rag_prompt_label"),
                )

                db_session.add(record)
            db_session.commit()

            print(f"Данные из {file_path} успешно загружены в базу данных.")

    except Exception as e:
        db_session.rollback()
        print(f"Ошибка при загрузке данных: {e}")

@app.on_event("startup")
def startup_event():
    engine = init_db()
    session = next(get_db())

    try:
        load_csv_to_db(CSV_FILE_PATH, session)

    except Exception as e:
        print(f"Файл {CSV_FILE_PATH} не найден.", e)
