import os
from pydub import AudioSegment

def convert_flac_to_mp3(source_folder):
    if not os.path.isdir(source_folder):
        print("The specified folder does not exist.")
        return

    for file_name in os.listdir(source_folder):
        if file_name.endswith(".flac"):
            flac_file_path = os.path.join(source_folder, file_name)
            mp3_file_path = os.path.join(source_folder, os.path.splitext(file_name)[0] + ".mp3")

            # Convert FLAC to MP3
            audio = AudioSegment.from_file(flac_file_path, format="flac")
            audio.export(mp3_file_path, format="mp3")

            print(f"Converted: {flac_file_path} to {mp3_file_path}")

    print("Conversion process completed.")

if __name__ == "__main__":
    source_folder = input("Enter the folder path: ")
    convert_flac_to_mp3(source_folder)
