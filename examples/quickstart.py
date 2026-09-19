from whatsapp_number_validator import WhatsAppNumberValidatorClient

client = WhatsAppNumberValidatorClient()
rows = client.run({'workflow': 'auto',
 'phoneNumbers': ['+14155552671'],
 'defaultCountry': 'US',
 'outputPreset': 'full'})
print(rows[0] if rows else "No results")
