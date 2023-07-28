import pandas as pd
from github import Github
import io

def update_transactions_on_github(transactions_df):
    # 設置 GitHub 倉庫相關信息
    repo_path = "raymondwang0225/OSH_OTC"

    # 使用 PyGithub 連接到 GitHub 倉庫，並指定提交者的帳戶和信箱
    g = Github("raymondwang0225", "raymondwang0225@gmail.com")
    repo = g.get_repo(repo_path)

    # 讀取 transactions.csv 文件內容
    contents = repo.get_contents("transactions.csv")
    content_str = contents.decoded_content.decode("utf-8")

    # 將內容轉換為 DataFrame
    current_transactions_df = pd.read_csv(io.StringIO(content_str))

    # 合併現有的和新的交易數據
    updated_transactions_df = pd.concat([current_transactions_df, transactions_df], ignore_index=True)

    # 將更新後的 DataFrame 轉換為 csv 格式
    updated_content_str = updated_transactions_df.to_csv(index=False)

    # 提交並將更新後的內容推送回 GitHub 倉庫
    repo.update_file(contents.path, "更新 transactions.csv", updated_content_str, contents.sha)

if __name__ == "__main__":
    # 這裡可以寫一些測試代碼來測試 update_transactions_on_github 函數
    pass
