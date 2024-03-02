# BotTalk Backend

## Setup

1. Modify `.secret/.secret.sh` to add the following secrets:

    - Open AI Secret:
      ```bash
      export OPENAI_API_KEY=####
      ```

    - If using a service account file:
      ```bash
      export GOOGLE_APPLICATION_CREDENTIALS="######"
      ```

    - Other optional variables can be added:
      ```bash
      export OPEN_AI_PORT=####  # Default value is 5000 if not specified
      export VERTEX_AI_PORT=####  # Default value is 5001 if not specified
      ```

2. Install requirements:
   ```bash
   pip3 install -r requirements.txt
   ```

## Run Appplication

    ./run.sh


VS CODE Build with Dev-container extension can also be used to serve the applications