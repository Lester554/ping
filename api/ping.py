import requests

def handler(request):
    url = 'https://vipa.onrender.com/docs'
    try:
        response = requests.get(url)
        return {
            "statusCode": 200,
            "body": f"Ping exitoso: {response.status_code}"
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error en el ping: {str(e)}"
        }
