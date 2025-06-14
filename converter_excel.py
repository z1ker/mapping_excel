import pandas as pd
import numpy as np
import random
from datetime import datetime
import os



class GoodsProcessor:
    def __init__(self, export_path, template_path, output_path, template_sheet_name):
        self.export_path = export_path
        self.template_path = template_path
        self.output_path = output_path
        self.template_sheet_name = template_sheet_name

        self.column_mapping = {
            "OFFERID": "ID товару/послуги",
            "Категорія": "Категорія",
            "Артикул": "ID товару/послуги",
            "Назва": "Товар/Послуга",
            "Назва (укр)": "Товар/Послуга",
            "Ціна": "Ціна",
            "Стара ціна": "Ціна",
            'Серія': "Штрихкод",
            "Виробник": "Виробник",
            "Зображення": "Зображення",
            "Наявність": "Ярлики",
            "Залишки": "Залишок на складі"
        }

    def load_data(self):
        self.export_df = pd.read_excel(self.export_path)

        self.template_df = pd.read_excel(self.template_path, sheet_name=self.template_sheet_name)

    def filter_data(self):
        categories = ["Відеокарти AMD (Radeon)", "Відеокарти NVIDIA (GeForce)"]
        self.filtered_df = self.export_df[self.export_df["Категорія"].isin(categories)].reset_index(drop=True)

    def process_data(self):
        self.output_df = pd.DataFrame(columns=self.template_df.columns)

        for template_col, export_col in self.column_mapping.items():
            if template_col in self.output_df.columns and export_col in self.filtered_df.columns:
                if template_col == "Назва (укр)":
                    self.output_df[template_col] = "Відеокарта " + self.filtered_df[export_col].astype(str)
                elif template_col == "Назва":
                    self.output_df[template_col] = "Видеокарта " + self.filtered_df[export_col].astype(str)
                elif template_col == "Ціна":
                    price = self.filtered_df[export_col] * 1.075
                    self.output_df[template_col] = np.ceil(price / 10) * 10
                elif template_col == "Стара ціна":
                    old_price = (self.filtered_df[export_col] * 1.075) * random.uniform(1.10, 1.15)
                    self.output_df[template_col] = np.ceil(old_price / 10) * 10
                elif template_col in ["Залишки", "Наявність"]:
                    continue  # опрацюємо пізніше
                else:
                    self.output_df[template_col] = self.filtered_df[export_col].values

        # Обробка зображень
        if "Зображення" in self.output_df.columns:
            self.output_df["Зображення"] = self.output_df["Зображення"].astype(str).str.replace(",", ";")

        # Обробка наявності та залишків
        availability_col = self.column_mapping['Наявність']
        stock_col = self.column_mapping['Залишки']
        availability = self.filtered_df[availability_col]
        mask = availability.isin(["Очікується", "Під замовлення"])



        self.output_df['Наявність'] = np.where(mask, "В наявності", availability)
        self.output_df['Кнопка передзамовлення|232597'] = np.where(mask, "Передзамовити", "")
        self.output_df['Термін доставки|252319'] = np.where(mask, "5", "")
        self.output_df['Залишки'] = np.where(mask, 1, self.filtered_df[stock_col])
        self.output_df['Наявність'] = self.output_df['Наявність'].replace("Немає в наявності", "Не в наявності")

        self.output_df['Залишки'] = self.output_df['Залишки'].apply(lambda x: 0 if x < 0 else x)

        # Дозаповнення колонок, яких не вистачає
        for col in self.template_df.columns:
            if col not in self.output_df.columns:
                self.output_df[col] = ""

        # Гарантуємо порядок колонок
        self.output_df = self.output_df[self.template_df.columns]

    def process_data_characreristics(self):
        try:
            import openpyxl
            from io import BytesIO

            # === 1. Знайти рядок з якого починаються дані (EAN;RU|...)
            with open(self.export_path, "rb") as file:
                workbook = openpyxl.load_workbook(filename=BytesIO(file.read()), data_only=True)
                sheet = workbook.active

                start_row_idx = None
                for i, row in enumerate(sheet.iter_rows(values_only=True), start=1):
                    for cell in row:
                        if isinstance(cell, str) and cell.startswith("EAN;RU|"):
                            start_row_idx = i + 1  # дані починаються з наступного рядка
                            break
                    if start_row_idx:
                        break

                if not start_row_idx:
                    print("❌ Не знайдено рядок, що починається на 'EAN;RU|'")
                    return
            characteristics_df = pd.read_excel(self.template_path, skiprows=start_row_idx - 1)
            # === 3. Перевірити наявність 'Артикул'
            if "OFFERID" not in self.export_df.columns or "OFFERID" not in self.template_df.columns:
                print("❌ У одному з файлів не знайдено колонку 'OFFERID'")
                return
            merged_df = self.export_df.copy()

            # === 5. Доповнюємо даними
            for col in characteristics_df.columns:
                if col == "Артикул":
                    continue
                if col not in merged_df.columns:
                    print('Не підходять файли')
                    break
                else:
                    temp = characteristics_df[["Артикул", col]]
                    merged_df = merged_df.merge(temp, on="Артикул", how="left", suffixes=("", "_char"))

                    if col.lower() in ["термін доставки", "передзамовлення"]:
                        # Повністю замінюємо значення
                        merged_df[col] = merged_df[f"{col}_char"]
                    else:
                        # Заповнюємо тільки порожні
                        merged_df[col] = merged_df[col].combine_first(merged_df[f"{col}_char"])

                    merged_df.drop(columns=[f"{col}_char"], inplace=True)

            self.output_df = merged_df
            print("✅ Дані з characteristics.xlsx успішно додані до export_df.")

        except Exception as e:
            print(f"❌ Помилка при злитті характеристик: {e}")

    def save_data(self):


        # Создаем папку output/с_датой, если ее нет
        today_str = datetime.now().strftime("%Y-%m-%d")
        output_dir = os.path.join("output", today_str)
        os.makedirs(output_dir, exist_ok=True)

        # Генерируем уникальное имя файла с учетом времени (чтобы избежать перезаписи)
        timestamp = datetime.now().strftime("%H-%M-%S")
        output_file_path = os.path.join(output_dir, f"{self.output_path}_{timestamp}.xlsx")

        self.output_df.to_excel(output_file_path, index=False)
        print(f"✅ Файл збережено як: {output_file_path}")

    def run(self):
        self.load_data()
        self.filter_data()
        self.process_data()
        self.save_data()

class GoodsProcessor_miners:
    def __init__(self, export_path, template_path, output_path, template_sheet_name, characteristics_path):
        self.export_path = export_path
        self.template_path = template_path
        self.output_path = output_path
        self.template_sheet_name = template_sheet_name
        self.characteristics_path = characteristics_path
        self.column_mapping = {
            "OFFERID": "Артикул",
            "Категорія": "Раздел",
            "Артикул": "Артикул",
            "Назва": "Название(RU)",
            "Назва (укр)": "Название(UA)",
            "Ціна": "Цена",
            "Стара ціна": "Цена",
            "Виробник": "Бренд",
            "Зображення": "Фото",
            "Наявність": "Наличие",
            "Залишки": ""
        }
        self.characteristics_mapping = {}

    def load_data(self):
        self.export_df = pd.read_excel(self.export_path)

        self.template_df = pd.read_excel(self.template_path, sheet_name=self.template_sheet_name)


    def process_data(self):
        self.output_df = pd.DataFrame(columns=self.template_df.columns)

        for template_col, export_col in self.column_mapping.items():
            if template_col in self.output_df.columns and export_col in self.export_df.columns:
                if template_col == "Ціна":
                    price = self.export_df[export_col] * 1.075
                    self.output_df[template_col] = np.ceil(price / 10) * 10
                elif template_col == "Стара ціна":
                    old_price = (self.export_df[export_col] * 1.075) * random.uniform(1.10, 1.15)
                    self.output_df[template_col] = np.ceil(old_price / 10) * 10
                elif template_col in ["Залишки", "Наявність"]:
                    continue  # опрацюємо пізніше
                else:
                    self.output_df[template_col] = self.export_df[export_col].values

        # Обробка зображень
        if "Зображення" in self.output_df.columns:
            self.output_df["Зображення"] = self.output_df["Зображення"].astype(str).str.replace(",", ";")

        # Обробка наявності та залишків
        #availability_col = self.column_mapping['Наявність']
        #stock_col = self.column_mapping['Залишки']
        #availability = self.export_df[availability_col]
        #mask = availability.isin(["Очікується", "Під замовлення"])

        #self.output_df['Наявність'] = np.where(mask, "Не в наявності", availability)
        #self.output_df['Кнопка передзамовлення|232597'] = np.where(mask, "Передзамовити", "")
        #self.output_df['Залишки'] = np.where(mask, 1, self.export_df[stock_col])
        #self.output_df['Наявність'] = self.output_df['Наявність'].replace("Немає в наявності", "Не в наявності")

        #self.output_df['Залишки'] = self.output_df['Залишки'].apply(lambda x: 0 if x < 0 else x)

        # Обробка наявності та залишків
        availability_col = self.column_mapping['Наявність']
        stock_col = self.column_mapping['Залишки']
        availability = self.export_df[availability_col]

        # Формування колонки "Наявність"
        mask_preorder = availability.isin(["Очікується", "Під замовлення"])
        self.output_df['Наявність'] = np.where(mask_preorder, "Не в наявності", availability)
        self.output_df['Наявність'] = self.output_df['Наявність'].replace("Немає в наявності", "Не в наявності")

        # Кнопка передзамовлення
        self.output_df['Кнопка передзамовлення|232597'] = np.where(mask_preorder, "Передзамовити", "")

        # Логіка заповнення "Залишки"
        # В наявності => 2
        # Не в наявності + є кнопка передзамовлення => 1
        # Не в наявності без кнопки => 0
        self.output_df['Залишки'] = np.select(
            [
                self.output_df['Наявність'] == "В наявності",
                (self.output_df['Наявність'] == "Не в наявності") & (
                            self.output_df['Кнопка передзамовлення|232597'] == "Передзамовити"),
                self.output_df['Наявність'] == "Не в наявності"
            ],
            [2, 1, 0],
            default=0
        )

        # Дозаповнення колонок, яких не вистачає
        #for col in self.template_df.columns:
        #    if col not in self.output_df.columns:
        #        self.output_df[col] = ""

        # 📦 Додавання характеристик за мапінгом
        if not self.characteristics_df.empty and "Артикул" in self.characteristics_df.columns:
            characteristics_prepared = pd.DataFrame()
            characteristics_prepared["Артикул"] = self.characteristics_df["Артикул"]

            for out_col, char_col in self.characteristics_mapping.items():
                 if char_col in self.characteristics_df.columns:
                    characteristics_prepared[out_col] = self.characteristics_df[char_col]
                 else:
                    characteristics_prepared[out_col] = ""

            self.output_df = self.output_df.merge(characteristics_prepared, on="Артикул", how="left")

        for col in self.template_df.columns:
             if col not in self.output_df.columns:
                self.output_df[col] = ""

        self.output_df = self.output_df[self.template_df.columns]



        # Гарантуємо порядок колонок
        self.output_df = self.output_df[self.template_df.columns]

    def save_data(self):


        # Создаем папку output/с_датой, если ее нет
        today_str = datetime.now().strftime("%Y-%m-%d")
        output_dir = os.path.join("output", today_str)
        os.makedirs(output_dir, exist_ok=True)

        # Генерируем уникальное имя файла с учетом времени (чтобы избежать перезаписи)
        timestamp = datetime.now().strftime("%H-%M-%S")
        output_file_path = os.path.join(output_dir, f"{self.output_path}_{timestamp}.xlsx")

        self.output_df.to_excel(output_file_path, index=False)
        print(f"✅ Файл збережено як: {output_file_path}")

    def run(self):
        self.load_data()

        self.process_data()
        self.save_data()
#if __name__ == "__main__":
#    processor = GoodsProcessor("export.xlsx", "import_template4.xlsx", "import_goods6.xlsx")
#    processor.run()
