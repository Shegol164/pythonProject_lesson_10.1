from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    card_number = input()
    account = input()
    print(get_mask_card_number(card_number))
    print(get_mask_account(account))

if __name__ == "__main__":
    print(mask_account_card(input()))
    print(get_date("2024-03-11T02:26:18.671407"))

if __name__ == "__main__":
    data_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    only_executed = filter_by_state(data_list)
    only_canceled = filter_by_state(data_list, "CANCELED")
    sorted_descending = sort_by_date(data_list)
    sorted_acscending = sort_by_date(data_list, False)
    print(only_executed)
    print(only_canceled)
    print(sorted_descending)
    print(sorted_acscending)
