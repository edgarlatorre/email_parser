import talon
from talon import quotations

def extract_from_html(body):
    talon.init()
    reply = quotations.extract_from_html(body)

    return reply
