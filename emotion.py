import os
import shutil

SOURCE_DIR = "data/images"
TARGET_DIR = "dataset"

os.makedirs(TARGET_DIR, exist_ok=True)

for person in os.listdir(SOURCE_DIR):
    person_path = os.path.join(SOURCE_DIR, person)

    if not os.path.isdir(person_path):
        continue

    for emotion in os.listdir(person_path):
        emotion_path = os.path.join(person_path, emotion)

        if not os.path.isdir(emotion_path):
            continue

        target_emotion_dir = os.path.join(TARGET_DIR, emotion)
        os.makedirs(target_emotion_dir, exist_ok=True)

        for img in os.listdir(emotion_path):
            src_img = os.path.join(emotion_path, img)
            dst_img = os.path.join(
                target_emotion_dir,
                f"{person}_{img}"   # avoid filename collisions
            )
            shutil.copy(src_img, dst_img)
