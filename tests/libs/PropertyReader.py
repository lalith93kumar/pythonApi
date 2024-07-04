import yaml
from yaml.loader import SafeLoader
import os

class PropertyReader(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(PropertyReader, cls).__new__(cls)
      if os.environ.get('yml_name')!=None:
      	file_name = os.environ.get('yml_name')
      else:
      	file_name = "properties.yaml"
      with open('./' + file_name) as f:
      	cls.data = yaml.load(f, Loader=SafeLoader)
    return cls.instance

def getInstance():
  return PropertyReader();