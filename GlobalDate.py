"""
TEST
no further test , please notice me if error occured.
See below to find useage.
"""
__author__ = 'septem'

from datetime import datetime
from datetime import timedelta

class GlobalDate(object):
    #here you keep your DICT of timezone infomation
    _tzDict = {"Landon":0,"Beijing":8,"Tokyo":9}

    def __init__(self,year=2000,month=1,day=1,hour=0,minute=0,second=0,tz=0,now=False):
        ltz = self.getTzHour(tz)
        if ltz==None:
            if isinstance(tz,int) and tz<=12 and tz>-12:
                ltz = tz
            else:
                ltz = 0
        if now==True:
            self.dt = datetime.now()
            self.tz = ltz
        else :
            self.dt = datetime(year,month,day,hour,minute,second)
            self.tz = ltz
    def getTimeUTC(self):
        result = self.dt - timedelta(hours=self.tz)
        return result
    def getTime(self,tz=None):
        ltz = self.getTzHour(tz)
        if ltz==None:
            if isinstance(tz,int) and tz<=12 and tz>-12:
                ltz = tz
            else:
                ltz = None
        tdelta = 0
        if ltz != None:
            tdelta = ltz-self.tz
        result = self.dt + timedelta(hours=tdelta)
        return result
    def getTzName(self,tz=0):
        pass
    def getTzHour(self,tzname='Landon'):
        #if no found,return None
        return self._tzDict.get(tzname,None)

def test():
    gtBJ = GlobalDate(2010,1,1,10,0,0,'Beijing')
    print('local time: ',gtBJ.getTime())
    print('utc time: ',gtBJ.getTimeUTC())
    print('another city\'s time: ',gtBJ.getTime(1))
    '''
    First create a GlobalDate by passing attributes to it,like 5 lines above.
    you can use gt.getTime() to get timeinfo according to the time and timezone
    like this:
       gt.getTime('Landon')  //city name
       gt.getTime(-2)        //timezone hour code
       gt.getTime()          //no attribute
    '''

if __name__ == '__main__':
    test()