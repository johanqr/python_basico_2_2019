import time
 
def printBorder(): print '--' * 45
def cls(): print "\n\r" * 80
#----------------------------------------------------------------
 
# Status of a cluster on all nodes in the cell
#----------------------------------------------------------------
def clusterStatus(Cluster):
 state = AdminControl.getAttribute(Cluster, "state" )
 statelist=['stopped', 'partial.stopped', 'running', 'partial.start']
 for s in statelist :
  if state.endswith(s): 
   return s
  
def startCluster(cell, Cluster):
 state = AdminControl.getAttribute(Cluster, 'state')
 printBorder()
 if (state == 'websphere.cluster.running'):
  print "Cluster is running\nRipple starting cluster ............."
  print AdminControl.invoke(Cluster ,'rippleStart')
 else:
  print "Starting cluster ............... "
  print AdminControl.invoke(Cluster ,'start')
 printBorder()
 time.sleep(30)  # waiting time in seconds you can change it according to your needs
   
def stopCluster(cell, Cluster):
 state = AdminControl.getAttribute(Cluster, 'state')
 if (state == 'websphere.cluster.running') or (state == 'websphere.cluster.partial.start'):
  print AdminControl.invoke(Cluster ,'stop')
  time.sleep(30)
 else:
  print "Cluster cannot stopped"
 printBorder()
  
#  Main program   
cls()
cellName=AdminControl.getCell()
cluster='GW_CLUSTER'
clusterObj = AdminControl.completeObjectName('cell='+ cellName +',type=Cluster,name='+ cluster +',*')
 
while 1:
 ch=1
 if ch == 1:
  print cluster, " state is ", clusterStatus(clusterObj)
  break

