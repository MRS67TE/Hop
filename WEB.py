import webbrowser

url = "https://web.telegram.org"
user_agent = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.95 Safari/537.36"

# Формируем URL с User-Agent
url_with_user_agent = f"{url}#user_agent={user_agent}"

# Открываем URL в стандартном браузере
webbrowser.open(url_with_user_agent)