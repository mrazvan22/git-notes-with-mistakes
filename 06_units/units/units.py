

class Unit(object):

  def load_units_from_config(filename):
    value_dict = {}
    SI_dict = {}
    with open(filename, 'r') as f:
      next(f)
      for line in f:
        #print line
        [key, value, SI_unit] = line.split(' ')
        value_dict[key] = float(value)
        SI_dict[key] = SI_unit[:-1]

    return [value_dict, SI_dict]

  [value_map, SI_map] = load_units_from_config('units/units.yaml')

  def __init__(self, unit, value):
    if(unit in Unit.value_map.keys()):
      self.unit = unit
      self.value = value
    else:
      raise(Exception)

  def get_SI_unit(self):
    return Unit.SI_map[self.unit]

  def add(self, other_unit):
    new_unit = Unit(self.unit, self.value)
    try:
      # if input is number convert to unit first
      float(other_unit)
      other_unit = Unit(self.unit, other_unit)
    except Exception:
      pass

    if (other_unit.unit == self.unit):
      new_unit.value += other_unit.value
    else:
      if (Unit.units_compatible(self.unit, other_unit.unit)):
        new_unit.unit = self.get_SI_unit()
        new_unit.value = self.to_SI().value + other_unit.to_SI().value
      else:
        raise(IncompatibleUnitsError(other_unit.unit, self.unit))

    return new_unit

  def multiply(self, other_unit):
    new_unit = Unit(self.unit, self.value)
    try:
      # if input is number convert to unit first
      float(other_unit)
      other_unit = Unit(self.unit, other_unit)
    except Exception:
      pass

    if (other_unit.unit == self.unit):
      new_unit.value *= other_unit.value
    else:
      if (Unit.units_compatible(self.unit, other_unit.unit)):
        new_unit.unit = self.get_SI_unit()
        new_unit.value = self.to_SI().value * other_unit.to_SI().value
      else:
        raise(IncompatibleUnitsError(other_unit.unit, self.unit))

    return new_unit

  def equal(self, other_unit):
    if (Unit.units_compatible(self.unit, other_unit.unit)):
      return abs(self.to_SI().value - other_unit.to_SI().value) < 0.00001
    else:
      raise(IncompatibleUnitsError(other_unit.unit, self.unit))


  def __radd__(self, other):
    return self.__add__(other)

  def __rmul__(self, other):
    return self.__mul__(other)

  def __add__(self, other):
    return self.add(other)

  def __mul__(self, other):
    return self.multiply(other)

  def __eq__(self, other):
    return self.equal(other)

  def to(self, new_unit_label):
    if(new_unit_label in Unit.value_map.keys()):
      return Unit(new_unit_label, self.value * Unit.value_map[self.unit] / Unit.value_map[new_unit_label])
    else:
      raise(IncompatibleUnitsError(new_unit_label, self.unit))


  def to_SI(self):
    return self.to(self.get_SI_unit())

  def get_unit(self):
    return self.unit

  @staticmethod
  def units_compatible(unit1, unit2):
    return (Unit.SI_map[unit1] == Unit.SI_map[unit2])


class Time(Unit):
  def __init__(self, unit, value):
    self.super(unit,value)

class Length(Unit):
  def __init__(self, unit, value):
    self.super(unit,value)


class IncompatibleUnitsError(Exception):
  def __init__(self, unit1, unit2):
    self.unit1 = unit1
    self.unit2 = unit2
  def __str__(self):
    return "Incompatible units " + unit1 + ", " + unit2 + "\n"


#Unit.load_units_from_config('units.yaml')

def main():
  a = Unit('meters', 1)
  a = a + 1
  print a.unit
  print a.value
  

if __name__ == "__main__":
  main()

