from .settings import app, PATH_TEMPLATES, templates
import fastapi.responses as responses
import fastapi
import os

@app.get("/{age}")

async def root(request: fastapi.Request, age: int):

    if age < 18:
        return responses.FileResponse(path=os.path.join(PATH_TEMPLATES, 'error.html'))
    else:
        return templates.TemplateResponse(
            request=request,
            name='age.html',
            context={'age': age}
        )