from fastapi import Response
from fastapi.responses import HTMLResponse


class JavascriptResponse(Response):
  media_type = "text/javascript"


class StyleSheetResponse(Response):
  media_type = "text/css"
