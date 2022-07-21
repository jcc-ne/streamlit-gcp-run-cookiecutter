.PHONY: run gcloud-deploy
rootdir = $(realpath .)

run:
	@streamlit run main_dashboard.py

gcloud-deploy:
	@cd deploy/ && ./deploy_prod.sh
