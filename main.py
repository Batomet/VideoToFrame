import os

import cv2


def extract_frames_from_video(video_file, output_folder):
    try:
        cap = cv2.VideoCapture(video_file)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        frame_count = 0

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}_from_{video_file}.jpg")
            cv2.imwrite(frame_filename, frame)

            frame_count += 1

        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error processing {video_file}: {str(e)}")


def process_mp4_files_in_directory(input_directory, output_directory):
    for root, dirs, files in os.walk(input_directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)

            file_list = os.listdir(dir_path)

            mp4_files = [f for f in file_list if f.endswith(".mp4")]

            if mp4_files:
                output_folder = os.path.join(output_directory, dir_name)

                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)

                for mp4_file in mp4_files:
                    video_file = os.path.join(dir_path, mp4_file)

                    extract_frames_from_video(video_file, output_folder)
                    print(f"Extracted frames from {video_file}")


if __name__ == "__main__":
    input_directory = r"\OMGEmotionChallenge\DetailedAnnotation\train"
    output_directory = r"OMGFrame"

    process_mp4_files_in_directory(input_directory, output_directory)
