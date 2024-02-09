import dlt

from chargebee import chargebee_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(pipeline_name="chargebee_pipeline", destination='duckdb',
                            dataset_name="chargebee_dataset", full_refresh=True)
    source = chargebee_source()
    info = pipeline.run(source)
    print(info)
