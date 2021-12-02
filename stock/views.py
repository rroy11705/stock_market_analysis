from rest_framework.decorators import api_view
from django.shortcuts import render
import requests
from django.db import connection
from rest_framework.response import Response
from rest_framework import status


#################################################################

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

#################################################################


@api_view(["GET"])
def stock_indicators(request, ticker):
    
    # ticker = 'LTI.NS'
        
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    
    try:
    
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&useYfid=true&range=ytd&corsDomain=finance.yahoo.com&.tsrc=finance"
        res = requests.get(url, headers=headers, timeout=5).json()

        result = res["chart"]["result"][0]
        
        query = "INSERT INTO stock_stockdetails (symbol, currency, instrument_type) VALUES ('{}', '{}', '{}');".format(result["meta"]["symbol"], result["meta"]["currency"], result["meta"]["instrumentType"])
        with connection.cursor() as cursor:
            cursor.execute(query)
            
        timestamps =  result["timestamp"]
        query = ""

        for i, timestamp in enumerate(timestamps):
            query += "INSERT INTO stock_stockopen (symbol_id, timestamp, value) VALUES ('{}', '{}', '{}');".format(result["meta"]["symbol"],
                                                                                                                        timestamp, result["indicators"]["quote"][0]["open"][i])                    
                
            query += "INSERT INTO stock_stockclose (symbol_id, timestamp, value) VALUES ('{}', '{}', '{}');".format(result["meta"]["symbol"],
                                                                                                            timestamp, result["indicators"]["quote"][0]["close"][i])

            query += "INSERT INTO stock_stockhigh (symbol_id, timestamp, value) VALUES ('{}', '{}', '{}');".format(result["meta"]["symbol"],
                                                                                                            timestamp, result["indicators"]["quote"][0]["high"][i])
                
            query += "INSERT INTO stock_stocklow (symbol_id, timestamp, value) VALUES ('{}', '{}', '{}');".format(result["meta"]["symbol"],
                                                                                                        timestamp, result["indicators"]["quote"][0]["low"][i])
                
            query += "INSERT INTO stock_stockvolume (symbol_id, timestamp, value) VALUES ('{}', '{}', '{}');".format(result["meta"]["symbol"],
                                                                                                            timestamp, result["indicators"]["quote"][0]["volume"][i])

        with connection.cursor() as cursor:
            cursor.execute(query)
                
                
            
        return Response({
            "status": "success"
        }, status=status.HTTP_200_OK)
        
    except:
        
        return Response({
            "status": "failure"
        }, status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(["GET"])
def get_details(request, ticker):

    # can be optimized using lag function ??
    
    query = f"SELECT " \
                "FROM_UNIXTIME(so.timestamp, '%Y-%m-%d') as date, " \
                "Round(sc.value, 2) as close, " \
                "so.value as open, " \
                f"Round((SELECT psc.value FROM stock_stockclose AS psc WHERE psc.symbol_id = '{ticker}' AND psc.timestamp < sc.timestamp ORDER BY psc.timestamp DESC LIMIT 1), 2) as prev_close,  " \
                f"Round((SELECT MAX(msc.value) FROM stock_stockclose AS msc WHERE msc.symbol_id = '{ticker}' AND DATEDIFF(FROM_UNIXTIME(sc.timestamp), FROM_UNIXTIME(msc.timestamp)) < 31 AND DATEDIFF(FROM_UNIXTIME(sc.timestamp), FROM_UNIXTIME(msc.timestamp)) > -1), 2) as 30_day_high, " \
                f"Round((SELECT MIN(msc.value) FROM stock_stockclose AS msc WHERE msc.symbol_id = '{ticker}' AND DATEDIFF(FROM_UNIXTIME(sc.timestamp), FROM_UNIXTIME(msc.timestamp)) < 31 AND DATEDIFF(FROM_UNIXTIME(sc.timestamp), FROM_UNIXTIME(msc.timestamp)) > -1), 2) as 30_day_low " \
            "FROM stock_stockclose as sc JOIN stock_stockopen as so ON sc.timestamp = so.timestamp " \
            f"WHERE sc.symbol_id = '{ticker}' " \
            "ORDER BY date DESC;"
    
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = dictfetchall(cursor)
    
    return Response({
        "result": result
    }, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_moving_average(request, ticker):
    
    # query = "SELECT FROM_UNIXTIME(a.timestamp) as date, Round(a.value, 2) as closing_value, Round((SELECT SUM(b.value) / COUNT(b.value) FROM stock_stockclose AS b WHERE DATEDIFF(FROM_UNIXTIME(a.timestamp), FROM_UNIXTIME(b.timestamp)) BETWEEN 0 AND 20), 2) AS 20_Day_Moving_Average " \
    #         "FROM stock_stockclose AS a " \
    #         f"WHERE a.symbol_id = '{ticker}' " \
    #         "ORDER BY a.timestamp ASC;"
            
    query = "SELECT " \
            "FROM_UNIXTIME(a.timestamp, '%Y-%m-%d') as date, " \
            "Round(a.value, 2) as closing_value, " \
            "Round((SELECT " \
                "CASE WHEN COUNT(b.value) > 19 THEN SUM(b.value) / COUNT(b.value) ELSE NULL END " \
                "FROM stock_stockclose AS b " \
                f"WHERE b.symbol_id = '{ticker}' AND a.timestamp > b.timestamp ORDER BY b.timestamp DESC), 2) AS 20_Day_Moving_Average " \
            "FROM stock_stockclose AS a " \
            f"WHERE a.symbol_id = '{ticker}' " \
            "ORDER BY a.timestamp ASC;"
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = dictfetchall(cursor)
    
    return Response({
        "result": result
    }, status=status.HTTP_200_OK)
    
    
