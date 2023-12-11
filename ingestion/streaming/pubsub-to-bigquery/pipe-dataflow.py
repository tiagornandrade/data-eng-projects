import os
import json
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from dotenv import load_dotenv


load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
SUBSCRIPTION = os.getenv("SUBSCRIPTION")
BUCKET = os.getenv("BUCKET")
DATASET = os.getenv("DATASET")
TABLE = os.getenv("TABLE")


SCHEMA = {
    'fields': [
        {'name': 'reference_day', 'type': 'TIMESTAMP'},
        {'name': 'tenant_id', 'type': 'STRING'},
        {'name': 'contact_id', 'type': 'STRING'},
        {'name': 'contact_name', 'type': 'STRING'},
        {'name': 'contact_email', 'type': 'STRING'},
        {'name': 'contact_job_title', 'type': 'STRING'},
        {'name': 'contact_city', 'type': 'STRING'},
        {'name': 'contact_country', 'type': 'STRING'},
        {'name': 'is_opportunity', 'type': 'STRING'},
        {'name': 'lifecycle_stage', 'type': 'STRING'},
        {'name': 'contact_origin', 'type': 'STRING'},
        {'name': 'created_at', 'type': 'TIMESTAMP'},
    ]
}


def run():
    pipeline_options = PipelineOptions(
        streaming=True,
        project=PROJECT_ID,
        runner='DirectRunner',
        temp_location='gs://pipeline-dataflow-templates/dataflow_temp/',
        region='us-central1',
        save_main_session=True
    )

    with beam.Pipeline(options=pipeline_options) as pipeline:
        (
            pipeline
            | 'Read from PubSub' >> beam.io.ReadFromPubSub(subscription=f'projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION}')
            | 'Decode' >> beam.Map(lambda x: x.decode('utf-8'))
            | 'Parse JSON' >> beam.Map(json.loads)
            | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
                table=f'{PROJECT_ID}:{DATASET}.{TABLE}',
                schema=SCHEMA,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND

            )
        )


if __name__ == '__main__':
    run()
