import cv2

def perform_dilation(img, size):
    img2 = img.copy()
    dilation_type = cv2.MORPH_CROSS
    kernel = cv2.getStructuringElement(dilation_type, (size, size))
    # return cv2.dilate(img, kernel, iterations=1)
    img2 = cv2.erode(img2, kernel, iterations=1)
    # img2 = cv2.dilate(img, kernel, iterations=1)
    return cv2.erode(img2, kernel, iterations=1)


def perform_denoising(img, size):
    dilation_type = cv2.MORPH_ELLIPSE
    kernel = cv2.getStructuringElement(dilation_type, (size, size))
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

def remove_small_dirts(img, MAX_GRAIN_AREA_TO_REMOVE):
    test_subject = img.copy()
    contours, hierarchy = cv2.findContours(img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if area < MAX_GRAIN_AREA_TO_REMOVE:
            cv2.fillPoly(test_subject, pts=[cnt], color=(255,255,255))
    return test_subject

