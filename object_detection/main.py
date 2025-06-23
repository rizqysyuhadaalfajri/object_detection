import cv2
from ultralytics import YOLO
import numpy as np
from collections import Counter
from datetime import datetime
from playsound import playsound
import os
import time

MODEL_PATH = "yolov8n.pt"

# Buat folder screenshot jika belum ada
os.makedirs("screenshot", exist_ok=True)

# Daftar label yang akan memicu suara dan screenshot
ALERT_LABELS = ["person", "car", "motorbike"]
ALERT_SOUND_PATH = "alert.wav"  # Pastikan file ini ada di direktori utama

# Untuk menghindari pemutaran suara berulang
played_alert = set()


last_screenshot_time = {}
def detect_from_camera():
    model = YOLO(MODEL_PATH)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Tidak bisa membuka kamera.")
        return

    conf_histories = {}
    bbox_histories = {}
    N = 5

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame, conf=0.5, save=False)
        boxes = results[0].boxes
        annotated_frame = frame.copy()

        detected_labels = []

        for i, box in enumerate(boxes):
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            label = model.names.get(cls_id, "Tidak dikenal")
            detected_labels.append(label)

            # Inisialisasi history
            if i not in conf_histories:
                conf_histories[i] = []
                bbox_histories[i] = []

            conf_histories[i].append(conf)
            bbox_histories[i].append([x1, y1, x2, y2])

            if len(conf_histories[i]) > N:
                conf_histories[i].pop(0)
                bbox_histories[i].pop(0)

            avg_conf = sum(conf_histories[i]) / len(conf_histories[i])
            avg_bbox = np.mean(bbox_histories[i], axis=0).astype(int)
            x1_s, y1_s, x2_s, y2_s = avg_bbox

            label_display = f"{label} ({avg_conf:.2f})"
            cv2.rectangle(annotated_frame, (x1_s, y1_s), (x2_s, y2_s), (0, 255, 0), 2)
            text_origin = (x1_s, y1_s - 10 if y1_s - 10 > 10 else y1_s + 20)
            cv2.putText(annotated_frame, label_display, text_origin, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            # Fitur logging waktu
            now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open("log.txt", "a") as f:
                f.write(f"[{now_str}] Detected: {label} - Confidence: {avg_conf:.2f}\n")

            # Fitur screenshot dan suara
            if label.lower() in ALERT_LABELS:
                current_time = time.time()
                last_time = last_screenshot_time.get(label, 0)

                if current_time - last_time >= 5:  # atur delay 5 detik misalnya
                    filename = f"screenshot/{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                    cv2.imwrite(filename, frame)
                    last_screenshot_time[label] = current_time

                # Suara alert hanya satu kali per label
                if label not in played_alert:
                    try:
                        playsound(ALERT_SOUND_PATH)
                        played_alert.add(label)
                    except Exception as e:
                        print(f"Gagal memutar suara: {e}")


        # Hitung objek per label
        label_counts = Counter(detected_labels)
        y_offset = 30
        for label, count in label_counts.items():
            display = f"{label}: {count}"
            cv2.putText(annotated_frame, display, (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
            y_offset += 25

        # Hapus history lama
        current_indices = set(range(len(boxes)))
        keys_to_delete = [k for k in conf_histories.keys() if k not in current_indices]
        for k in keys_to_delete:
            del conf_histories[k]
            del bbox_histories[k]

        cv2.imshow("Deteksi Objek", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_from_camera()
