# read QR code and output the data
import cv2
import cv2
import webbrowser

def scan_qr(frame):
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(frame)
    if bbox is not None and data:
        # Tegn ramme om QR-koden
        pts = bbox.astype(int).reshape(-1, 2)
        for i in range(len(pts)):
            cv2.line(frame, tuple(pts[i]), tuple(pts[(i+1) % len(pts)]), (0, 255, 0), 2)
        # Vis tekst på skærmen
        x, y = pts[0]
        cv2.putText(frame, f"QR: {data}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print(f"QR fundet: {data}")
        webbrowser.open(data)
        return True
    return False

def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if scan_qr(frame):
            break  # Stop når vi har fundet en QR-kode
        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
