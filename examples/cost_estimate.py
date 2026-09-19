from whatsapp_number_validator import WhatsAppNumberValidatorClient

for count in (10, 100, 1000):
    print(count, WhatsAppNumberValidatorClient.estimate_cost(count), "USD estimated result charges")
