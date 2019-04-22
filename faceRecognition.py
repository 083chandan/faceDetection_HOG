import numpy as np
import face_recognition
import pickle
import cv2


cameraSel=1
pickleFileLoc="faceModel.pickle"
detectionModel="hog"

print("[INFO] program started...")
print("[INFO] loading encodings...")
data = pickle.loads(open(pickleFileLoc, "rb").read())

def findPerson(imageFrame):
	image = imageFrame
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	print("[INFO] recognizing faces...")
	boxes = face_recognition.face_locations(rgb,
											model=detectionModel)
	encodings = face_recognition.face_encodings(rgb, boxes)
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
		names.append(name)
	for ((top, right, bottom, left), name) in zip(boxes, names):
		cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
					0.75, (0, 255, 0), 2)
	return(image)


def runDetection():
	print("[INFO] program started...")
	cap=cv2.VideoCapture(cameraSel)
	if (cap.isOpened()==False):
		print("[ERROR] Error opening vidoe file/camera")
	print("[INFO] webcam loaded and available, using ",cameraSel)
	while(cap.isOpened()):
		ret, frame =cap.read()
		if ret==True:

			cv2.imshow("Frame", findPerson(frame))

			if cv2.waitKey(25) & 0xFF == ord("q"):
				break
		else:
			break
	cap.release()

if __name__ == "__main__":
	runDetection()
	