# Chargebee API v1 source

Chargebee source contains the following resources:

* `subscriptions`
* `customers`
* `invoices`
* `orders`
* `transactions`
* `events`

It extracts data from v1 API and perform normalizations.

## How to use this source
To use chargebee source please do the following:

### Set up the credentials

1) You need to set the `site` in `.dlt/config.toml` under `base_url` parameter. For example

```toml
[chargebee_pipeline]
base_url = "https://name-test.chargebee.com/api/v2"
```

2) [Create an API key](https://www.chargebee.com/docs/api_keys.html) and set it in `.dlt/secrets.toml` under `api_key` parameter. For example
```toml
[chargebee_pipeline.credentials]
api_key = "xxxx"
```

### Install dlt with the required destination 

This example uses `duckdb`. But you can use any of available [destinations](https://dlthub.com/docs/dlt-ecosystem/destinations/).

```
pip install 'dlt[duckdb]'
```

### Run the pipeline

```
python chargebee_pipeline.py
```
