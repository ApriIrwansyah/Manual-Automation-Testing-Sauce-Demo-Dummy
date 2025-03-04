import sys
import os
# configparser adalah modul bawaan Python yang digunakan untuk membaca, menulis, dan memanipulasi file konfigurasi dalam format yang mirip dengan format INI. File konfigurasi sering digunakan untuk menyimpan pengaturan atau informasi yang dapat diubah tanpa harus memodifikasi kode sumber program.
import configparser

sys.path.append("../")
# ini untuk mengambil file di dalam folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))


# Membuat parser
config = configparser.RawConfigParser()
# Membaca file konfigurasi
config.read(".\\configuration\\config.ini")

# Membuat class
class Read_Config:
    # @staticmethod
    def get_admin_page_url():
        # Mengakses nilai
        url        = config.get('admin login info', 'pageURL')
        return url
    
    @staticmethod
    def get_username_std():
        # Mengakses nilai
        username_std        = config.get('admin login info', 'username_std')
        return username_std
    
    @staticmethod
    def get_username_locked():
        # Mengakses nilai
        username_locked     = config.get('admin login info', 'username_locked')
        return username_locked
    
    @staticmethod
    def get_username_problem():
        # Mengakses nilai
        sername_problem        = config.get('admin login info', 'username_problem')
        return sername_problem
    
    @staticmethod
    def get_username_performance():
        # Mengakses nilai
        username_performance        = config.get('admin login info', 'username_performance')
        return username_performance
    
    @staticmethod
    def get_username_error():
        # Mengakses nilai
        username_error        = config.get('admin login info', 'username_error')
        return username_error
    
    @staticmethod
    def get_username_visual():
        # Mengakses nilai
        username_visual        = config.get('admin login info', 'username_visual')
        return username_visual
    
    @staticmethod
    def get_password():
        # Mengakses nilai
        password        = config.get('admin login info', 'password')
        return password
