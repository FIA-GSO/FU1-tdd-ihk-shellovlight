def schriftliche_note_bestimmen(prozentwert: int) -> str:
    if(prozentwert > 100 or prozentwert < 0):
        raise ValueError
    return "sehr gut"