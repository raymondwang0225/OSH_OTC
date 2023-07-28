import streamlit as st
import pandas as pd

def main():
    st.title("買賣單交易數據")

    # 載入現有數據或創建新的 DataFrame
    transactions_df = load_data()

    # 顯示買賣單交易數據
    st.write("### 當前交易數據：")
    st.dataframe(transactions_df)

    # 添加新的買賣單交易數據
    st.write("### 添加新的買賣單交易數據：")
    order_id = st.text_input("掛單序號：")
    price = st.number_input("價格(USDT)：", step=0.01)
    quantity = st.number_input("數量(OSH)：", step=1.0)
    trade_type = st.selectbox("交易類型：", ["買單", "賣單"])

    if st.button("新增交易"):
        add_transaction(transactions_df, order_id, price, quantity, trade_type)
        st.success("交易已添加！")

    # 保存更新後的數據
    save_data(transactions_df)

def load_data():
    # 加載現有數據，如果數據不存在，創建新的 DataFrame
    try:
        transactions_df = pd.read_csv("transactions.csv")
    except FileNotFoundError:
        transactions_df = pd.DataFrame(columns=["掛單序號", "價格(USDT)", "數量(OSH)", "交易類型"])
    return transactions_df

def add_transaction(df, order_id, price, quantity, trade_type):
    # 將新的交易數據添加到 DataFrame
    new_row = {"掛單序號": order_id, "價格(USDT)": price, "數量(OSH)": quantity, "交易類型": trade_type}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    return df

def save_data(df):
    # 將更新後的數據保存到 CSV 文件
    df.to_csv("transactions.csv", index=False)

if __name__ == "__main__":
    main()
