import os
import time
import concurrent.futures
from itertools import cycle

class FileProcessor:

    def __init__(self, key:str) -> None:
        self.__key = key.encode('ascii')

    @staticmethod
    def file_read(src_file_path:str) -> bytes:
        with open(src_file_path, 'rb') as f:
            content_chars = f.read()
        return content_chars
    
    @staticmethod
    def file_write(data:bytes, tgt_file_path:str) -> None:
        try:
            os.mkdir(os.path.dirname(tgt_file_path))
        except:
            pass
        with open(tgt_file_path, 'wb') as f:
            f.write(data)

    def process(self, src_file_path:str, tgt_file_path:str) -> None:
        print(f"Processing file - {src_file_path}...")
        data = self.file_read(src_file_path)
        processed_data = bytes(a ^ b for a, b in zip(data, cycle(self.__key)))
        self.file_write(processed_data, tgt_file_path)
        print(f"Processing file - {src_file_path} to {tgt_file_path} is done.")

if __name__ == "__main__":
    start = time.time()
    fp = FileProcessor("my secret key")
    video_path = 'G:\Lectures\PostgreSQL\S1\Processed'
    videos = os.listdir(video_path)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        procs = [executor.submit(fp.process,os.path.join(video_path, video),
                                                os.path.join(video_path, "Processed", video)) 
                                                for video in videos]
    finish = time.time()
    print(f"Total time taken: {finish-start} second(s).")
