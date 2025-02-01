import mysql.connector

def create_database():
    try:
        # Connect to the MySQL server (update with your actual credentials)
        mydb = mysql.connector.connect(
            host="localhost",
            user="mercylinekemunto",
            password="Orina.duncan3181"
        )

        if mydb.is_connected():
            cursor = mydb.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as e:
        # This block catches MySQL-related errors
        print(f"Error: {e}")
    finally:
        # Ensure the cursor and connection are closed if they were opened
        if 'cursor' in locals():
            cursor.close()
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
