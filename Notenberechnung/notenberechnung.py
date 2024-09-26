def schriftliche_note_bestimmen(prozentwert: int) -> str:
    if(prozentwert > 100 or prozentwert < 0):
        raise ValueError
    if(prozentwert > 91):
        return "sehr gut"
    if(prozentwert > 80):
        return "gut"
    return "moment mal so nicht mein freund"