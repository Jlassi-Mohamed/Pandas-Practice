import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rowCount = len(players.index)
    colCount = len(players.keys())
    return [rowCount, colCount]
