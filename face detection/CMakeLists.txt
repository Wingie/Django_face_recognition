project( facedetect )
find_package( OpenCV REQUIRED )
add_executable( facedetect facedetect )
target_link_libraries( facedetect ${OpenCV_LIBS} )

