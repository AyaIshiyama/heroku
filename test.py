import pykintone
from pykintone import model

# 対象アプリモデル
class Sample(model.kintoneModel):
    def __init__(self):
        super(Sample, self).__init__()
        self.channel=""
        self.customer=""

account = pykintone.load("test.yml")
app = account.app()

# 新規登録するレコードオブジェクトの設定、及び登録処理実行
record = Sample()
print('1')
record.channel = "test"
record.customer = "test2"
result = app.create(record)
print(result)