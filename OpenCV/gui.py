import cv2

if __name__ == '__main__':
    #### 각 파트 실행할 때 다른 파트는 주석처리하여 사용 !!!!
    #(공통) 윈도우 생성
    #cv2.namedWindeow(window_name, flag)
    #이미지가 그려질 창을 생성하며, 창의 구분은 문자열 타입의 윈도우 이름으로 식별
    #flag에서 WINDOW_NORMAL, WINDOW_FULLSCREEN, WINDOW_AUTOSIZE 등 창을 최대화했을 때 자동으로 리사이징 할 건지, 리사이징 하나면 종횡비를 지키며 리사이징 할 건지 등 다양하게 선택 가능
    img = cv2.imread('./img/Lenna.png', cv2.IMREAD_COLOR)
    cv2.namedWindow('My Image', cv2.WINDOW_AUTOSIZE)
    #이미지 창에 그리기 - cv2.imshow(window_name, img_color)
    cv2.imshow('My Image', img)
    
    #2. 키보드 사용하기
    #waitKey : 키 입력 대기 시간 (ms단위를 받고 0이면 무한대기)
    cv2.waitKey(0)
    while True:
        key = cv2.waitKey(1000) #키를 받음
        if key == ord('q'): # q 키를 받으면
            break
        elif key == ord('g'):
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #g 키를 받으면 그레이로 바꿔라
        cv2.imshow('My Image', img)
        
    #2. 마우스 사용하기
    #콜백함수 정의
    def onMouse(event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            param[0] = cv2.circle(param[0], (x,y), 50, (255,0,0), 5)
            
    # param = [img]
    cv2.setMouseCallback('My Image', onMouse, param)
    
    while True:
        key = cv2.waitKey(1000) #키를 받음
        if key == ord('q'): # q 키를 받으면
            break
        elif key == ord('g'):
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #g 키를 받으면 그레이로 바꿔라
        cv2.imshow('My Image', img)
    
    #3. ROI 적용하기
    #roi : Region of Interest 관심 영역이라는 뜻으로 이미지 영역 중에서 특정 영역만 알고리즘을 적용하거나, 특정 영역에서 검출된 정보만을 사용
    #불필요한 주변 픽셀을 다 사용하지 않고 관심이 가는 영역을 지정하여 알고리즘의 성능을 높이고 싶을 때 설정
    roi = cv2.selectROI("My Image", img)
    print(roi) #실행하고 영역 선택해서 엔터치면 그 영역의 shape을 리턴 !