# message.py
# Collects methods that handle details of messages

# Checks that the message information in the dictionary m is valid:
# - There should be a `from` with length at most 20
# - There should be a `to` with length at most 20
# - There should be a `subject` with length at most 140
# - There should be a `body` with length at most 5000
def validate_new_message(m):
   for field in ['to', 'subject', 'body']:
      if field not in m:
         return 'Required fields: to, subject, body'
   if len(m.keys()) > 4:
      return 'Only fields allowed: to, subject, body'
   for field, length in [('from', 40), ('to', 40),
                         ('subject', 140), ('body', 5000)]:
      if len(m[field]) > length:
         return 'Field "%s" must not exceed length %d' % (field, length)
   return None
