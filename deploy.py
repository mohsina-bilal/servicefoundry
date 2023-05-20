image=Build(
        build_spec=PythonBuild(
            command="uvicorn app:app --port 8000 --host 0.0.0.0",
            requirements_path="requirements.txt",
        )
    ),
    ports=[
        Port(
            port=8000,
            host="<Provide a host value based on your configured domain>"
        )
    ],
    resources=Resources(
        cpu_request=0.5,
        cpu_limit=1,
        memory_request=1000,
        memory_limit=1500
    ),
    env={
        "UVICORN_WEB_CONCURRENCY": "1",
        "ENVIRONMENT": "dev"
    }
)
service.deploy(workspace_fqn=args.workspace_fqn)