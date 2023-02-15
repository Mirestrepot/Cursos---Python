import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/", StaticFiles(directory="static", html=True), name="staticfiles")
@app.get('/')
def get_list():
    return [1,2,3]



@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return {'asdafasdsa'}


def run():
    store.get_categories()

if __name__ == '__main__':
    run()
    