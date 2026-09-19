import json
from whatsapp_number_validator import WhatsAppNumberValidatorClient

rows = WhatsAppNumberValidatorClient().run({'workflow': 'auto',
 'phoneNumbers': ['+14155552671'],
 'defaultCountry': 'US',
 'outputPreset': 'full'})
with open("results.json", "w", encoding="utf-8") as handle:
    json.dump(rows, handle, ensure_ascii=False, indent=2)
