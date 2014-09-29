class Stat_outfile():

    def read_from_file(self,outfile,testfile):
        train_data={}
        file = open(outfile)
        file_read = {}
        file_write = {}
        file_dtime = {}
        file_offset = {}
        del_offset = {}

        for line in file:
            data = line.split()
            if len(data)<1:
                if(len(file_read)+len(file_write)>0):
                    dataset={}
                    print 'in last two seconds:'
                    if(file_read!={}):
                        res=self.compute_stat(file_read)
                        print 'read,avg,var      ',res
                        for k in res:
                            if k in dataset:
                                dataset[k].extend(res[k])
                            else:
                                dataset[k]=res[k]
                        #print dataset
                    if(file_write!={}):
                        res=self.compute_stat(file_write)
                        print 'write,avg,var     ',res
                        for k in res:
                            if k in dataset:
                                dataset[k].extend(res[k])
                            else:
                                dataset[k]=res[k]
                        #print dataset
                    if(file_dtime!={}):
                        res=self.compute_stat(file_dtime)
                        print 'dtime,avg,var     ',res
                        for k in res:
                            if k in dataset:
                                dataset[k].extend(res[k][1:])
                            else:
                                dataset[k]=res[k]
                        #print dataset
                    if(file_offset!={}):
                        res=self.compute_stat(file_offset)
                        print 'offset,avg,var    ',res
                        for k in res:
                            if k in dataset:
                                dataset[k].extend(res[k][1:])
                            else:
                                dataset[k]=testFile.res[k]
                        #print dataset
                    if(del_offset!={}):
                        res=self.compute_stat(del_offset)
                        print 'del_offset,avg,var',res
                        for k in res:
                            if k in dataset:
                                dataset[k].extend(res[k][1:])
                            else:
                                dataset[k]=res[k]
                        #print dataset
                    for k in dataset:
                        if k in train_data:
                            train_data[k].append(dataset[k])
                        else:
                            train_data[k]=[]
                            train_data[k].append(dataset[k])
                    file_read = {}
                    file_write = {}
                    file_dtime = {}
                    file_offset = {}
                    del_offset = {}
            else:
                # print data[0]
                #print data[7]
                if(testfile in data[3]):
                    data[3]=data[3][len(testfile):len(data[3])]
                else:
                    continue
                if data[0]=='R':
                    if data[3] in file_read:
                        file_read[data[3]].append(int(data[4]))
                    else:
                        values = []
                        values.append(int(data[4]))
                        file_read[data[3]]=values
                else:
                    if data[3] in file_write:
                        file_write[data[3]].append(int(data[4]))
                    else:
                        values = []
                        values.append(int(data[4]))
                        file_write[data[3]]=values
                #add delta time to the dict
                if data[3] in file_dtime:
                        file_dtime[data[3]].append(int(data[5]))
                else:
                    values = []
                    values.append(int(data[5]))
                    file_dtime[data[3]]=values
                #add offset to the dict
                if data[3] in file_offset:
                        file_offset[data[3]].append(int(data[7]))
                else:
                    values = []
                    values.append(int(data[7]))
                    file_offset[data[3]]=values

            for key in file_offset.keys():
                d_offs=[]
                pre=0
                for i in range(len(file_offset[key])):
                    d_offs.append(abs(file_offset[key][i]-pre))
                    pre=file_offset[key][i]
                del_offset[key]=d_offs
        return train_data

    def compute_stat(self,dic):
        res_dic={}
        for key in dic.keys():
            data=dic[key]
            res=[]
            average=sum(data) / len(data)
            res.append(len(data))
            res.append(average)
            res.append(sum((average - value) ** 2 for value in data) / len(data))
            res_dic[key]=res
        return res_dic


print Stat_outfile().read_from_file("outfile2","/lustre1/ior-test-file.")


