from whatsapp_number_validator import WhatsAppNumberValidatorClient

client = WhatsAppNumberValidatorClient()
payload = {'workflow': 'auto',
 'phoneNumbers': ['+14155552671'],
 'defaultCountry': 'US',
 'outputPreset': 'full'}
# Add more targets or queries to the list fields supported by this Actor.
rows = client.run(payload)
print(f"Received {len(rows)} rows")
