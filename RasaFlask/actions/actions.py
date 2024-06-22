import sqlite3
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionSaveDetails(Action):

    def name(self):
        return "action_save_details"

    def run(self, dispatcher, tracker, domain):
        name = tracker.get_slot('name')
        phone_number = tracker.get_slot('phone_number')
        chi_nhanh = tracker.get_slot('chi_nhanh')
        loai_phong = tracker.get_slot('loai_phong')
        so_luong = tracker.get_slot('so_luong')
        thoi_gian = tracker.get_slot('thoi_gian')

        # Lưu thông tin vào SQLite3
        conn = sqlite3.connect('hotel.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                chi_nhanh TEXT NOT NULL,
                loai_phong TEXT NOT NULL,
                so_luong TEXT NOT NULL,
                thoi_gian TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            INSERT INTO customers (name, phone_number, chi_nhanh, loai_phong, so_luong, thoi_gian) VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, phone_number, chi_nhanh, loai_phong, so_luong, thoi_gian))
        conn.commit()
        conn.close()

        dispatcher.utter_message(template="utter_thank_you", name=name, phone_number=phone_number, chi_nhanh=chi_nhanh, loai_phong=loai_phong, so_luong=so_luong, thoi_gian=thoi_gian)
        return [SlotSet("name", name), SlotSet("phone_number", phone_number), SlotSet("chi_nhanh", chi_nhanh), SlotSet("loai_phong", loai_phong), SlotSet("so_luong", so_luong), SlotSet("thoi_gian", thoi_gian)]
    

class ActionSaveDetails_thay_doi(Action):

    def name(self):
        return "action_save_details_thay_doi"

    def run(self, dispatcher, tracker, domain):
        name = tracker.get_slot('name')
        phone_number = tracker.get_slot('phone_number')

        # Lưu thông tin vào SQLite3
        conn = sqlite3.connect('hotel.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS thay_doi (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone_number TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            INSERT INTO thay_doi (name, phone_number) VALUES (?, ?)
        ''', (name, phone_number))
        conn.commit()
        conn.close()

        dispatcher.utter_message(template="utter_thong_bao_thay_doi", name=name, phone_number=phone_number)
        return [SlotSet("name", name), SlotSet("phone_number", phone_number)]
    

class ActionSaveDetails_huy_phong(Action):

    def name(self):
        return "action_save_details_huy_phong"

    def run(self, dispatcher, tracker, domain):
        name = tracker.get_slot('name')
        phone_number = tracker.get_slot('phone_number')

        # Lưu thông tin vào SQLite3
        conn = sqlite3.connect('hotel.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS huy_phong (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone_number TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            INSERT INTO huy_phong (name, phone_number) VALUES (?, ?)
        ''', (name, phone_number))
        conn.commit()
        conn.close()

        dispatcher.utter_message(template="utter_thong_bao_huy_phong", name=name, phone_number=phone_number)
        return [SlotSet("name", name), SlotSet("phone_number", phone_number)]