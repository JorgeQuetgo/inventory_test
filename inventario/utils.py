from inventario.models import Inventory, LoadFile
from django.core.files.base import File
import decimal
import openpyxl
import json


def load_document(file: File, object: LoadFile):
    book = openpyxl.load_workbook(file)
    sheet = book.active
    total_rows = sheet.max_row
    total_quantity = 0
    total_price = 0
    resume = dict()
    for row in sheet.values:
        if not None in row:
            add_to_inventory(serial_number=row[0], stock=row[1], price=row[2])
            total_quantity += row[1]
            total_price += row[2]
    resume["elementos"] = total_quantity
    resume["precio_promedio"] = total_price / total_rows
    object.jfile = json.dumps(str(resume))
    object.save()




def add_to_inventory(serial_number: str, stock: int, price: decimal):
    product = Inventory.objects.filter(serial_number=serial_number).first()
    if product is None:
        Inventory.objects.create(
            serial_number=serial_number,
            stock=stock,
            price=price
        )
        return
    product.stock += stock
    product.save()
    return




