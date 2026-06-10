import pandas as pd
from datetime import date
import smtplib
from email.message import EmailMessage
from pathlib import Path

def import_data(file_path: str) -> pd.DataFrame:
    df = pd.read_json(file_path, encoding = 'utf-8')
    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:

    df['Marca'] = df['Marca'].str.replace("\n", "").str.strip()

    df['PrecioRegular'] = (
                                df['PrecioRegular']
                                .str.replace("S/", "")
                                .str.replace(",", "")
                                .str.strip()
                                .astype(float)
                                .round(2)
                            )

    df['PrecioOnline'] = (
                                df['PrecioOnline']
                                .str.replace("S/", "")
                                .str.replace(",", "")
                                .str.strip()
                                .astype(float)
                                .round(2)
                                )
    
    return df


def load_to_excel(df: pd.DataFrame, file_path: str, sheet: str):

    with pd.ExcelWriter(file_path, engine="xlsxwriter") as writer:

        df.to_excel(writer, sheet_name=sheet, index=False)

        worksheet = writer.sheets[sheet]

        for i, col in enumerate(df.columns):

            ancho = min(
                max(
                    df[col].fillna("").astype(str).str.len().max(),
                    len(col)
                ) + 2,
                75
            )

            worksheet.set_column(i, i, ancho)


def send_email(file_path: str):

    correo_origen = "edgar.quispeq10@gmail.com"
    password_app = "lpya unui kmhh eblt"

    correo_destino = "cursos@addc-peru.com"
    asunto = "Reporte Excel"
    mensaje = "Hola, adjunto el archivo Excel solicitado."

    ruta_excel = Path(file_path)

    if not ruta_excel.exists():
        raise FileNotFoundError(f"No existe el archivo: {ruta_excel}")

    email = EmailMessage()
    email["From"] = correo_origen
    email["To"] = correo_destino
    email["Subject"] = asunto
    email.set_content(mensaje)

    with open(ruta_excel, "rb") as file:
        email.add_attachment(
            file.read(),
            maintype="application",
            subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename=ruta_excel.name
        )

    try:
        print("Conectando...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=60) as smtp:
            smtp.set_debuglevel(1)
            print("Login...")
            smtp.login(correo_origen, password_app)

            print("Enviando...")
            smtp.send_message(email)

        print("Correo con Excel enviado correctamente")

    except Exception as e:
        print("Error al enviar correo:")
        print(type(e).__name__, e)

def main():

    fecha_actual = date.today()
    fecha_format = fecha_actual.strftime('%Y%m%d')
    json_file_path = 'data/raw/Celulares_' + fecha_format + '.json'
    excel_file_path = 'data/clean/Celulares_' + fecha_format + '.xlsx' 

    df = import_data(json_file_path)
    df = transform_data(df)
    load_to_excel(df, excel_file_path, 'data')

    send_email(excel_file_path)

if __name__ == "__main__":
    main()