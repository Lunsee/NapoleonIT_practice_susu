import os
import csv
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

class PollingData(BaseModel):
    question1: str
    question2: str
    question3: str
    question4: str
    question5: str
    question6: str
    question7: str
    question8: str


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")




@app.post("/submit_data_polling")
async def submit_data_polling(
    question1: str = Form(...),
    question2: str = Form(...),
    question3: str = Form(...),
    question4: str = Form(...),
    question5: str = Form(...),
    question6: str = Form(...),
    question7: str = Form(...),
    question8: str = Form(...)
):
    print(f"Received data: question1={question1}, question2={question2}, question3={question3}, question4={question4},"
        f" question5={question5}, question6={question6}, question7={question7}, question8={question8}")
    if all([question1, question2, question3, question4, question5, question6, question7, question8]):
        csv_file_path = "results_polling.csv"


        if not os.path.exists(csv_file_path):
            with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["Инструменты и платформы для хранения данных?", "CI/CD процессы?", "Используется контейнеризацию и оркестрацию контейнеров?",
                     "Предпочтения по используемым технологиям и инструментам?", "специфические требования к безопасности?",
                     "Насколько критична для вас интеграция с существующими системами и инструментами?",
                     "Какие метрики вы используете,Устраивают ли вас результаты?",
                     "Есть ли у вас специфические кейсы или примеры, где вы сталкиваетесь с трудностями и хотели бы улучшить процессы?"])


        with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([question1, question2, question3, question4, question5, question6, question7, question8])
        return RedirectResponse(url="http://localhost:8501/?page=ml_system", status_code=303)
    return



@app.get("/ml_system", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("ml_system.html", {"request": request})




@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("feature.html", {"request": request})



