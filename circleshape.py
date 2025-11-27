import pygame


class CircleShape(pygame.sprite.Sprite):
    """CircleShape class:

    Args:
        x (int): x-coordinate of the circle's center
        y (int): y-coordinate of the circle's center
        radius (int): radius of the circle
    """

    def __init__(self, x, y, radius) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface):
        pass

    def update(self, dt: float):
        pass

    def collides_with(self, other: "CircleShape") -> bool:
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)
