
import face_recognition
import imutils
import pickle
import cv2

currentname = "unknown"
encodingsP = "encodings.pickle"

print("[INFO] Carregando Codificações + Detctor de face...")
data = pickle.loads(open(encodingsP, "rb").read())

cap = cv2.VideoCapture(0)

while True:

	ret, frame = cap.read()
	frame = imutils.resize(frame, width=500)
	boxes = face_recognition.face_locations(frame)
	encodings = face_recognition.face_encodings(frame, boxes)
	names = []

	for encoding in encodings:
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)
		name = "Unknown"

		if True in matches:
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1
			name = max(counts, key=counts.get)
			if currentname != name:
				currentname = name
				print(currentname)
		names.append(name)
	for ((top, right, bottom, left), name) in zip(boxes, names):
		cv2.rectangle(frame, (left, top), (right, bottom),
			(0, 255, 225), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			.8, (0, 255, 255), 2)
	cv2.imshow("Detector de Face rodando...", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

cv2.destroyAllWindows()

