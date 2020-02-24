######################## Converter class ##############################
class Converter:
  def __init__(self, exp, symbols = 'MDCLXVI'):
    self.exp = exp
    self.symbols = symbols
    
  def convert(self):
    if len(self.symbols)>len(set(self.symbols)) or not self.symbols.isalpha():
      return ''
    self.generate_key_value()
    if self.exp.isdecimal() and self.exp[0] != '0':
      n, d = len(self.exp), {v: k for (k, v) in self.mapping.items()}
      d[0] = ''
      if int(self.exp[0])*10**(n-1) > max(d.keys()):
        return ''
      syms = [d[int(self.exp[i])*10**(n-1-i)] for i in range(n)]
      return ''.join(syms)
    elif self.exp.isalpha():
      i, result, max_val = 0, 0, 9*10**((len(self.symbols)-1)//2)
      while i < len(self.exp):
        key, key_len = '', 0
        while i+key_len < len(self.exp) and \
        self.exp[i: i+key_len+1] in self.mapping.keys():
          key = self.exp[i: i+key_len+1]
          key_len += 1
        if key_len == 0 or self.mapping[key] > max_val:
          return ''
        max_val //= 10
        result += self.mapping[key]
        i += key_len
      return result
    else:
      return ''
    
  def generate_key_value(self):
    d = {self.symbols[-1-i]: 5**(i%2)*10**(i//2) \
         for i in range(len(self.symbols))}
    one = self.symbols[-1]
    d[one*2], d[one*3] = 2, 3
    for i in range(-2,-len(self.symbols)-1,-2):
      c1, c2 = self.symbols[i], self.symbols[i+1]
      d[c2+c1], d[c1+c2], d[c1+c2*2], d[c1+c2*3] = \
      d[c1]-d[c2], d[c1]+d[c2], d[c1]+d[c2]*2, d[c1]+d[c2]*3
      if i + len(self.symbols) > 0:
        c1, c2 = self.symbols[i-1], self.symbols[i+1]
        d[c2+c1], d[c1*2], d[c1*3] = d[c1]-d[c2], d[c1]*2, d[c1]*3
    self.mapping = d
    
  def min_convert(self):
    if not self.exp.isalpha():
      return ''
    i, result, level, sym_map, expr = 0, 0, 1, {}, self.exp[::-1]
    while i < len(expr):
      s, r = expr[i], 1
      while i+r < len(expr) and expr[i+r] == s:
        r += 1
      if r > 3:
        return ''
      t, following = expr[i+r] if i+r < len(expr) else '', expr[i+r+1:]
      if r > 1 or (level, s) in sym_map.items():
        if not self.add_to_map(sym_map, level, s):
          return ''
        result += r*level
        if i+r < len(expr):
          if t not in following:
            if not self.add_to_map(sym_map, 5*level, t):
              return ''
            result += 5*level
            i += 1
          else:
            sym_map[5*level] = '_'
      else:
        if i+r >= len(expr) or t in following:
          if not self.add_to_map(sym_map, level, s):
            return ''
          result += level
        elif s in following:
          if not (self.add_to_map(sym_map, 10*level, s) and \
                  self.add_to_map(sym_map, level, t)):
            return ''
          sym_map[5*level] = '_'
          result += 9*level
          i += 1
        else:
          if not (self.add_to_map(sym_map, 5*level, s) and \
                  self.add_to_map(sym_map, level, t)):
            return '' 
          result += 4*level
          i += 1
      i += r
      level *= 10
    sym_array = ''.join([sym_map[k] for k in sorted(sym_map)])[::-1]
    return '{} using {}'.format(result, sym_array)
  
  def add_to_map(self, m, k, v):
    if (k in m.keys() and m[k] != v) or \
    (v in m.values() and (k, v) not in m.items()):
      return False
    else:
      m[k] = v
      return True
        
######################## Program class ################################
class Program:
  msg_wait_command = 'How can I help you? '
  msg_input_invalid = 'Sorry, I don\'t get what you want.'
  msg_input_error = 'Hey, ask me something that\'s possible to do!'
  msg_answer = 'It is'
  valid_tk1, valid_tk2, valid_tk3= 'Please convert', 'using', 'minimally'
  
  def __init__(self):
    self.instruction = ''
    self.tokens = []
    
  def run(self):
    self.instruction = input(Program.msg_wait_command)
    self.tokens = self.instruction.split()
    if not self.input_valid():
      print(Program.msg_input_invalid)
    else:
      ans = ''
      if len(self.tokens) == 3:
        c = Converter(self.tokens[2])
        ans = c.convert()
      elif len(self.tokens) == 4:
        c = Converter(self.tokens[2], '')
        ans = c.min_convert()
      else:
        c = Converter(self.tokens[2], self.tokens[4])
        ans = c.convert()
      if not ans:
        print(Program.msg_input_error)
      else:
        print(Program.msg_answer, ans)
      
  def input_valid(self):
    words_count = len(self.tokens)
    if words_count > 5 or words_count < 3:
      return False
    if ' '.join(self.tokens[:2]) != Program.valid_tk1:
      return False
    if words_count == 4 and self.tokens[3] != Program.valid_tk3:
      return False
    if words_count == 5 and self.tokens[3] != Program.valid_tk2:
      return False
    return True
  
######################## Program execute ################################
p = Program()
p.run()
