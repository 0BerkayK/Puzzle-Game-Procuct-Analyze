import pandas as pd
import numpy as np

# Kaggle üzerinden uygun veri seti bulamadığım için kendim random veri seti oluşturdum.

# Örnek oyun isimleri ( App Store Top Free puzzle oyunları)

# Link : https://apps.apple.com/us/charts/iphone/puzzle-games/7012

games = ['Township', 'Block Blast!', 'Gossip Harbor', 'Magic Sort!', 'Word Search Explorer']

np.random.seed(42)  # Tekrar üretilebilirlik

benchmark = pd.DataFrame({
    'game': games,
    'publisher': ['StudioA', 'StudioB', 'StudioC', 'StudioD', 'StudioE'],
    'retention_1': np.random.uniform(0.15, 0.9, len(games)),
    'retention_7': np.random.uniform(0.05, 0.7, len(games)),

})

benchmark.to_csv('../data/puzzle_games_benchmark.csv', index=False)

