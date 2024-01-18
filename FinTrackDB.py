from FinTrackDBEntry import FinTrackDBEntry

class FinTrackDB:
    """
    - simple database to store FinDBEntry objects
    """    

    def __init__(self, init=False, dbName='FinDB.csv'):
        """
        - initialize database variables here
        - mandatory :
            - any type can be used to store database entries for FinDBEntry objects
            - e.g. list of class, list of dictionary, list of tuples, dictionary of tuples etc.
        """
        # CSV filename         
        self.dbName = dbName
        # initialize container of database entries 
        print('TODO: __init__')


    def fetch_statements(self):
        """
        - returns a list of tuples containing entry entry fields
        - example
          [('1','230101', 'Earning', 'Passive Income', '=', 'Cash', '1000'),
           ('2','230202', 'Expense', '=', 'Grocery', 'Cheque',  '400'),
           ('3','230303', 'Expense', '=', 'Utility Bills', 'GCash',  '3000')]
        """
        tupleList = [('1','230101', 'Earning', 'Passive Income', '=', 'Cash', '1000'),
                     ('2','230202', 'Expense', '=', 'Grocery', 'Cheque',  '400'),
                     ('3','230303', 'Expense', '=', 'Utility Bills', 'GCash',  '3000')]
        
        return tupleList
        
    def insert_statement(self, id, date, cf_type, earning, expense, paymode, amount):
        """
        - inserts an entry in the database
        - no return value
        """
        newEntry = FinTrackDBEntry(id=id, date=date, cf_type=cf_type, earning=earning, expense=expense, paymode=paymode, amount=amount)
        print('TODO: insert_entry')

    def delete_statement(self, id):
        """
        - deletes the corresponding entry in the database as specified by 'date'
        - no return value
        """
        print('TODO: delete_entry')

    def update_statement(self, new_date, new_cf_type, new_earning, new_expense, new_paymode, new_amount, id):
        """
        - updates the corresponding entry in the database as specified by 'ID'
        - no return value
        """
        print('TODO: update_entry')

    def update_statementID(self, new_id, date):
        """
        - updates the corresponding entry in the database as specified by 'date'
        - no return value
        """
        print('TODO: update_entry')

    def export_csv(self):
        """
        - exports database entries as a CSV file
        - CSV : Comma Separated Values
        - no return value
        - example
        230101,Earning,Passive Income,=,Cash,1000
        230202,Expense,=,Grocery,Cheque,400
        230303,Expense,=,Utility Bills,GCash,3000      
        """
        print('TODO: export_csv')

    def export_json(self):
        """
        - exports database entries as a JSON file    
        """
        print('TODO: export_json')

    def id_exists(self, id):
        """
        - returns True if an entry exists for the specified 'date'
        - else returns False
        """
        return False
