from sqlalchemy import create_engine

import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# connect_MySQL.py の修正後コード

from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# --- ここからが修正箇所 ---

# 1. このファイル(connect_MySQL.py)が存在するディレクトリのパスを取得
#    例: /home/site/wwwroot/db_control
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. 証明書ファイルの絶対パスを構築する
#    '..' を使って、一つ上の階層(backend/)に移動し、ファイル名を結合する
#    例: /home/site/wwwroot/DigiCertGlobalRootCA.crt.pem
CERT_PATH = os.path.join(BASE_DIR, '..', 'DigiCertGlobalRootCA.crt.pem')

# 3. 不要になった環境変数の読み込みを削除
# SSL_CA_PATH = os.getenv('SSL_CA_PATH')  <- この行は削除またはコメントアウトします

# --- ここまでが修正箇所 ---

# データベース接続情報
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# MySQLのURL構築
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SSL_CA_PATH = os.getenv('SSL_CA_PATH')
# エンジンの作成
engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    pool_recycle=3600,
    connect_args={
        "ssl_ca": SSL_CA_PATH
    }
)
