### Quick Start

Simple streamlit template to launch microservices using cookiecutter

```
pip install -U cookiecutter
cookiecutter gh:jcc-ne/streamlit-cloudrun-cookiecutter

# -- enter custom project name and db urls

# -- in your venv
cd <project>/
pip install -r requirements.txt
streamlit run main_dashboard.py

```

open browser to the url shown http://0.0.0.0:8501

### Deploy to cloud (GCP version)

Follow instructions on [Install google-cloud-sdk](https://cloud.google.com/sdk/docs/install) to install the
command line tool

### check Makefile
`make gcloud-deploy`  to deploy
