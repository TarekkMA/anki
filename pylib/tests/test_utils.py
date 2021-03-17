from anki.utils import stripHTML

def test_stripHTML_will_remove_tags():
  strings = [
    "<>",
    "<1>",
    "<asdasd>",
    "<\n>",
    "<\\qwq>",
    "<aa\nsd\nas\n?\n>"
  ]

  for s in strings:
    assert stripHTML(s) == ""