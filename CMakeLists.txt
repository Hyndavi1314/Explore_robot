cmake_minimum_required(VERSION 3.8)
project(explore_robot_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

install(
  DIRECTORY config launch rviz urdf worlds models
  DESTINATION share/${PROJECT_NAME}
)

ament_package()