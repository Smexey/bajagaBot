from dataclasses import dataclass


@dataclass(frozen=True)
class Emojis:
    """
    Contains emoji id's
    """
    DOGE_DANCE = 854522626202664961
    DOGE_VIBE = 854523853015482400
    COFI = 668539556378837002
    BONK = 854524543849463839


@dataclass(frozen=True)
class Radio:
    """
    Contains radio urls
    """
    NAXI = 'https://naxi64ssl.streaming.rs:9162/;stream'
    ROCK = 'http://stream.radioparadise.com/rock-128'
