from Flask_DB_SQLalchemy import createApp


flask_app = createApp()

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=5889, debug=True)