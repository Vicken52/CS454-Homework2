from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRegistration(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getInt32()

            print "ResponseRegistration - ", self.msg

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_REGISTER) + '] String Response')
            print_exc()