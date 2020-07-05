import pykintone
from pykintone import model
import json
import sys
import datetime

class Kintone(model.kintoneModel):
    # アプリデータの取得
    def appDataget(self):
        # 受け取った引数でAPP接続先を変える
        fileName = self.appName + '_account.yml'
        try:
            account = pykintone.load(fileName)
            app = account.app()
            result = app.select("flag = 0").records
            return result
        except Exception:
            texta = "{}:アプリデータ取得に失敗\n"
            dt = datetime.datetime.now()

            with open("log.txt", "a") as fileobj:
                text = texta.format(dt)   
                fileobj.write(text)

    # 取引先配列生成
    def getCustomerList(self):
        customerList = {
            "rt":"楽天市場",
            "yh":"Yahoo!",
            "st":"STORE",
            "mn":""
            }
        return customerList

    # 取引先名を取得
    def getCustomerName(self):
        customerList = self.getCustomerList()
        customer = customerList[self.appName]
        return customer
    
    # insert
    def insertOrderManagementAPP(self):
        print(appDataList[0])
        account = pykintone.load("test.yml")


        
        app = account.app()
        record = Kintone()
        record.channel = "test6"
        record.customer = "test7"
        try:
            app.create(record)
        except Exception:
            texta = "{}:受注管理表の更新に失敗\n"
            dt = datetime.datetime.now()
            with open("log.txt", "a") as fileobj:
                text = texta.format(dt)   
                fileobj.write(text)

pr = Kintone()
# 引数取得
arg = sys.argv
pr.appName = arg[1]
# データ取得
appDataList = pr.appDataget()
customer = pr.getCustomerName()

#insert
pr.insertOrderManagementAPP()
print('End')
#print("{}".format(json.dumps(appDataList[0],indent=4)))
#print(appDataList[0])

#print(appName)
#print("{}".format(json.dumps(appDataList[0],indent=4)))
#print(result[0]["rt_orderNumber"]["value"])