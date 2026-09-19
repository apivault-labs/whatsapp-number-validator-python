# WhatsApp Number Validator — Python SDK

Python client for the [WhatsApp Number Validator Apify Actor](https://apify.com/apivault_labs/whatsapp-number-validator). Send public Actor inputs, wait for the hosted run, and receive clean Dataset rows without maintaining scraping infrastructure.

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-blue)](https://apify.com/apivault_labs/whatsapp-number-validator)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Results

- Bulk phone-number input
- International number normalization
- WhatsApp availability result
- Public profile and phone metadata when available

Availability can change over time. Validation and processing remain inside the hosted Actor.

## Install

```bash
pip install git+https://github.com/apivault-labs/whatsapp-number-validator-python.git
```

Create an Apify token at [Console → Integrations](https://console.apify.com/account/integrations), then:

```python
from whatsapp_number_validator import WhatsAppNumberValidatorClient

client = WhatsAppNumberValidatorClient(api_token="apify_api_xxxxxx")
rows = client.run({'workflow': 'auto',
 'phoneNumbers': ['+14155552671'],
 'defaultCountry': 'US',
 'outputPreset': 'full'})
print(rows[0] if rows else "No results")
```

You can set `APIFY_API_TOKEN` instead of passing the token in code.

## Public input options

| Field | Type | Default | Description |
|---|---|---|---|
| `workflow` | `string` | `auto` | Validate and enrich supplied numbers. |
| `phoneNumbers` | `array` | `[]` | Phone numbers, preferably in international format. |
| `numbersText` | `string` | `` | A pasted list or CSV column of numbers. |
| `defaultCountry` | `string` | `US` | ISO-2 country used for numbers without a country code. |
| `outputPreset` | `string` | `full` | Choose a public result layout. |

The complete, versioned schema is also available on the [Actor page](https://apify.com/apivault_labs/whatsapp-number-validator).

## Pricing

Pay per delivered result through Apify, starting around **$3/1,000 results** on paid tiers. Free-plan pricing and platform usage can differ; check the Actor page before large runs.

## Examples

- `examples/quickstart.py` — first run
- `examples/bulk_analysis.py` — expand a target list
- `examples/export_csv.py` — save flat result fields
- `examples/save_json.py` — preserve nested output
- `examples/cost_estimate.py` — estimate result-event charges
- `examples/environment_token.py` — keep credentials out of code

## Architecture and privacy

This repository is intentionally a thin API client. Collection, retries, analysis and billing run inside the hosted Apify Actor. No private implementation, credentials, scoring weights or infrastructure configuration are included.

## License

MIT. The hosted Actor is a separate paid service governed by Apify terms.
