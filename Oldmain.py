import pandas as pd
import numpy as np
import random
# Завантаження файлів
export_df = pd.read_excel("export-2025-05-28_16-34-43(old).xlsx")
template_df = pd.read_excel("import_template (1).xlsx")

# Маппінг: шаблон -> експорт
column_mapping = {
    "OFFERID": "ID товару/послуги",
    "Категорія": "Категорія",
    "Артикул": "ID товару/послуги",
    "Назва": "Товар/Послуга",  # буде особлива обробка
    "Назва (укр)": "Товар/Послуга",
    "Ціна": "Ціна",
    "Стара ціна": "Ціна",
    'Серія': "Штрихкод",
    "Виробник": "Виробник",
    "Зображення": "Зображення",
    "Наявність": "Ярлики",
    "Залишки": "Залишок на складі"
}
# Фільтрація по категорії
# Фільтрація по категорії та наявності (в наявності або очікується)
filtered_export_df = export_df[
    (export_df["Категорія"].isin(["Відеокарти AMD (Radeon)", "Відеокарти NVIDIA (GeForce)"]))
].reset_index(drop=True)
pd.set_option('display.max_rows', None)

# Выводим DataFrame
print(filtered_export_df)
# Створення порожнього DataFrame з колонками шаблону
output_df = pd.DataFrame(columns=template_df.columns)

# Заповнення згідно мапінгу
for template_col, export_col in column_mapping.items():
    if template_col in output_df.columns and export_col in filtered_export_df.columns:
        print(template_col, export_col)
        if template_col == "Назва (укр)":
            output_df[template_col] = "Відеокарта " + filtered_export_df[export_col].astype(str)
        elif template_col == 'Назва':
            output_df[template_col] = "Видеокарта " + filtered_export_df[export_col].astype(str)
        elif template_col == "Ціна":
            price = (filtered_export_df[export_col] * 1.075)
            output_df[template_col] = np.ceil((price)/10)*10
        elif template_col == "Стара ціна":
            old_price = ((filtered_export_df[export_col] * 1.075)*(random.uniform(1.10,1.15)))
            output_df[template_col] = np.ceil((old_price)/10)*10
        elif template_col == "Залишки":
            # Залишки поки не заповнюємо тут, бо обробимо їх пізніше разом з наявністю
            continue
        elif template_col == 'Наявність':
            # Обробимо окремо нижче, щоб уникнути конфлікту
            continue
        else:
            output_df[template_col] = filtered_export_df[export_col].values

        if 'Зображення' in output_df.columns:
            output_df['Зображення'] = output_df['Зображення'].astype(str).str.replace(",", ";")

availability = filtered_export_df[column_mapping['Наявність']]

mask = availability.isin(["Очікується", "Під замовлення"])

output_df['Наявність'] = np.where(mask, "Не в наявності", availability)
output_df['Кнопка передзамовлення|232597'] = np.where(mask, "Передзамовити", "")
output_df['Залишки'] = np.where(mask, 1, filtered_export_df[column_mapping['Залишки']])

output_df['Наявність'] = output_df['Наявність'].replace("Немає в наявності", "Не в наявності")


# Якщо шаблон має більше колонок — заповнюємо порожніми
for col in template_df.columns:
    if col not in output_df.columns:
        output_df[col] = ""

# Гарантуємо, що всі колонки йдуть у тому самому порядку, як у шаблоні
output_df = output_df[template_df.columns]

# Збереження
output_file = "import_goods10.xlsx"
output_df.to_excel(output_file, index=False)

print(f"✅ Файл збережено як: {output_file}")