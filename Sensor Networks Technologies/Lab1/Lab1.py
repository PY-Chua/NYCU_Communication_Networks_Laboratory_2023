# -*- coding: utf-8 -*-
import blescan
import bluetooth._bluetooth as bluez

import sys
import time
import math

# BLE
def init_ble():
    try:
        # open hci0 interface
        sock = bluez.hci_open_dev(0)
        print ("ble thread started")
    except:
        print ("error accessing bluetooth device...")
        sys.exit(1)

    blescan.hci_le_set_scan_parameters(sock)    
    blescan.hci_enable_le_scan(sock)            

    return sock

def ble_scan(sock):
    rssiDict = dict()   
    returnedList = blescan.parse_events(sock)

    for beacon in returnedList:
        raw_uuid = ""

        for word in beacon.uuid.split('-'):
            raw_uuid = raw_uuid + word

        if raw_uuid == "00000000000000000000000109511286":    # Change your uuid here
            print("--------")
            print("raw_uuid", raw_uuid)
            print("uuid:", beacon.uuid)
            print("major:", beacon.major, ", minor:", beacon.minor, ", txpower:", beacon.unknown)
            print("rssi", beacon.rssi)

            
            # 藉由 RSSI 和 txpower 來計算傳輸距離並 print 出結果
            # 此處會用到的變數
            #   1. beacon.rssi
            #   2. beacon.unknown
            #   前兩項變數為 string 型態，需用 float() 方式轉換成 float 型態才能進行運算
            #   python 中的指數運算為 ** example: 2**10 -> 2 的 10 次方
            ''' start of you code '''
            coef1, coef2, coef3 = 0.42093, 6.9476, 0.54992     # alpha, beta, gamma 
            ratio = float(beacon.rssi) / float(beacon.unknown)
            if ratio < 1:             # ratio < 1
                rssiDict = ratio**10
            else:            # ratio > 1
                rssiDict = coef1 * (ratio**coef2) + coef3

            ''' end of you code '''

    time.sleep(1)
    return rssiDict

def main():
    sock = init_ble()

    while True:
        rssiDict = ble_scan(sock)
        print("distance (m)", rssiDict)

if __name__ == "__main__":
    main()
