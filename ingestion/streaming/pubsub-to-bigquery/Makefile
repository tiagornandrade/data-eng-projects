PROJECT = $$(PROJECT_ID)
REGION = $$(REGION)
BUCKET = $$(BUCKET)


build-image:
	gcloud config set project $(PROJECT) && \
	gcloud builds submit --tag "gcr.io/$(PROJECT)/samples/dataflow/pipe-dataflow:latest" .

create-flex-template:
	gcloud dataflow flex-template build "gs://$(BUCKET)/samples/dataflow/templates/pipe-dataflow.json" \
	  --image "gcr.io/$(PROJECT)/samples/dataflow/pipe-dataflow:latest" \
	  --sdk-language "PYTHON" \
	  --metadata-file "metadata.json"

run-flex-template:
	export GOOGLE_APPLICATION_CREDENTIALS=credential.json && \
	gcloud config set project $(PROJECT) && \
	gcloud dataflow flex-template run "pipe-dataflow-`date +%Y%m%d-%H%M%S`" \
		--template-file-gcs-location "gs://$(BUCKET)/samples/dataflow/templates/pipe-dataflow.json" \
		--region "us-central1"
