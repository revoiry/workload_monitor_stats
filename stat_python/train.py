from stat_output import Stat_outfile
from sklearn import svm

class Trainning():
    def get_data(self):
        st = Stat_outfile()
        train_dict=st.read_from_file("outfile","/lustre1/ior-test-file.")
        #print train_dict


t=Trainning()
t.get_data()
