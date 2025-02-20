from src.reading_file import reading_file_csv,reading_file_xlsx
import os

if __name__ == "__main__":
    file_path_csv = os.path.join("data_1", "transactions.csv")
    operations = reading_file_csv(file_path_csv)
    for operation in operations:
        print(operation)

if __name__ == "__main__":
    file_path_xlsx = os.path.join("data_1", "transactions_excel.xlsx")
    print(reading_file_xlsx(file_path_xlsx))
