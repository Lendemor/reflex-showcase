import pynecone as pc


config = pc.Config(
    app_name="pynecone_showcase",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    port=3002,
)
