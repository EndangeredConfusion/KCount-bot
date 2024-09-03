class JsonModel:
    serverID: str
    counting: bool

    def __init__(self, serverID: str, counting: bool):
        self.serverID = serverID
        self.counting = counting
