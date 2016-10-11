#http://cuiqingcai.com/1001.html
import re

class CleanTool:
    #replace for \n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #replace for \t
    replaceTD= re.compile('<td>')
    #replace for \n
    replaceBR = re.compile('<br><br>|<br>')
    #delete other tags
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        return x
