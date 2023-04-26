class Transaction:

    def __init__(self):
        self.__id: int = 0
        self.__amount: float = 0.00
        self.__transaction_type = None
        self.__sender_name = None

    def set_id(self, identity_number: int):
        self.__id = identity_number

    def get_id(self) -> int:
        return self.__id

    def set_amount(self, amount: float):
        self.__amount = amount

    def get_amount(self) -> float:
        return self.__amount

    def set_transfer_type(self, transaction_type: str):
        self.__transaction_type = transaction_type

    def get_transaction_type(self, identity_number) -> str:
        return self.__transaction_type

    def set_senders_name(self, senders_name: str):
        self.__sender_name = senders_name

    def get_senders_name(self) -> str:
        return self.__sender_name

    def __str__(self):
        return f"""   
            Id: {self.__id}
            Amount: {self.__amount}
            Transaction Type: {self.__transaction_type}
            Sender's Name: {self.__sender_name}"""
