files = ["1.txt", "2.txt"]

file_data = []

for file_name in files:
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
        file_data.append(
            {"name": file_name, "line_count": len(lines), "content": lines}
        )

file_data.sort(key=lambda x: x["line_count"])

result_file_name = "result_sorted.txt"
with open(result_file_name, "w", encoding="utf-8") as result_file:
    for file_info in file_data:
        result_file.write(f"{file_info['name']}\n" f"{file_info['line_count']}\n")

        result_file.write("".join(file_info["content"]))

print(f"Итоговый файл сохранен как {result_file_name}")
