import math

from pygame.math import Vector2

class Ball:
    """
    base class for bouncing objects
    """
    def __init__(self, bounds, position, velocity, color, radius):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.radius = radius

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: # screen width
            self.velocity.x *= -1
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius: # screen height
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)

        
class BouncingBall(Ball):
    def __init__(self, bounds, position, velocity, color, radius):
        print("what up")
        Ball.__init__(self, bounds, position, velocity, color, radius)
        
    def update(self):
        #f = mg we don't have a mass 
        # ALSO V = U - gt
        if self.velocity.y > 0.001:
            self.velocity.y = self.velocity.y - 0.001
        elif self.velocity.y < 0.001:
            self.velocity.y = self.velocity.y + 0.001
        else:
            self.velocity.y = 0
        
        Ball.update(self)
        
    
class BouncingBall2(Ball):
    """
    ball effected by gravity
    """
    def update(self):
        self.velocity.y += 0.3
        Ball.update(self)

class RainbowBall(Ball):
    def update(self):
        r =  (self.color[0] + 6) % 256
        g =  (self.color[1] + 4) % 256
        b =  (self.color[2] - 2) % 256
        
        self.color = [r,g,b]
        Ball.update(self)
# class RainbowBall(???):
#     """
#     Ball that changes colors
#     """
#     # TODO:

# class BouncingRainbow(???):
#     """
#     Ball that changes color and is affected by gravity
#     """
#     # TODO:

class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    def update(self):   
        BouncingBall.update(self)
        RainbowBall.update(self)

class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    def __init__(self, object_list, bounds, position, velocity, color, radius):
        self.object_list = object_list
        super().__init__(bounds, position, velocity, color, radius)

    def update(self):
        for obj in self.object_list:

            if not issubclass(type(obj), KineticBall):
                continue

            if obj == self:
                continue

            distance = obj.position.distance_to(self.position)
            
            sumr = self.radius + obj.radius

            if distance < sumr:
                self.velocity.x *= -1
                self.velocity.y *= -1
                print("Collision!")
        Ball.update(self)  
        
class KineticBouncing(KineticBall):
    """
    Ball that changes color and is affected by gravity
    """
    def update(self):
        self.velocity.y += 0.3
        KineticBall.update(self)
    

# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """