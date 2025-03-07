import fastapi
import os
import fastapi.templating as templating

app = fastapi.FastAPI()

PATH_TEMPLATES = os.path.abspath(os.path.join(__file__, "..","..", "templates"))
templates = templating.Jinja2Templates(directory=PATH_TEMPLATES)