

class Unit(object):

  def load_units_from_config(filename):
    value_dict = {}
    with open(filename, 'r') as f:
      for line in f:
        [key, value] = line.split(' ')
        value_dict[key] = float(value[:-1])

    return value_dict

  value_map = load_units_from_config('units.yaml')

  def __init__(self, unit, value):
    if(unit in Unit.value_map.keys()):
      self.unit = unit
      self.value = value
    else:
      raise(Exception)

  def add(self, other_unit):
    new_unit = Unit(self.unit, self.value)
    if (strcmp(other_unit.unit, self.unit) == 0):
      new_unit.value += other_unit.value
    else:
      if (units_compatible(self.unit, other_unit.unit)):
        new_unit.unit = get_SI_unit(self.unit)     
        new_unit.value = self.to(new_unit.unit).value +  
  
    return new_unit

  def to(self, new_unit_label):
    if(new_unit_label in Unit.value_map.keys()):
      return Unit(new_unit_label, self.value * Unit.value_map[self.unit] / Unit.value_map[new_unit_label])
    
  def get_unit(self):
    return self.unit



class Time(Unit):
  def __init__(self, unit, value):
    self.super(unit,value)

class Length(Unit):
  def __init__(self, unit, value):
    self.super(unit,value)


  
  

