from FinTrackDBSQ import FinTrackDBSQ
from FinTrackGUI import FinTrackGUI

def main():
    db = FinTrackDBSQ(dbName='FinTrackDB.db')
    app = FinTrackGUI(dataBase=db)
    app.mainloop()

if __name__ == "__main__":
    main()