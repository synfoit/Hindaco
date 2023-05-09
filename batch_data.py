import time
import serial
import codecs
from datetime import datetime
from threading import Thread

from model import BatchModel
class SerialData(Thread):
    def Convert(self,string):
        li = list(string.split(","))
        return li

    def ReadData(self):
        ser = serial.Serial(
            port='COM4',
            baudrate=9600,
            timeout=1,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.SEVENBITS
        )
        ser.isOpen()
        while True:
            # configure the serial connections (the parameters differs on the device you are connecting to)

            # Reading the data from the serial port. This will be running in an infinite loop.
            bytesToRead = ser.inWaiting()
            data = ser.read(bytesToRead)
            print(data)
            print(bytesToRead)
            # bytesToRead=b'S2,BCNT  9,G  95,T  5,N  90,Tot  2455!SIDB,START*\n\r'
            if (bytesToRead > 0):
                d=codecs.decode(data, 'UTF-8')
                dataInString=str(d)
                print(len(dataInString))

                if(len(dataInString)>=40):
                    print("data")
                    now = datetime.now()
                    dataList=self.Convert(dataInString)
                    Batch_ID=dataList[0]
                    Batch = dataList[1].replace('BCNT','')
                    TareWeigh = dataList[3].replace('T','')
                    GrossWeight = dataList[2].replace('G','')
                    NetWeight = dataList[4].replace('N','')
                    ShipTotal=''
                    if(Batch_ID=='S2'):
                        ShipTotal = dataList[5].replace('Tot','').replace('!SIDB','')
                        BatchModel().insert(Batch_ID, Batch, TareWeigh, GrossWeight, NetWeight, ShipTotal, now)
                        print(ShipTotal)
                    if (Batch_ID == 'S1'):
                        ShipTotal = dataList[5].replace('Tot', '').replace('!SIDA', '')
                        BatchModel().insert(Batch_ID, Batch, TareWeigh, GrossWeight, NetWeight, ShipTotal, now)
                        print(ShipTotal)

                    # print(Batch_ID)
                    # print(Batch)
                    # print(TareWeigh)
                    # print(GrossWeight)
                    # print(NetWeight)




            time.sleep(1)

            # print(bytesToRead)
            # print(data)

    def run(self) -> None:
        sd=SerialData()
        sd.ReadData()
        time.sleep(1)

