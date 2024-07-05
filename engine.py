#    engine.py: A Programmable Tetris-like Games Engine
#    Copyright (C) 2024  Ramprasad S. Joshi
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter import filedialog
from board import Board
from allextetrominoes import *
from shape import Shape
from time import time, sleep
from copy import copy, deepcopy

class TetrisEngine:
	def __init__(self, height=20, width=10, extetromino_distribution=range(1,20), update_duration=100, move_down_duration=1000,fg_color=2,bg_color=1,difficulty=1,rotation_limit=1e7):
		color_list=['light gray','blue','red','green','yellow','orange','black']
		self.window = tk.Tk()											  # fixed
		self.window.title("Python Text Tetris")		  # Programmable, inconsequential
		self.extetromino_distribution = extetromino_distribution	# Programmable:
			# Controls the number, variety and distribution.
			# This can be changed to range(1,74) for the give allextetrominoes module. Or to your list too.
			# If you want some pieces to have more frequency than others, then repeat their index in this 
			# list, and in that case give a proper enumerated tuple or a list, not a range or something
		self.width = height															# Essential and programmable
		self.height = width														# Essential and programmable
		self.rotations_limit=rotation_limit
		self.update_duration=update_duration
		self.text_area = tk.Text(										# Essential and partially programmable
															self.window,			# fixed unless you populate more components
															wrap=tk.CHAR,			# programmable, please find some way not to let it wrap
															height=self.height, # fixed
															width=2*self.width, # fixed
															bg=color_list[bg_color],		# programmable
															fg=color_list[fg_color],					# programmable
															font=('Courier New','16','bold'),		# programmable
														)
		self.text_area.pack(expand=tk.YES, fill=tk.BOTH)				# fixed
		self.board = Board(width=self.width,height=self.height)	# fixed
		self.pauseStatus = False																# fixed in the beginning, state variable
		self.window.bind("<Up>",self.rotate_CW)									# semi-fixed: change by providing a new
		self.window.bind("<Down>",self.rotate_AntiCW)						# callback: this is true of all the callbacks
		self.window.bind("<Left>",self.move_left)								# callback
		self.window.bind("<Right>",self.move_right)							# callback
		self.window.bind("<space>",self.drop_piece)							# callback
		self.update_duration = update_duration		# Progrmmable, and its progression too
		self.window.after(self.update_duration, lambda: self.update_step())	# callback4
		self.score=0
		self.move_down_duration =move_down_duration-100*difficulty													# Progrmmable, and its progression too
		self.window.after(self.move_down_duration, lambda: self.move_down_step()) # callback
		self.default_cursor = (0,int(self.board.width/2-1))			# Programmable. Where the new piece appears
		self.cursor = self.default_cursor												# State variable.
		self.initial_update_duration = self.update_duration
		self.initial_move_down_duration = self.move_down_duration
		self.new_piece()																				# This sequence is not much programmable.
		self.text_area.insert(tk.END,self.render())
		self.create_menu()
		self.window.mainloop()
	# Each of the methods below are programmable (replaceable) -- but give in the documentation
	# what the game programmer has to provide -- the functionality, role, the entagling of concerns.
	def render(self):
		area = deepcopy(self.board)
		piece = self.piece
		for row in range(self.piece.matrix.shape[0]):
			for column in range(self.piece.matrix.shape[1]):
				if self.piece.matrix[row][column] : area.area[row+self.cursor[0]][column+self.cursor[1]] = True
		return str(area)
	
	def toggle_pause_status(self):
		self.pauseStatus = not(self.pauseStatus)
	
	def rotate_CW(self, event):
		if(self.rotations_limit>0):
			newpiece = Shape(self.piece.matrix)
			newpiece.rotateCW()
			self.rotations_limit-=1
			if self.board.collision(newpiece.matrix,self.cursor):
				return False
			else:
				self.piece = newpiece
				return True

	
	def rotate_AntiCW(self, event):
		if(self.rotations_limit>0):
			newpiece = Shape(self.piece.matrix)
			newpiece.rotateAntiCW()
			self.rotations_limit-=1
			if self.board.collision(newpiece.matrix,self.cursor):
				return False
			else:
				self.piece = newpiece
				return True
			
	
	def move_left(self, event):
		self.move_piece('LEFT')
	
	def move_right(self, event):
		self.move_piece('RIGHT')
	
	def drop_piece(self, event):
		while self.move_piece('DOWN'):
			pass # Could be: nothing = "doing" # keep dropping
	
	def move_down_step(self):
		if not(self.move_piece('DOWN')):
			self.board.insertShape(self.piece.matrix,self.cursor[0],self.cursor[1])
			self.cursor = self.default_cursor
			self.new_piece()
		tobedeleted = [row for row in reversed(range(self.height)) if all(self.board.area[row])]
		if tobedeleted:
			self.score+=1
			self.create_menu()
			for row in reversed(tobedeleted):
				for newrow in reversed(range(row)):
					for column in range(self.width):
						self.board.area[newrow+1][column] = self.board.area[newrow][column]
			for row in range(len(tobedeleted)):
				self.board.area[row] = numpy.full_like(self.board.area[row],False)
		self.window.after(self.move_down_duration, lambda: self.move_down_step())
	
	def update_step(self):
		if self.pauseStatus:
			self.window.after(self.update_duration, lambda: self.update_step())
			return
		self.text_area.delete(1.0,tk.END)
		self.text_area.insert(tk.END,self.render())
		if self.board.collision(self.piece.matrix,self.cursor):
			string_board = self.render().split('\n')
			string_board[int(self.height/5)] = 'Game Over'
			lastmessage = ""
			for row in range(self.height):
				lastmessage = lastmessage + string_board[row].strip() + '\n'
			self.text_area.delete(1.0, tk.END)
			self.text_area.insert(1.0,lastmessage)
			self.dialog=tk.simpledialog.Dialog(self.window,"Game Over!")
			self.window.quit()
		else:
			self.window.after(self.update_duration, lambda: self.update_step())
	
	def speed_up(self):
		self.move_down_duration = int(numpy.floor(self.move_down_duration*0.9))
	
	def slow_down(self):
		self.move_down_duration = int(numpy.ceil(self.move_down_duration*1.1))
	
	def extetricks_help(self):
		self.pauseStatus = True
		help_message = '''
			This is EXtendedTETRIckS, extensible to extetrominoes and more.
			Play it like all other tetris clones.
			Copyright (C) 2024 Ramprasad S. Joshi.
			(CS&IS Dept, BITS, Pilani K K Birla Goa Campus, GOA INDIA.)
			+91 832 2580 121. rsj [at] the bits mail id below.
			goa.bits-pilani.ac.in
			https://www.bits-pilani.ac.in/goa/ramprasad-savlaram-joshi
			Developed as a pedagogical resource for
			Birla Institute of Technology and Science, Pilani.
			'''
		self.text_area.delete(1.0,tk.END)
		self.text_area.insert(tk.END,help_message)
		tk.simpledialog.Dialog(self.window,"Click any button to continue")
		self.pasueStatus = False
	
	def create_menu(self):
		menu = tk.Menu(self.window)
		self.window.config(menu=menu)

		extetris_menu = tk.Menu(menu)
		menu.add_cascade(label="Ameya's EXtendedTETRIckS", menu=extetris_menu)
		menu.add_cascade(label=f"Score={self.score}", menu=extetris_menu)
		extetris_menu.add_command(label="New Game", command=self.new_game)
		extetris_menu.add_separator()
		extetris_menu.add_command(label="Pause", command=self.toggle_pause_status)
		extetris_menu.add_separator()
		extetris_menu.add_command(label="Speed-Up", command=self.speed_up)
		extetris_menu.add_command(label="Slow-down", command=self.slow_down)
		extetris_menu.add_separator()
		extetris_menu.add_command(label="Save state", command=self.save_file)
		extetris_menu.add_separator()
		extetris_menu.add_command(label="Exit", command=self.window.quit)
		extetris_menu.add_separator()
		extetris_menu.add_command(label="Quit", command=self.window.quit)
		extetris_menu.add_separator()
		extetris_menu.add_command(label="About", command=self.extetricks_help)
	
	def new_piece(self,piece=None):
		if(piece==None): self.piece = Shape(get_any_extetromino(self.extetromino_distribution))
		else: self.piece = piece
	
	def new_game(self):
		self.pauseStatus = True
		self.text_area.delete(1.0, tk.END)
		self.board.area = numpy.full_like(self.board.area,False)
		self.new_piece()
		self.text_area.insert(tk.END,self.render())
		self.cursor = self.default_cursor
		self.update_duration = self.initial_update_duration
		self.move_down_duration = self.initial_move_down_duration
		self.pauseStatus = False

	def save_file(self):
		file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
		if file:
			with open(file, "w") as file_handler:
				file_handler.write(self.text_area.get(1.0, tk.END))
			self.window.title(f"Python Tetris Board - {file}")
    
	def increase_difficulty(self, increase_rotations=False, decrease_hold=False, increase_speed=False):
		if increase_rotations:
			self.rotations_limit = max(0, self.rotations_limit - 1)
		if decrease_hold:
			self.hold_limit = max(0, self.hold_limit - 1)
		if increase_speed:
			self.move_down_duration *= 1.2
		
	def move_piece(self,direction):
		if(direction=='LEFT'):
			offset = (0,-1)
		elif(direction=='RIGHT'):
			offset = (0,1)
		elif(direction=='UP'):
			offset = (-1,0)
		elif(direction=='DOWN'):
			offset = (1,0)
		new_cursor = tuple(map(lambda a,b:a+b,self.cursor,offset))
		if self.board.collision(self.piece.matrix,new_cursor):
			return False
		else:
			self.cursor = new_cursor
			return True
    



if __name__ == "__main__":
	tetris_engine = TetrisEngine()
