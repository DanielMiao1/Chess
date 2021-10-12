"""
Type Enumerations
"""


class enums:
	class Color:
		white, black = "white", "black"
		current, any = "current", "any"

		@staticmethod
		def all():
			return [enums.Color.white, enums.Color.black]

		@staticmethod
		def invert(color):
			if color in ["white", "w"]:
				return "black"
			elif color in ["black", "b"]:
				return "white"
			else:
				raise errors.UndefinedColor(color)

	class Piece:
		pawn, knight, bishop, rook = "pawn", "knight", "bishop", "rook"
		queen, king = "queen", "king"
		unicode_dictionary = {"whiteking": "♔", "blackking": "♚", "whitequeen": "♕", "blackqueen": "♛", "whiterook": "♖", "blackrook": "♜", "whitebishop": "♗", "blackbishop": "♝", "whiteknight": "♘", "blackknight": "♞", "whitepawn": "♙", "blackpawn": "♟"}
		piece_values = {"pawn": 1, "knight": 3, "bishop": 3, "rook": 5, "queen": 9, "king": float("inf")}
		piece_square_tables = {
			"middlegame": {
				"pawn": [[0, 0, 0, 0, 0, 0, 0, 0], [50, 50, 50, 50, 50, 50, 50, 50], [35, 35, 35, 35, 35, 35, 35, 35], [5, 5, 15, 14, 14, 15, 5, 5], [5, 5, 7, 12, 12, 7, 5, 5], [-4, -4, -4, -2, -2, -4, -4, -4], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
				"knight": [[-100, -70, -50, -50, -50, -50, -70, -100], [-70, -30, 0, 0, 0, 0, -30, -70], [-50, 10, 15, 16, 16, 15, 10, -50], [-30, 5, 8, 30, 30, 8, 5, -30], [-30, 4, 12, 15, 15, 12, 4, -30], [-50, 5, 15, 5, 5, 15, 5, -50], [-70, -50, -5, -2, -7, -5, -50, -70], [-100, -20, -50, -10, -10, -20, -20, -100]],
				"bishop": [[-20, 0, -2, -2, -2, -2, 0, -20], [-10, 0, 0, 0, 0, 0, 0, -10], [-6, 10, 8, 5, 5, 8, 10, -6], [-4, 15, 10, 9, 9, 10, 15, -4], [-2, 0, 20, 12, 12, 20, 0, -2], [-5, -5, 2, 15, 15, 2, -5, -5], [0, 30, -5, 5, 5, -5, 30, 0], [-50, -20, -10, -40, -40, -10, -20, -50]],
				"rook": [[10, 10, 10, 10, 10, 10, 10, 10], [25, 25, 25, 25, 25, 25, 25, 25], [5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5], [-5, -5, -5, -5, -5, -5, -5, -5], [-15, -15, -5, -15, -15, -15, -15, -15], [0, -5, 0, 10, 15, 10, -5, 0]],
				"queen": [[0, 30, 30, 40, 40, 30, 30, 0], [5, 20, 20, 25, 25, 20, 20, 5], [0, 20, 20, 25, 25, 20, 20, 0], [0, 20, 20, 20, 20, 20, 20, 6], [-2, 5, 5, 5, 5, 5, 5, -2], [-5, 0, 0, -5, -5, 6, 0, -5], [-10, -2, 0, 2, 2, 2, -2, -10], [-20, -19, -5, 5, 0, -5, -19, -20]],
				"king": [[-50, -50, -50, -50, -50, -50, -50, -50], [-50, -50, -50, -50, -50, -50, -50, -50], [-50, -50, -50, -50, -50, -50, -50, -50], [-50, -50, -50, -50, -50, -50, -50, -50], [-50, -50, -50, -50, -50, -50, -50, -50], [-50, -50, -50, -50, -50, -50, -50, -50], [-50, -50, -50, -45, -45, -50, -50, -50], [5, 7, 5, -10, 0, 0, 5, 7]]
			},
			"endgame": {
				"pawn": [[0, 0, 0, 0, 0, 0, 0, 0], [200, 200, 200, 200, 200, 200, 200, 200], [80, 80, 80, 80, 80, 80, 80, 80], [40, 30, 20, 10, 10, 20, 30, 40], [20, 10, 0, -2, -2, 0, 10, 20], [10, 10, 5, 0, 0, 5, 10, 10], [5, 5, 5, 5, 5, 5, 5, 5], [0, 0, 0, 0, 0, 0, 0, 0]],
				"knight": [[-100, -70, -50, -50, -50, -50, -70, -100], [-70, -30, 0, 0, 0, 0, -30, -70], [-50, 10, 15, 16, 16, 15, 10, -50], [-30, 5, 8, 30, 30, 8, 5, -30], [-30, 4, 12, 15, 15, 12, 4, -30], [-50, 5, 15, 5, 5, 15, 5, -50], [-70, -50, -5, -2, -7, -5, -50, -70], [-100, -150, -50, -10, -10, -20, -150, -100]],
				"bishop": [[-20, -10, -2, -2, -2, -2, -10, -20], [-10, 0, 0, 0, 0, 0, 0, -10], [-6, 10, 8, 5, 5, 8, 10, -6], [-4, 15, 10, 9, 9, 10, 15, -4], [-2, 0, 20, 12, 12, 20, 0, -2], [-5, -5, 2, 15, 15, 2, -5, -5], [0, 30, -5, 5, 5, -5, 30, 0], [-50, -20, -150, -40, -40, -150, -20, -50]],
				"rook": [[10, 10, 10, 10, 10, 10, 10, 10], [30, 30, 30, 30, 30, 25, 25, 25], [5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5], [-5, -5, -5, -5, -5, -5, -5, -5], [-15, -15, -5, -15, -15, -15, -15, -15], [0, -5, 0, 10, 15, 10, -5, 0]],
				"queen": [[20, 30, 30, 40, 40, 30, 30, 20], [5, 20, 20, 25, 25, 20, 20, 5], [0, 20, 20, 25, 25, 20, 20, 0], [0, 20, 20, 20, 20, 20, 20, 0], [5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, -150, 5, 5, 5, 5]],
				"king": [[-500, -250, -200, -200, -200, -200, -250, -500], [-250, 10, 10, 10, 10, 10, 10, -250], [-200, 10, 10, 10, 10, 10, 10, -200], [-200, 10, 10, 10, 10, 10, 10, -200], [-200, 10, 10, 10, 10, 10, 10, -200], [-200, 10, 10, 10, 10, 10, 10, -200], [-250, 0, 0, 0, 0, 0, 0, -250], [-500, -400, -350, -200, -200, -200, -400, -500]]
			}
		}

		@staticmethod
		def all():
			return [enums.Piece.pawn, enums.Piece.knight, enums.Piece.bishop, enums.Piece.rook, enums.Piece.queen, enums.Piece.king]

		@staticmethod
		def unicode(piece, color="white"):
			if piece not in enums.Piece.all():
				raise errors.UndefinedPiece(piece)
			if color not in [enums.Color.white, enums.Color.black]:
				raise errors.UndefinedColor(color)
			return enums.Piece.unicode_dictionary[color + piece]

		@staticmethod
		def value(piece):
			if piece in enums.Piece.all():
				return enums.Piece.piece_values[piece]
			raise errors.UndefinedPiece(piece)

		@staticmethod
		def evaluate_piece_position(piece, position, color, game_phase):
			if game_phase not in enums.Phase.all():
				raise errors.UndefinedGamePhase(game_phase)
			if piece not in enums.Piece.all():
				raise errors.UndefinedPiece(piece)
			if color not in [enums.Color.white, enums.Color.black]:
				raise errors.UndefinedColor(color)
			if color == enums.Color.white:
				return enums.Piece.piece_square_tables["middlegame" if game_phase in [enums.Phase.opening, enums.Phase.middlegame] else "endgame"][piece][functions.coordinateToIndex(position)[0]][functions.coordinateToIndex(position)[1]]
			return list(reversed([list(reversed(i)) for i in enums.Piece.piece_square_tables["middlegame" if game_phase in [enums.Phase.opening, enums.Phase.middlegame] else "endgame"][piece]]))[functions.coordinateToIndex(position)[0]][functions.coordinateToIndex(position)[1]]

	class Phase:
		opening, middlegame, endgame = "opening", "middlegame", "endgame"

		@staticmethod
		def all():
			return [enums.Phase.opening, enums.Phase.middlegame, enums.Phase.endgame]

	class Move:
		def __init__(self, name, old_position, new_position, piece, is_capture=False, check=False):
			self.piece = piece
			self.name = name
			self.old_position, self.new_position = old_position, new_position
			self.is_capture = is_capture
			self.check = check
			if is_capture:
				self.captured_piece = self.piece.board.pieceAt(new_position)
			else:
				self.captured_piece = None

		__str__ = __repr__ = lambda self: str(self.name)
