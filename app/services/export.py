import io
from typing import List
from app.models.asset import Asset


class ExportService:
    def assets_to_csv(self, assets: List[Asset]) -> bytes:
        import csv

        output = io.StringIO()
        writer = csv.writer(output, delimiter=";")

        writer.writerow([
            "ID", "Tag", "Nome", "Descrição", "Número de Série", "Marca", "Modelo",
            "Status", "Localização", "Categoria", "Responsável", "Departamento",
            "Data Compra", "Valor Compra (R$)", "Garantia Até", "Observações",
            "Criado em", "Atualizado em",
        ])

        for a in assets:
            writer.writerow([
                a.id,
                a.tag,
                a.name,
                a.description or "",
                a.serial_number or "",
                a.brand or "",
                a.model or "",
                a.status.value if a.status else "",
                a.location or "",
                a.category.name if a.category else "",
                a.responsible_user.name if a.responsible_user else "",
                a.responsible_user.department if a.responsible_user else "",
                a.purchase_date.strftime("%d/%m/%Y") if a.purchase_date else "",
                f"{a.purchase_value:.2f}".replace(".", ",") if a.purchase_value else "",
                a.warranty_expires.strftime("%d/%m/%Y") if a.warranty_expires else "",
                a.notes or "",
                a.created_at.strftime("%d/%m/%Y %H:%M") if a.created_at else "",
                a.updated_at.strftime("%d/%m/%Y %H:%M") if a.updated_at else "",
            ])

        return output.getvalue().encode("utf-8-sig")

    def assets_to_excel(self, assets: List[Asset]) -> bytes:
        import pandas as pd

        rows = []
        for a in assets:
            rows.append({
                "ID": a.id,
                "Tag": a.tag,
                "Nome": a.name,
                "Descrição": a.description or "",
                "Número de Série": a.serial_number or "",
                "Marca": a.brand or "",
                "Modelo": a.model or "",
                "Status": a.status.value if a.status else "",
                "Localização": a.location or "",
                "Categoria": a.category.name if a.category else "",
                "Responsável": a.responsible_user.name if a.responsible_user else "",
                "Departamento": a.responsible_user.department if a.responsible_user else "",
                "Data Compra": a.purchase_date.strftime("%d/%m/%Y") if a.purchase_date else "",
                "Valor Compra (R$)": a.purchase_value or 0,
                "Garantia Até": a.warranty_expires.strftime("%d/%m/%Y") if a.warranty_expires else "",
                "Observações": a.notes or "",
                "Criado em": a.created_at.strftime("%d/%m/%Y %H:%M") if a.created_at else "",
                "Atualizado em": a.updated_at.strftime("%d/%m/%Y %H:%M") if a.updated_at else "",
            })

        df = pd.DataFrame(rows)
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Ativos de TI")
        return output.getvalue()
