from stat import Stat_outfile

class Trainning():
    def get_data(self):
        st= Stat_outfile()
        print st.read_from_file("outfile","/lustre1/ior-test-file.")

Tr=Trainning()
Tr.get_data()
