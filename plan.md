# Data Structures:

>### Occupied_Spaces
> dict of spaces (keys) with pieces (values)


## Classes:

### Hierarchy:
>- Queen as superclass
>- King as sub of queen
>- Bishop as sub of queen
>- Rook as sub of queen
>- Pawn as sub of queen
>- knight as sub of queen


### Attributes:

>#### Has_Moved
>- bool
>- init False

>#### Position
>- str
>- init 'a1'

>#### Colour
>- str
>- init 'w'

>#### Passant
>- unique to Pawn
>- bool
>- init False


### Methods:

>#### Validate_Move(NewPos)
>- checks the shape of movement of the piece
>- returns a bool

>#### Move(Piece, NewPos)
>- sets piece pos to newpos if valid move
>- calls Check_Space_Occupied(NewPos)
>- calls Take(NewPos) if NewPos occupied

# Functions:

>### Take(Pos)
>- Kills the object at Pos
>- Uses the dict

>### Check_Valid_Space(Pos)
>- Checks that a space is within the confines of the board
>- Returns a bool

>### Check_Space_Occupied(Pos)
>- Checks the dict for occupation of a given space
>- Returns the piece at the position