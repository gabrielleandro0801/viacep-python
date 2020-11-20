import requests

print('#######################')
print('### Consulta de CEP ###')
print('#######################')

def main():

    cep_input = input('\nDigite o CEP para consulta: ')

    if len(cep_input) != 8:
        print('Quantidade invalida de digitos!')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json'.format(cep_input))

    address_data = request.json()
    if 'erro' not in address_data:
        print('==> CEP ENCONTRADO <==')
        print('CEP: {}' .format(address_data['cep']))
        print('UF: {}' .format(address_data['uf']))
        print('Municipio: {}' .format(address_data['localidade']))
        print('Bairro: {}' .format(address_data['bairro']))
        print('Logradouro: {}' .format(address_data['logradouro']))
    else:
        print('CEP invalido!')

    opcao = input('\nDeseja buscar novamente? ')

    if opcao.lower() == 'sim':
        main()
    else:
        print('Fim de Programa')

if __name__ == '__main__':
    main()

