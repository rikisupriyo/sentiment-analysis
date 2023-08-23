import re

#defining regex patterns
urlPattern        = r"((http://)[^ ]*|(https://)[^ ]*|(www\.)[^ ]*)"
userPattern       = '@[^\s]+'
hashtagPattern    = '#[^\s]+'
alphaPattern      = "[^a-z0-9<>]"
sequencePattern   = r"(.)\1\1+"
seqReplacePattern = r"\1\1"

# Defining regex for emojis
smileemoji        = r"[8:=;]['`\-]?[)d]+"
sademoji          = r"[8:=;]['`\-]?\(+"
neutralemoji      = r"[8:=;]['`\-]?[\/|l*]"
lolemoji          = r"[8:=;]['`\-]?p+"

def preprocessing(text):

  """
  Preprocesses the text

  Parameters
  ----------
  text (str): text in string format
  """
  text = re.sub(urlPattern,'<url>',text)
  text = re.sub(userPattern,'<user>', text)
  text = re.sub(sequencePattern, seqReplacePattern, text)
  text = re.sub(r'<3', '<heart>', text)
  text = re.sub(smileemoji, '<smile>', text)
  text = re.sub(sademoji, '<sadface>', text)
  text = re.sub(neutralemoji, '<neutralface>', text)
  text = re.sub(lolemoji, '<lolface>', text)
  text = re.sub(alphaPattern, ' ', text)
  text = re.sub(r'/', ' / ', text)
  text = text.lower()
  
  return text
