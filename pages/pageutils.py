def get_session_cookie(page):
    for cookie in page.context.cookies():
        if cookie["name"] == "sessionid":
            return {"sessionid": cookie["value"]}
    return None