from config.dbconfig import dbCon
from helpers import helper


class DbDeal:
    cursor = dbCon.cursor()

    # constructor
    def __init__(self):
        # initializing db connection in constructor
        """ constructor """

    @classmethod
    def getSharesToDealWithSocket(cls):
        sql = "SELECT t.id, t.variety, t.script_name, t.exchange, t.trading_symbol, t.symbol_token, " \
              "t.angel_buy_threshold, t.angel_sell_threshold, t.valid_from, t.valid_to, " \
              "t1.symbol, t1.expiry_date, t1.is_fut, t1.strike, t1.is_CE, " \
              "t.angel_buy_stoploss, t.angel_sell_stoploss, t.buy_stoploss_modified_target, " \
              "t.sell_stoploss_modified_target " \
              "FROM script_master t " \
              "LEFT JOIN script_master_desc t1 ON t.id = t1.script_master_id " \
              "WHERE t.active = 'Y' AND " \
              "CURDATE() BETWEEN t.valid_from AND t.valid_to "
        # print(sql)
        cls.cursor.execute(sql)
        res = cls.cursor.fetchall()
        return res

    @classmethod
    def saveAccessToken(cls, userId, apiName, req, res, remark):
        try:

            sql = "INSERT INTO log_angel_broking_others(user_id, api_name, req_log, res_log, remarks) " \
                  "values (%s, %s, %s, %s, %s) "
            bindData = (userId, apiName, req, res, remark)
            cls.cursor.execute(sql, bindData)
            dbCon.commit()

        except Exception as e:
            print('Unable to insert accessToken!! ', helper.line_info())
            print(e)
            exit()
        finally:
            """ If needed to execute something """

    @classmethod
    def getUpdatedPriceAndThresholds(cls):
        sql = "SELECT t.symbol_token, t.angel_buy_threshold, t.angel_sell_threshold, " \
              "t.angel_buy_stoploss, t.angel_sell_stoploss, t.buy_stoploss_modified_target, " \
              "t.sell_stoploss_modified_target " \
              "FROM script_master t " \
              "WHERE t.active = 'Y' AND " \
              "CURDATE() BETWEEN t.valid_from AND t.valid_to "
        # print(sql)
        cls.cursor.execute(sql)
        res = cls.cursor.fetchall()
        return res
