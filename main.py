import phonenumbers
from phonenumbers import carrier, geocoder, timezone

numero ='' #coloca teu numero com o code do país(+55) e ddd
numero = phonenumbers.parse(numero)

print(f'Timezone: {timezone.time_zones_for_number(numero)}')
print(f'Operadora: {carrier.name_for_number(numero, "pt-BR")}')
print(f'Informacoes da região: {geocoder.description_for_number(numero, "pt-BR")}')
print(f'Validacao do numero: {phonenumbers.is_valid_number(numero)}')
print(f'Checando a possibilidade no numero: {phonenumbers.is_possible_number(numero)}')

