# define Constants

class Constants:
    RAND_INT                            = 1
    RAND_STRING                         = 2
    RAND_SHORT                          = 3
    RAND_FLOAT                          = 4

    SERVER_IP = 'localhost'
    SERVER_PORT = 9252
    DEBUG = True
    MSG_NONE                            = 0
    CMSG_AUTH                           = 101
    CMSG_DISCONNECT                     = 102
    CMSG_REGISTER                       = 103
    CMSG_CREATE_CHARACTER               = 104
    CMSG_CHAT                           = 105
    CMSG_MOVE                           = 106
    CMSG_SAVE_EXIT_GAME                 = 119

    SMSG_AUTH                           = 201
    SMSG_DISCONNECT                     = 202
    SMSG_REGISTER                       = 203
    SMSG_CREATE_CHARACTER               = 204
    SMSG_CHAT                           = 205
    SMSG_MOVE                           = 206
    SMSG_SAVE_EXIT_GAME                 = 219

    REQ_HEARTBEAT                       = 301
