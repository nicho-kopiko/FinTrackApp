'''
This is the interface to an SQLite Database
'''

import sqlite3

class FinTrackDBSQ:
    def __init__(self, dbName='statements.db'):
        super().__init__()
        self.dbName = dbName
        self.csvFile = self.dbName.replace('.db', '.csv')
        self.jsonFile = self.dbName.replace('.db', '.json')
        self.conn = sqlite3.connect(self.dbName)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS statements (
                id TEXT PRIMARY KEY,
                date TEXT,
                cf_type TEXT,
                earning TEXT,
                expense TEXT,
                paymode TEXT,
                amount TEXT)''')
        self.conn.commit()
        self.conn.close()

# === CURSOR FUNCTIONS ====================================
    def connect_cursor(self):
        self.conn = sqlite3.connect(self.dbName)
        self.cursor = self.conn.cursor()        

    def commit_close(self):
        self.conn.commit()
        self.conn.close()        

# === CREATE TABLE ====================================
    def create_table(self):
        self.connect_cursor()
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS statements (
                    id TEXT PRIMARY KEY,
                    date TEXT,
                    cf_type TEXT,
                    earning TEXT,
                    expense TEXT,
                    paymode TEXT,
                    amount TEXT)''')
        self.commit_close()

# === STATEMENT ACTIONS ====================================
    
    # FETCH
    def fetch_statements(self):
        self.connect_cursor()
        self.cursor.execute('SELECT * FROM statements')
        statements = self.cursor.fetchall()
        self.conn.close()
        return statements
    
    # INSERT
    def insert_statement(self, id, date, cf_type, earning, expense, paymode, amount):
        self.connect_cursor()
        self.cursor.execute('INSERT INTO statements (id, date, cf_type, earning, expense, paymode, amount) VALUES (?, ?, ?, ?, ?, ?, ?)',
                    (id, date, cf_type, earning, expense, paymode, amount))
        self.commit_close()

    # DELETE
    def delete_statement(self, id):
        self.connect_cursor()
        self.cursor.execute('DELETE FROM statements WHERE id = ?', (id,))
        self.commit_close()
    
    # UPDATES
    def update_statement(self, new_date, new_cf_type, new_earning, new_expense, new_paymode, new_amount, id):
        self.connect_cursor()
        self.cursor.execute('UPDATE statements SET date = ?, cf_type = ?, earning = ?, expense = ?, paymode = ?, amount = ? WHERE id = ?',
                    (new_date, new_cf_type, new_earning, new_expense, new_paymode, new_amount, id))
        self.commit_close()

    def update_statementID(self, new_id, date):
        self.connect_cursor()
        self.cursor.execute('UPDATE statements SET id = ? WHERE  date = ?',
                    (new_id, date))
        self.commit_close()

    # UNIQUE ID VERIFY
    def id_exists(self, id):
        self.connect_cursor()
        self.cursor.execute('SELECT COUNT(*) FROM statements WHERE id = ?', (id,))
        result =self.cursor.fetchone()
        self.conn.close()
        return result[0] > 0

# === EXPORT FUNCTIONS ====================================
    def export_csv(self):
        with open(self.csvFile, "w") as filehandle:
            dbEntries = self.fetch_statements()
            for entry in dbEntries:
                print(entry)
                filehandle.write(f"{entry[0]},{entry[1]},{entry[2]},{entry[3]},{entry[4]},{entry[5]},{entry[6]}\n")

    def export_json(self):
        with open(self.jsonFile, "w") as filehandle:
            dbEntries = self.fetch_statements()
            for entry in dbEntries:
                print(entry)
                filehandle.write(f"{entry[0]},{entry[1]},{entry[2]},{entry[3]},{entry[4]},{entry[5]},{entry[6]}\n")


def test_FinTrackDB():
    iFinTrackDB = FinTrackDBSQ(dbName='FinTrackDB.db')

    for entry in range(30):
        iFinTrackDB.insert_statement(entry, f'1', f'230101', 'Earning', 'Salary (Work)', '=', 'Cash', f'1000')
        assert iFinTrackDB.id_exists(entry)

    all_entries = iFinTrackDB.fetch_statements()
    assert len(all_entries) == 30

    for entry in range(10, 20):
        iFinTrackDB.update_statement(entry, f'1', f'230101', 'Earning', 'Salary (Work)', '=', 'Cash', f'1000', entry)
        assert iFinTrackDB.id_exists(entry)

    all_entries = iFinTrackDB.fetch_statements()
    assert len(all_entries) == 30

    for entry in range(10):
        iFinTrackDB.delete_statement(entry)
        assert not iFinTrackDB.id_exists(entry) 

    all_entries = iFinTrackDB.fetch_statements()
    assert len(all_entries) == 20