import cv2


if __name__ == '__main__':
    #이미지 읽어오기 - cv2.imread(filename, flag)
    #flag : 컬러/흑백으로 읽을 것인지 설정
    color_img = cv2.imread("./img/Lenna.png", cv2.IMREAD_COLOR) 
    gray_img = cv2.imread("./img/Lenna.png", cv2.IMREAD_GRAYSCALE)
    
    print(color_img.shape) #opencv에서는 numpy array 형식으로 표현됨 - shape 확인 가능
    print(gray_img.shape)
    # (512, 512, 3)
    # (512, 512)     
    
    #파일로 저장하기 - cv2.imwrite(filename, image var)
    if cv2.imwrite("./img/lenna.jpg", gray_img):
        print("저장완료")
    else:
        print("저장실패") 