import pandas as pd
from datetime import date

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
    df.to_excel(file_path, sheet_name=sheet, index=False)


def main():

    fecha_actual = date.today()
    fecha_format = fecha_actual.strftime('%Y%m%d')
    json_file_path = 'data/raw/Celulares_' + fecha_format + '.json'
    excel_file_path = 'data/clean/Celulares_' + fecha_format + '.xlsx' 

    df = import_data(json_file_path)
    df = transform_data(df)
    load_to_excel(df, excel_file_path, 'data')


if __name__ == "__main__":
    main()