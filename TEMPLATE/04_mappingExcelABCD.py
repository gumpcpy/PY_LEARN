'''
Author: gumpcpy gumpcpy@gmail.com
Date: 2024-11-02 18:09:02
LastEditors: gumpcpy gumpcpy@gmail.com
LastEditTime: 2024-11-02 19:08:16
Description: 
我想要一個python的程式，可以讀取一個excel表格，
四個column分別是Raw, Shotname, Short, Mapped。
我想要逐一讀取Short裡面的簡短名稱，去Shotname對應找到符合的，
然後把Raw的內容填到Short旁邊的Mapped這樣。可以幫我實現嗎？

我的Shotname是這樣的SHOT_0770A_02_100fps_NG
然後我的Short是0770A 02 這樣的。
所以規則是 要先把Shotname的內容用underline都分割開來，
然後Short的這裡則是把空格的部分分割開來，
就會變成尋找 0770A 以及 02 同時存在於Shotname分割開來的元素裡面。
這樣就算是符合。
'''
import pandas as pd


def process_find(file_path):

    # 讀取 Excel 檔案
    df = pd.read_excel(file_path)

    # 確保所需的列都存在
    required_columns = ['Raw', 'Shotname', 'Short', 'Mapped']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Excel 檔案缺少必要的列")

    # 創建一個字典，將 Shotname 映射到對應的 Raw 值
    shotname_to_raw = dict(zip(df['Shotname'], df['Raw']))

    # 對每一個 Short 值進行處理
    for index, row in df.iterrows():
        short_value = row['Short']

        # 確保 short_value 是字符串類型
        if pd.notna(short_value):
            short_value = str(short_value)
            short_parts = short_value.split()
        else:
            # 如果 short_value 是 NaN，跳過這一行
            continue

        # 在 Shotname 中尋找匹配項
        matching_shotname = next(
            (shotname for shotname in shotname_to_raw.keys()
            if all(part in shotname.split('_') for part in short_parts)),
            None
        )

        if matching_shotname:
            # 如果找到匹配項，將對應的 Raw 值填入 Mapped 列
            df.at[index, 'Mapped'] = shotname_to_raw[matching_shotname]

    # 將結果保存回 Excel 檔案
    df.to_excel(file_path, index=False)

    print("處理完成，結果已保存到 'updated_excel_file.xlsx'")


if __name__ == '__main__':

    excel_file_path = input("拖入Excel檔案: ").strip()
    process_find(excel_file_path)
