import os
from predict import predict_image

test_dir = "test"

total = 0
correct = 0

for label in os.listdir(test_dir):
    class_path = os.path.join(test_dir, label)
    if not os.path.isdir(class_path):
        continue

    for img_name in os.listdir(class_path):
        img_path = os.path.join(class_path, img_name)

        try:
            pred, conf = predict_image(img_path)

            if pred == label:
                correct += 1

            total += 1

            print(f"{img_name} → Pred: {pred}, Actual: {label}")

        except Exception as e:
            print(f"Error with {img_name}: {e}")

accuracy = correct / total * 100
print(f"\nAccuracy: {accuracy:.2f}%")