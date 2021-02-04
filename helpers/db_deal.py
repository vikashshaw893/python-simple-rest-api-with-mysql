import json
import sys
import time

import MySQLdb
import pymysql

from config.dbconfig import MySql
from helpers import helper


class DbDeal:

    # constructor
    def __init__(self):
        # initializing db connection in constructor
        """ constructor """
        self.conn = MySql.connect()
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    # fetching all shares list to execute - currently unused method
    def getSharesToDealWithSocket(self):
        sql = "SELECT t.id, t.variety, t.script_name, t.exchange, t.trading_symbol, t.symbol_token, " \
              "t.angel_buy_threshold, t.angel_sell_threshold, t.valid_from, t.valid_to, " \
              "t1.symbol, t1.expiry_date, t1.is_fut, t1.strike, t1.is_CE " \
              "FROM script_master t " \
              "LEFT JOIN script_master_desc t1 ON t.id = t1.script_master_id " \
              "WHERE t.active = 'Y' AND " \
              "CURDATE() BETWEEN t.valid_from AND t.valid_to "
        # print(sql)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    # saving first socket data into database
    def saveFirstSocketOpeningData(self, req):
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO shares_interval_values (user_id, trading_symbol, symbol_token, exchange, price, " \
              "last_trading_time, req_log, res_log) values(%s, %s, %s, %s, %s, %s, %s, %s)"

        bindData = (1, json.dumps(req['instrument']), req['token'], req['exchange'],
                    req['ltp'], now, 'Req: SOCKET_DATA Opening', json.dumps(req))

        try:
            self.cursor.execute(sql, bindData)
            self.conn.commit()
            return True
        except:
            e = str(sys.exc_info())
            msg = 'Unable to save order record!! ' + helper.line_info() + ' :: ' + e
            print(msg)
            helper.logError(msg)
            return False

    # saving order details
    def saveOrderDetail(self, data):
        # print(data)
        # now = time.strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO daily_shares_orders(user_id, order_id, variety, trading_symbol, symbol_token, " \
              "transaction_type, exchange, order_type, product_type, price, quantity, req_log, res_log ) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

        bindData = (data['user_id'], data['order_id'], data['variety'], data['trading_symbol'], data['symbol_token'],
                    data['transaction_type'], data['exchange'], data['order_type'], data['product_type'],
                    data['price'], data['quantity'], json.dumps(data['req_log']), json.dumps(data['res_log']))

        try:
            self.cursor.execute(sql, bindData)
            self.conn.commit()
            return True
        except:
            e = str(sys.exc_info())
            msg = 'Unable to save order record!! ' + helper.line_info() + ' :: ' + e
            print(msg)
            helper.logError(msg)
            return False
