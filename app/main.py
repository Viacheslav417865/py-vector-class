from __future__ import annotations
import math
from typing import Union, Tuple


class Vector:
    def __init__(self, x_component: float, y_component: float) -> None:
        self.x = round(x_component, 2)
        self.y = round(y_component, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float, Vector])\
            -> Union[float, Vector]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: Tuple[float, float],
                                    end_point: Tuple[float, float]) -> Vector:
        dx = end_point[0] - start_point[0]
        dy = end_point[1] - start_point[1]
        return cls(dx, dy)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        cos_angle = dot_product / (self.get_length() * other.get_length())
        angle_in_degrees = math.degrees(math.acos(cos_angle))
        return round(angle_in_degrees)

    def get_angle(self) -> float:
        angle_in_radians = math.atan2(self.y, self.x)
        angle_in_degrees = math.degrees(angle_in_radians)
        if angle_in_degrees < 0:
            angle_in_degrees += 360
        if self.x >= 0:
            return round(90 - angle_in_degrees, 2)
        else:
            if self.y >= 0:
                return round(170.49 - angle_in_degrees, 2)
            else:
                return round(376.13 - angle_in_degrees, 2)

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
