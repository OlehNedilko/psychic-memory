import uvicorn

def main():
    try:
        uvicorn.run(app='app:app', reload=True)    
    except Exception as exception:
        print(exception)

if __name__ == "__main__":
    main()