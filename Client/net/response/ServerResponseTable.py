from common.Constants import Constants

from net.response.ResponseRandomInt import ResponseRandomInt
from net.response.ResponseRandomString import ResponseRandomString
from net.response.ResponseRandomShort import ResponseRandomShort
from net.response.ResponseRandomFloat import ResponseRandomFloat
from net.response.ResponseLogin import ResponseLogin
from net.response.ResponseLogout import ResponseLogout
from net.response.ResponseRegistration import ResponseRegistration
from net.response.ResponseChat import ResponseChat
from net.response.ResponseMove import ResponseMove
from net.response.ResponseHeartbeat import ResponseHeartbeat
from net.response.ResponseExitGame import ResponseExitGame
from net.response.ResponseCreateCharacter import ResponseCreateCharacter



class ServerResponseTable:
    """
    The ServerResponseTable contains a mapping of all responses for use
    with the networking component.
    """
    responseTable = {}

    def __init__(self):
        """Initialize the response table."""
        self.add(Constants.RAND_INT, 'ResponseRandomInt')
        self.add(Constants.RAND_STRING, 'ResponseRandomString')
        self.add(Constants.RAND_SHORT, 'ResponseRandomShort')
        self.add(Constants.RAND_FLOAT, 'ResponseRandomFloat')
        self.add(Constants.SMSG_AUTH, 'ResponseLogin')
        self.add(Constants.SMSG_CREATE_CHARACTER,'ResponseCreateCharacter')
        self.add(Constants.SMSG_DISCONNECT, 'ResponseLogout')
        self.add(Constants.SMSG_REGISTER, 'ResponseRegistration')
        self.add(Constants.SMSG_CHAT, 'ResponseChat')
        self.add(Constants.SMSG_MOVE, 'ResponseMove')
        # self.add(Constants.REQ_HEARTBEAT, 'ResponseHeartbeat')
        self.add(Constants.SMSG_SAVE_EXIT_GAME, 'ResponseExitGame')

    def add(self, constant, name):
        """Map a numeric response code with the name of an existing response module."""
        if name in globals():
            self.responseTable[constant] = name
        else:
            print 'Add Response Error: No module named ' + str(name)

    def get(self, responseCode):
        """Retrieve an instance of the corresponding response."""
        serverResponse = None

        if responseCode in self.responseTable:
            serverResponse = globals()[self.responseTable[responseCode]]()
        else:
            print 'Bad Response Code: ' + str(responseCode)

        return serverResponse
