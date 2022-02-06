import cv2

if __name__ == '__main__':
    # 흑백 이미지 컬러 변환하기 - cv2.cvtColor(image, option)
    color_img = cv2.imread("./img/Lenna.png", cv2.IMREAD_COLOR) 
    # BGR - OpenCV에서는 BGR 순서로 읽는다.
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
    
    # cv2.imwrite('./img/converted_to_gray.jpg', gray_img)
    
    #이미지 리사이징 하기 - cv2.resize(image, dsize)
    #dsize : 목적 이미지 크기. 튜플 형태로 (가로, 세로) 지정
    resized_img = cv2.resize(color_img, (1024, 1024))
    # cv2.imwrite('./img/resized_img.jpg', resized_img)
    print(resized_img.shape) #(1024, 1024, 3)
    
    #이미지 크롭하기 - 단순히 인덱싱을 하면 된다. (슬라이싱)
    #OpenCV는 이미지를 행렬로 다루므로 numpy의 슬라이싱 기능 그대로 사용 가능
    #[시작행:종료행, 시작열:가로열]
    cropped_img = color_img[0:color_img.shape[0]//2, 0:color_img.shape[1]//2]
    print(cropped_img.shape) #(256, 256, 3)
    cv2.imwrite('./img/cropped_img.jpg', cropped_img)