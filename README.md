
# Litigation MLOps Workflow

This is an MLOps project focused on building a machine learning pipeline for litigation data science. The workflow includes data ingestion, preprocessing, model training, deployment, CI/CD integration, and monitoring.

## How to Run

1. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # on Windows, use venv\Scripts\activate
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI app locally:
    ```bash
    uvicorn api.app:app --reload
    ```

4. Test the pipeline:
    ```bash
    pytest
    ```
