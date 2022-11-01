MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def cek_stok(bahan):
    # melakukan perbandingan dari menu yang di pilih
    # dengan stok barang minuman
    for item in bahan:
        # melakukan pengecekan pada tiap item
        if bahan[item] >= resources[item]:
            print(f"maaf kami kehabisan {item}")
            # jika sesuai maka akan bernilai False
            return False
    # nilai akan bernilai True jika tidak sesuai
    return True

def perhitungan_coin():
    print("Masukan duit anda : ")
    total = int(input("mata uang quarters : ")) * 0.25
    total += int(input("mata uang quarter : ")) * 0.10
    total += int(input("mata uang nickel : ")) * 0.05
    total += int(input("mata uang pennies : ")) * 0.01
    return total

def pesanan(coin, harga_menu):
    if coin >= harga_menu:
        kembalian = round(coin - harga_menu, 2)
        print(f"kembalian kamu {kembalian}")
        global profit
        profit += harga_menu
        return True
    else:
        print("Uang kamu kurang")
        return False


def membuat_pesanan(menu, stok_pesanan):
    for item in stok_pesanan:
        resources[item] -= stok_pesanan[item]
    print(f"Ini {menu} pesanan anda ")


profit = 0
# TODO : 1. ask user for
order = True
while order:
    # melakukan penginputan data
    choice = input("What would you like? (espresso/latte/cappuccino):")
    # menentukan pilihan data jika sesuai
    if choice == "off":
        order = False
    elif choice == "report":
        # menampilkan data resources
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        # untuk menyimpan penghasilan yang dibuat secara gelobal
        print(f"Money: ${profit}")
    else:
        # pilihan jika user memilih minuman
        # drink dibawah menyimpan dect MENU yang berisi minuman
        drink = MENU[choice]
        # function cek_stock dibuat untuk mengecek stok barang
        # dengan membawa drink sebagai dest menu, dan 'ingredients' sebagai isi dari menu
        # jika menu yang dipilih lebih dari resource
        if cek_stok(drink['ingredients']):
            # nilai yang diberikan bernilai True / False
            coin = perhitungan_coin() # mengecek coin user
            if pesanan(coin, drink['cost']): # coin bertujuan untuk melakukan perbandingan dengan drink cost
                membuat_pesanan(choice, drink['ingredients']) # melakukan pengurangan pada stok