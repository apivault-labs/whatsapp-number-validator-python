import os
from whatsapp_number_validator import WhatsAppNumberValidatorClient

if not os.environ.get("APIFY_API_TOKEN"):
    raise SystemExit("Set APIFY_API_TOKEN before running this example")
client = WhatsAppNumberValidatorClient()
print(client.run_one({'workflow': 'auto',
 'phoneNumbers': ['+14155552671'],
 'defaultCountry': 'US',
 'outputPreset': 'full'}))
