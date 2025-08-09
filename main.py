import os
import tkinter as tk
from tkinter import filedialog

# Создаем скрытое окно Tkinter
root = tk.Tk()
root.withdraw()

# Выбор входного файла
input_file = filedialog.askopenfilename(
    title="Выберите TXT файл с акцизами",
    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
)

if not input_file:
    print("❌ Файл не выбран. Завершение.")
    exit()

# Выбор папки для сохранения
output_dir = filedialog.askdirectory(
    title="Выберите папку для сохранения"
)

if not output_dir:
    print("❌ Папка не выбрана. Завершение.")
    exit()

# Словарь: поставщик -> список акцизов
data = {}

# Читаем файл
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 2:
            acciz = parts[0]
            supplier = " ".join(parts[1:])
            data.setdefault(supplier, []).append(acciz)

# Записываем по поставщикам
for supplier, accizes in data.items():
    safe_name = supplier.replace("/", "_").replace("\\", "_").replace(":", "_")
    output_path = os.path.join(output_dir, f"{safe_name}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(accizes))

print(f"✅ Готово! Файлы сохранены в: {output_dir}")
