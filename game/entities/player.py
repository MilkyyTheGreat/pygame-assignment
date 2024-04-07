import pygame
from game.globals import Dimensions, Colours
from game.entities.entity import Entity

class Player(Entity):
	def __init__(self, x: int, y: int):
		self.size = 32
		self.speed = 7
		self.jump_force = 9
		self.gravity = 6
		self.jumping = False
		self.jump_count = 0

		super().__init__(pygame.Surface((self.size, self.size)))
		self.surf.fill(Colours.PLAYER)
		self.rect = self.surf.get_rect(center=(x, y))

	def update(self, pressed_key):
		vel_x = 0
		vel_y = 0
		
		if pressed_key[pygame.K_d]:
			vel_x = self.speed

		if (pressed_key[pygame.K_SPACE] or pressed_key[pygame.K_w]) and self.on_ground():
			self.jumping = True
		
		if self.jumping:
			if self.jump_count <= 10:
				vel_y = -self.jump_force
				self.jump_count += 1
			elif self.jump_count <= 12:
				# frames to stay in the air
				self.jump_count += 1
			else:
				self.jumping = False
				self.jump_count = 0
		else:
			vel_y += self.gravity

		

		self.rect.move_ip(vel_x, vel_y)
		self.rect.clamp_ip(pygame.Rect(0, 0, Dimensions.WINDOW_WIDTH, Dimensions.WINDOW_HEIGHT/2))

	def on_ground(self):
		return self.rect.bottom >= Dimensions.WINDOW_HEIGHT / 2