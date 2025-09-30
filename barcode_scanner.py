import cv2
from pyzbar import pyzbar

def læs_stregkoder(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        # Tegn en firkant omkring stregkoden
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Afkod data
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        # Skriv typen og data ovenpå billedet
        text = f"{barcode_type}: {barcode_data}"
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)

        print(f"Fundet: {barcode_type} - {barcode_data}")

    return frame

def main():
    cap = cv2.VideoCapture(0)  # 0 = standard webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = læs_stregkoder(frame)
        cv2.imshow("Stregkode Scanner", frame)

        # Tryk på 'q' for at afslutte
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
