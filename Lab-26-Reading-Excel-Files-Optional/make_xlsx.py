from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Sales"

ws.append(["Item", "Quantity", "Region"])
ws.append(["Apples", 10, "North"])
ws.append(["Pears", 25, "South"])
ws.append(["Plums", 7, "East"])

wb.save("sample.xlsx")
