from kv_store.app import create_app


def run_app():
    app = create_app()
    app.run()


if __name__ == '__main__':
    run_app()
