import logging # 6

class LogMaker: #6 

    def log_generated(): # 6
        # mendefinisikan definisikan format waktu
        logging.basicConfig(filename=".\\logs\\orangeHRM.log", format="%(asctime)s:%(levelname)s:%(message)s", datefmt="%Y-%m-%d %H:%M:%S", force=True)
        # logging dot . ini harus memanggil salah satu metode untuk mendapatkan metode getLogger() untuk menggunakan kita harus mengatur levelnya untuk mendapatkan INFO
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # setelah itu menngembalikan object dan memanggilnya di test-cases
        return logger 