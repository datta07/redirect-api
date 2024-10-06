from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.api_route("/tvschedule/{path_params:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])
@app.api_route("/tvschedule", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])
async def tvschedule(request: Request, path_params: str = None):
    response_message = {
        "status": "error",
        "message": "This API has been moved due to unforeseen circumstances.",
        "migration_info": {
            "moved_since": "2024-01-01",
            "new_api_url": "https://rapidapi.com/Garuda07/api/indian-tv-schedule-api",
            "documentation_url": "https://rapidapi.com/Garuda07/api/indian-tv-schedule-api/docs"
        },
        "status_code": 301,  # 301 Moved Permanently status code for API relocation
        "request_id": request.headers.get("X-Request-ID", "N/A")
    }
    return JSONResponse(content=response_message, status_code=301)
