import datetime as dt, pandas as pd, codecs, math


def get_help_txt() -> str:
    with codecs.open("/opt/Mtt-Helper-Bot/src/txt/help.txt", "r", "utf_8_sig") as file:
        lines = file.readlines()
        output = "".join(lines)
    return output


def get_currency() -> dict:
    date = dt.datetime.now().strftime("%d/%m/%Y")
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}"
    df = pd.read_xml(url, encoding="cp1251")
    df_dict = df.set_index("CharCode")["VunitRate"].to_dict()
    return df_dict
