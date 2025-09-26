def handler(event, context):
    html = """
    <html>
    <body style='display:flex; flex-direction:column; align-items:center; justify-content:center; min-height:100vh;'>
        <h1 style='text-align:center;'>Hello from Lambda!</h1>
        <img src='https://cataas.com/cat' alt='Cute Cat' style='width:200px; display:block; margin:auto;'>
    </body>
    </html>
    """
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': html
    }
