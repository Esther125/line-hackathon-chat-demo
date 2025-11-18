# line-hackathon-chat-demo

## Run the Chat Demo

```
docker compose up -d
```

## Switch to Your Own Local Model

Follow these steps if you want Ollama WebUI to use a local .gguf model.

1. Put your model file into the Ollama volume
    ```
    mkdir -p ollama-data/models
    cp your_model.gguf ollama-data/models/
    ```
    This folder is mounted to /root/.ollama/models inside the container.
2. Create a Modelfile
   Inside ollama-data/models/, add a file named Modelfile:
    ```
    FROM ./your_model.gguf
    TEMPLATE """{{ .Prompt }}"""
    ```
3. Build your model inside the Ollama container Start the containers (if not already running):
    ```
    docker compose up -d
    ```
    Enter the Ollama container:
    ```
    docker exec -it ollama bash
    ```
    Build the model (you can choose any model name):
    ```
    ollama create mylocalmodel -f /root/.ollama/models/Modelfile
    ```
    Check that it was created:
    ```
    ollama list
    ```
4. Set the default model for the WebUI
   Update docker-compose.yml:
    ```
    environment:
        - OLLAMA_BASE_URL=http://ollama:11434
        - DEFAULT_MODEL=mylocalmodel
    ```
5. Restart everything
    ```
    docker compose down
    docker compose up -d
    ```
    Open the WebUI:
    http://localhost:3000
    Your local model should now be available and set as default.
