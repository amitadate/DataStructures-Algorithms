def toh(disks,stpeg,endpeg):
    if disks:
        toh(disks-1,stpeg,6-stpeg-endpeg)
        print "Move disk %d from peg %d to peg %d\n"%(disks,stpeg,endpeg)
        toh(disks-1,6-stpeg-endpeg,endpeg)


toh(4,1,3)
