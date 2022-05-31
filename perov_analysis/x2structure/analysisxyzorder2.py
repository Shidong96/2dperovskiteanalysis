#! /usr/bin/env python
import numpy as np
import os
import sys
import math

class analysis():
    def _init_(self):
        self.path = os.getcwd()
    def getcoord(self, inf):
        """
        This part gets the cartesian coordinates of needed atoms
        """
        poscar = open(inf,'r')
        poscar.readline()
        poscar.readline()
        string = poscar.readline()
        a = float(string.split()[0])
        string = poscar.readline()
        b = float(string.split()[1])
        string = poscar.readline()
        c = float(string.split()[2])
        poscar.readline()
        string = poscar.readline()
        numI = int(string.split()[0])
        numPb = int(string.split()[1])
        numC = int(string.split()[2])
        numH = int(string.split()[3])
        numN = int(string.split()[4])
        poscar.readline()
        coordC = []
        coordI = []
        coordN = []
        coordPb = []
        extraI = []
        extraC = []
        for i in xrange(0, numI):
            string = poscar.readline()
            temp = string.split()
            temp[0] = float(temp[0])
            temp[1] = float(temp[1])
            temp[2] = float(temp[2])
            coordI.append([temp[0]*a,temp[1]*b,temp[2]*c])
            extraI.append([temp[0]*a,temp[1]*b,temp[2]*c])
            for n in (0,1,2):
                #if temp[n]>0.85 or temp[n]<0.15:
                    extraI.append([(temp[0]-1)*a,temp[1]*b,temp[2]*c])
                    extraI.append([(temp[0]+1)*a,temp[1]*b,temp[2]*c])
                    extraI.append([temp[0]*a,(temp[1]-1)*b,temp[2]*c])
                    extraI.append([temp[0]*a,(temp[1]+1)*b,temp[2]*c])
                    extraI.append([temp[0]*a,temp[1]*b,(temp[2]-1)*c])
                    extraI.append([temp[0]*a,temp[1]*b,(temp[2]+1)*c])
                    extraI.append([(temp[0]+1)*a,(temp[1]+1)*b,temp[2]*c])
                    extraI.append([(temp[0]+1)*a,(temp[1]-1)*b,temp[2]*c])
                    extraI.append([(temp[0]-1)*a,(temp[1]+1)*b,temp[2]*c])
                    extraI.append([(temp[0]-1)*a,(temp[1]-1)*b,temp[2]*c])
                    extraI.append([temp[0]*a,(temp[1]+1)*b,(temp[2]+1)*c])
                    extraI.append([temp[0]*a,(temp[1]+1)*b,(temp[2]-1)*c])
                    extraI.append([temp[0]*a,(temp[1]-1)*b,(temp[2]+1)*c])
                    extraI.append([temp[0]*a,(temp[1]-1)*b,(temp[2]-1)*c])
                    extraI.append([(temp[0]+1)*a,temp[1]*b,(temp[2]+1)*c])
                    extraI.append([(temp[0]+1)*a,temp[1]*b,(temp[2]-1)*c])
                    extraI.append([(temp[0]-1)*a,temp[1]*b,(temp[2]+1)*c])
                    extraI.append([(temp[0]-1)*a,temp[1]*b,(temp[2]-1)*c])
                    extraI.append([(temp[0]+1)*a,(temp[1]+1)*b,(temp[2]+1)*c])
                    extraI.append([(temp[0]+1)*a,(temp[1]+1)*b,(temp[2]-1)*c])
                    extraI.append([(temp[0]+1)*a,(temp[1]-1)*b,(temp[2]+1)*c])
                    extraI.append([(temp[0]+1)*a,(temp[1]-1)*b,(temp[2]-1)*c])
                    extraI.append([(temp[0]-1)*a,(temp[1]+1)*b,(temp[2]+1)*c])
                    extraI.append([(temp[0]-1)*a,(temp[1]+1)*b,(temp[2]-1)*c])
                    extraI.append([(temp[0]-1)*a,(temp[1]-1)*b,(temp[2]+1)*c])
                    extraI.append([(temp[0]-1)*a,(temp[1]-1)*b,(temp[2]-1)*c])
                    break
            #if temp[0]>float(0.8):
            #    extraI.append([(temp[0]-1)*a,temp[1]*b,temp[2]*c])
            #    #print temp
            #elif temp[0]<float(0.2):
            #    extraI.append([(temp[0]+1)*a,temp[1]*b,temp[2]*c])
            #    #print temp
            #if temp[1]>float(0.8):
            #    extraI.append([temp[0]*a,(temp[1]-1)*b,temp[2]*c])
            #    #print temp
            #elif temp[1]<float(0.2):
            #    extraI.append([temp[0]*a,(temp[1]+1)*b,temp[2]*c])
            #    #print temp
            #if temp[2]>float(0.8):
            #    extraI.append([temp[0]*a,temp[1]*b,(temp[2]-1)*c])
            #    #print temp
            #elif temp[2]<float(0.2):
            #    extraI.append([temp[0]*a,temp[1]*b,(temp[2]+1)*c])
                #print temp
        #print len(extraI)

        for i in xrange(0, numPb):
            string = poscar.readline()
            temp = string.split()
            temp[0] = float(temp[0])*a
            temp[1] = float(temp[1])*b
            temp[2] = float(temp[2])*c
            coordPb.append([temp[0],temp[1],temp[2]])

        for i in xrange(0, numC):
            string = poscar.readline()
            temp = string.split()
            temp[0] = float(temp[0])
            temp[1] = float(temp[1])
            temp[2] = float(temp[2])
            coordC.append([temp[0]*a,temp[1]*b,temp[2]*c])
            extraC.append([temp[0]*a,temp[1]*b,temp[2]*c])
            extraC.append([(temp[0]-1)*a,temp[1]*b,temp[2]*c])
            extraC.append([(temp[0]+1)*a,temp[1]*b,temp[2]*c])
            extraC.append([temp[0]*a,(temp[1]-1)*b,temp[2]*c])
            extraC.append([temp[0]*a,(temp[1]+1)*b,temp[2]*c])
            extraC.append([(temp[0]+1)*a,(temp[1]+1)*b,temp[2]*c])
            extraC.append([(temp[0]+1)*a,(temp[1]-1)*b,temp[2]*c])
            extraC.append([(temp[0]-1)*a,(temp[1]+1)*b,temp[2]*c])
            extraC.append([(temp[0]-1)*a,(temp[1]-1)*b,temp[2]*c])
        for i in xrange(0, numH):
            poscar.readline()


        for i in xrange(0, numN):
            string = poscar.readline()
            temp = string.split()
            temp[0] = float(temp[0])*a
            temp[1] = float(temp[1])*b
            temp[2] = float(temp[2])*c
            coordN.append([temp[0],temp[1],temp[2]])

        #print len(extraC)
        return extraC, coordI, coordN, coordPb, extraI, numN, numPb
    
    
    def distance(self, a, b):
        return np.sqrt(np.square(a[0]-b[0])+np.square(a[1]-b[1])+np.square(a[2]-b[2]))
    
    def MA(self, C, N):
        """
        This part gets the vector of MA cations and the two angles
        """
        #print C
        #print N
        vector = []
        anglez = []
        anglexy = []
        temp = []
        error = 0
        avrgx=0
	avrgy=0
	avrgz=0
	avrg = []
	for n in N:
            #print n
            control = 0
            for c in C:
                #print c
                #print n
                if self.distance(c,n)<1.6 :
                    temp.append([c,n])
                    #print temp
                    vector.append([n[0]-c[0],n[1]-c[1],n[2]-c[2]])
                    control = control+1
            if control  != 1:
                error=error+1
                print "ERROR! C-N wrong match!"
                print temp
        if error>0:
            print "Number of errors in MA:  "+str(error)
#        else:print('MA job done, no error.')
        for v in vector:
            anglez.append(180*math.acos(sum((a*b) for a, b in zip(v, [0,0,1]))/math.sqrt(sum(i**2 for i in v)))/math.pi)
        for v in vector:
            if sum((a*b)for a,b in zip(v,[0,1,0]))>0:
                anglexy.append(180*math.acos(sum((a*b) for a, b in zip(v, [1,0,0]))/math.sqrt(sum(i**2 for i in v)))/math.pi)
            else: 
                anglexy.append(360-180*math.acos(sum((a*b) for a, b in zip(v, [1,0,0]))/math.sqrt(sum(i**2 for i in v)))/math.pi)
        for v in vector:
	    avrgx +=v[0]
	    avrgy +=v[1]
	    avrgz +=v[2]
	avrg = [avrgx,avrgy,avrgz]
	return vector, anglez, anglexy, avrg

    def excursion(self, Pb, I1, I2):
        """
        This part gives the distance between the Pb atom and the line formed by the two Iodine atoms
        """
        vI = [I2[0]-I1[0], I2[1]-I1[1], I2[2]-I2[2]]
        vPb = [Pb[0]-I1[0], Pb[1]-I1[1], Pb[2]-I1[2]]
        v = [vI[1]*vPb[2]-vI[2]*vPb[1],vI[2]*vPb[0]-vI[0]*vPb[2],vI[0]*vPb[1]-vI[1]*vPb[0]]
        excursion = math.sqrt(sum(i**2 for i in v))/self.distance(I1,I2)/self.distance(Pb,I1)
        return excursion

    def bondangle(self, pb, i1, i2):
        '''
        This part gives the bond angle of two iodine and a lead atom
        '''
        v1 = [i1[0]-pb[0], i1[1]-pb[1], i1[2]-pb[2]]
        v2 = [i2[0]-pb[0], i2[1]-pb[1], i2[2]-pb[2]]
        return 180*math.acos(sum((a*b) for a, b in zip(v1,v2))/math.sqrt(sum(i**2 for i in v1))/math.sqrt(sum(i**2 for i in v2)))/math.pi

    def octahedron(self, Pb, I):
        """
        This part finds the 6 I atoms in vicinity of every Pb atom, and calculate the mass center of the distorted octahedron, then find the excursion vector.
        """
        excursion = []
        dbond = []
        dangle = []
	danglex = []
	dangley = []
	danglez = []
        error = 0
        for pb in Pb:
            distance = []
            num = 0
            temp = []
            massc = [0,0,0]
            control = 0
            for i in I:
                if self.distance(pb,i)<4.5:
                    temp.append(i)
                    control = control+1
            if control != 6:
                if control >10:
                    print control
                    print pb,temp
                    error = error+1
                print "ERROR! Pb-I wrong match!"
                print control
                print pb,temp
                error = error+1
            x1 = sorted(temp, key = lambda s:s[0])[0]
            x2 = sorted(temp, key = lambda s:s[0])[5]
            y1 = sorted(temp, key = lambda s:s[1])[0]
            y2 = sorted(temp, key = lambda s:s[1])[5]
            z1 = sorted(temp, key = lambda s:s[2])[0]
            z2 = sorted(temp, key = lambda s:s[2])[5]
            dbond.append(sum(abs(self.distance(i,pb)-3.16) for i in temp)/6)
            #dangle.append((360-self.bondangle(pb,x1,x2)-self.bondangle(pb,y1,y2))/2)
            dangle.append((540-self.bondangle(pb,x1,x2)-self.bondangle(pb,y1,y2)-self.bondangle(pb,z1,z2))/3)
	    danglex.append(180-self.bondangle(pb,x1,x2))
	    dangley.append(180-self.bondangle(pb,y1,y2))
	    danglez.append(180-self.bondangle(pb,z1,z2))
        averagedbond = sum(i for i in dbond)/len(dbond)
        averagedangle = sum(i for i in dangle)/len(dangle)
        averagedanglexyz = [sum(i for i in danglex)/len(danglex),sum(i for i in dangley)/len(dangley),sum(i for i in danglez)/len(danglez)]
#	print 'average delta bond length(3.16):', averagedbond
#        print 'average delta angle:', averagedangle
	print 'average delta angle per xyz', averagedanglexyz
#        print 'delta angle per octahedron:', dangle
        return excursion
#            massc[0] = float(np.sum(x[0] for x in temp)/6)
#            massc[1] = float(np.sum(x[1] for x in temp)/6)
#            massc[2] = float(np.sum(x[2] for x in temp)/6)
#            vector.append([pb[0]-massc[0],pb[1]-massc[1],pb[2]-massc[2]])
#        for i in vector:
#            length.append(math.sqrt(sum(o**2 for o in i)))
#        if error>0:
#            print 'Number of error in Pb:  '+str(error)
#        else:
#            print "Pb job done, no error."
#            print 'average excursion: ',float(sum(length))/len(length)
#        return vector,length


a = analysis()
infile = sys.argv[1]
C,I,N,Pb,extra,numN,numPb = a.getcoord(infile)
a.octahedron(Pb,extra)
vectorMA, anglez, anglexy, avrgv = a.MA(C,N)
#print 'Sum of MA vectors:', avrgv, 'lenvector:', math.sqrt(sum(o**2 for o in avrgv))

#vectorPb,length = a.octahedron(Pb,extra)
#MA = open("MAinfo-"+str(infile),'w')
#for i in xrange(0,numN-2):
#    string = 'vector:'+"{0:70}".format(vectorMA[i])+'anglez:'+"{0:20}".format(anglez[i])+'   anglexy:'+"{0:20}".format(anglexy[i])+'\n'
#    MA.write(string)
#octahedron = open("Pbinfo-"+str(infile),'w')
#for i in xrange(0,numPb):
#    string = 'vector'+"{0:70}".format(vectorPb[i])+'   excursion length:'+"{0:20}".format(length[i])+'\n'
#    octahedron.write(string)
#MA.close()
#octahedron.close()
