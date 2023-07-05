from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Anik', 'age':20}}



@app.get('/about')
def about():
    return {'data': 'About Page'}
