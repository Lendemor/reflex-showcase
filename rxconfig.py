import reflex as rx


config = rx.Config(
    app_name="pynecone_showcase",
    db_url="sqlite:///pynecone.db",
    env=rx.Env.DEV,
    frontend_port=3002,
    backend_port=8002,
    api_url="http://localhost:8002"
)
