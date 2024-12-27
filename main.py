from src.masks import get_mask_account, get_mask_card_number

print(get_mask_card_number(input("Введите номер карты: ")))
print(get_mask_account(input("Введите номер счета: ")))


from src.widget import get_date, mask_account_card

mask_account_card(input())
print(get_date("2024-03-11T02:26:18.671407"))