class Customer:
    def __init__(self):
        self.transaction_log = []

    def log_transaction(self, transaction):
        self.transaction_log.append(transaction)

    def view_transaction_log(self):
        print("Transaction Log:")
        for transaction in self.transaction_log:
            print(transaction)