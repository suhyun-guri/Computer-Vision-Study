import cv2
from cv2 import FONT_HERSHEY_SIMPLEX

if __name__ == '__main__':
    #이미지에 선 그리기
    #cv2.line(img, start_point, end_point, color, line_thickness, line_type)
    img = cv2.imread("./img/Lenna.png", cv2.IMREAD_COLOR)
    line_img = cv2.line(img, (0,0), (img.shape[0], img.shape[1]), (255,0,0),
                        1, cv2.LINE_AA)
    cv2.imwrite('./img/draw_line.jpg', line_img)
    
    #원 그리기 
    #cv2.circle(img, center_point, radius, color, line_thickness, line_type)
    #center_point : 원의 중심점 / radius : 반지름 길이
    #OpenCV는 x,y 로 인식을 하므로 shape[1], shape[0] 이렇게 적용해야 한다.
    circle_img = cv2.circle(img, (img.shape[1]//2, img.shape[0]//2), 100, (0,255,0), 5)
    cv2.imwrite('./img/circle_img.jpg', circle_img)
    
    #직사각형 그리기
    #cv2.rectangle(img, top_left, bottom_right, color, line_thickness, line_type)
    #top_left : 사각형이 이미지에 위치할 좌상단 모서리 좌표
    #bottom_right : 사각형이 이미지에 위치할 우하단 모서리 좌표
    rectangle_img = cv2.rectangle(img, (100,100), (300,400), (0,0,255), 5)
    cv2.imwrite('./img/rectangle_img.jpg', rectangle_img)
    
    #텍스트 쓰기
    #cv2.putText(img, string, text_bottom_left, font_type, font_scale, color, line_thickness, line_type)
    #string : 이미지에 쓸 문자열, 영문만 사용 가능 - 지원하는 폰트가 한글을 지원하지 않음. - 한글 쓰면 물음표로 나온다.
    #text_bottom_left : 문자열이 시작되는 좌측 하단 좌표
    text_img = cv2.putText(img, "This is Lenna", (100,100), cv2.FONT_HERSHEY_SIMPLEX, 2.7, (128,0,128), 5)
    cv2.imwrite('./img/text_img.jpg', text_img)
    