from web3 import Web3

# MainNet
bsc = "https://bsc-dataseed.binance.org"
# testnet
# bsc = "https://data-seed-prebsc-1-s1.binance.org:8545"

web3 = Web3(Web3.HTTPProvider(bsc))
if web3.is_connected():
    print('Conexion exitosa')

    # CREAR WALLET
    print('')
    print('Creando nueva Wallet')
    create_wallet = web3.eth.account.create()

    new_wallet_address = create_wallet.address
    new_wallet_key = create_wallet.key.hex()

    print('Wallet:    ' + new_wallet_address)
    print('WalletKey: ' + new_wallet_key)