import requests
import json
from flask import Flask


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)  # Используем name для создания экземпляра Flask


def create_html(valutes):
    text = '<h1>Курс валют</h1>'
    text += '<table border="1">'
    text += '<tr>'

    # Создаем заголовки таблицы на основе ключей первого словаря в списке
    for key in valutes[0].keys():
        text += f'<th>{key}</th>'
    text += '</tr>'

    for valute in valutes:
        text += '<tr>'
        for value in valute.values():
            text += f'<td>{value}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":  # Используем name, чтобы определить, запускается ли скрипт напрямую
    app.run()