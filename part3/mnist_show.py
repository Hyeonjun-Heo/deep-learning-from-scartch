import sys, os
sys.path.append(os.pardir) # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

# 처음 한 버은 몇 분 정도 걸립니다.
(x_train, t_train), (x_test, t_test) = \
  load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label)

print(img.shape) # (784,)
img = img.reshape(28, 28) # 원래 이미지의 모양으로 변형
print(img.shape) # (28, 28)

img_show(img)

