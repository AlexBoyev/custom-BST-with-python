'''
alexander boyev 314393158
genady yolgin 321983413
'''

def inches_to_meters(x=1):
    ''' convert inches to meters '''
    return  x * 0.0254

def inches_to_feets(x=1):
    ''' convert inches to feets '''
    return x * (1/12)

def miles_to_feets(x=1):
    ''' convert miles to feets '''
    return x * 5280

def composition(f1,f2):
    ''' convert compose two functions '''
    return lambda x: f1(f2(x))

def opposite(f):
    ''' convert opposite the convertion '''
    return lambda x: x/f(x=1)

feets_to_inches = opposite(inches_to_feets)
miles_to_inches = composition(feets_to_inches, miles_to_feets)
miles_to_meters = composition(inches_to_meters,miles_to_inches)
inches_to_miles =  opposite(miles_to_inches)
feets_to_miles = opposite(miles_to_feets)
feets_to_meters = composition(miles_to_meters,feets_to_miles)
meters_to_miles = opposite(miles_to_meters)
meters_to_feets = opposite(feets_to_meters)
meters_to_inches = opposite(inches_to_meters)

'''
#1 
print(meters_to_inches(10))
print(meters_to_feets(10))
print(meters_to_miles(10))
print(feets_to_meters(10))
print(feets_to_miles(10))
print(inches_to_miles(10))
print(miles_to_meters(10))
print(feets_to_inches(10))
print(miles_to_inches(10))
'''

def make_class(attrs, base=None):
    '''Return a new class (a dispatch dictionary) with given class attributes'''

    
    # Getter: class attribute (looks in this class, then base)
    def get(name):
        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)

    # Setter: class attribute (always sets in this class)
    def set(name, value):
        attrs[name] = value


    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):
            attrs[name] = value

        # instance dictionary
        obj = {'get': get, 'set': set}

        # calls constructor if present
        init = get('__init__')
        if init: init(*args)

        return obj

    # class dictionary
    
    cls = {'get': get, 'set': set, 'new': new}
    return cls

def make_feets_class():
    '''Return a new class (a dispatch dictionary) with given class attributes'''
    __type__ = 'Feets'
    
    def __init__(self,value):
        ''' constructor function '''
        if type(value) == str:
            temp = value.split(" ")
            try:
                float(temp[0])
            except Exception:
                raise Exception('format error: {0}'.format(value))
            if temp[1] != 'ft':
                raise Exception('format error: {0}'.format(value))
            self['set']('value',float(temp[0]))
        elif type(value) == float or type(value) == int:
            self['set']('value',float(value))
        else:
            raise Exception('Type error: {0}'.format(type(value)))
    
    def __str__(self):
        ''' str function '''
        return '{0} ft'.format(self['get']('value'))

    def __repr__(self):
        ''' repr function '''
        return 'Feets[{0}]({1})'.format("'new'",self['get']('value'))
    
    return  make_class({'__init__':__init__, '__repr__':__repr__, '__str__':__str__,'__type__':__type__})

def make_miles_class():
    '''Return a new class (a dispatch dictionary) with given class attributes'''
    __type__ = 'Miles'

    def __init__(self,value):
        ''' constructor function '''
        if type(value) == str:
            temp = value.split(" ")
            try:
                float(temp[0])
            except Exception:
                raise Exception('format error: {0}'.format(value))
            if temp[1] != 'mi':
                raise Exception('format error: {0}'.format(value))
            self['set']('value',float(temp[0]))
        elif type(value) == float or type(value) == int:
            self['set']('value',float(value))
        else:
            raise Exception('Type error: {0}'.format(type(value)))
    
    def __str__(self):
        ''' str function '''
        return '{0} mi'.format(self['get']('value'))

    def __repr__(self):
        ''' repr function '''
        return 'Miles[{0}]({1})'.format("'new'",self['get']('value'))

    return  make_class({'__init__':__init__, '__repr__':__repr__, '__str__':__str__,'__type__':__type__})

def to_str(obj):
    ''' to string generic function '''
    if type(obj) == dict:
        return obj['get']('__str__')()
    else:
        return obj.__str__()
 
def to_repr(obj):
    '''dict repr generic function '''
    if type(obj) == dict:
        return obj['get']('__repr__')()
    if obj == None:
        return None
    else:
        return obj.__repr__() 

def type_of(obj):
    ''' type of X function '''
    if type(obj) == dict:
        return obj['get']('__type__')
    elif type(obj) == str:
        return str
    else:
        return type(obj)
        
class Inches:
    ''' python Inches class '''
    value = None
    
    def __init__(self,param):
        ''' constructor '''
        if type(param) == str:
            temp = param.split(" ")
            try:
                float(temp[0])
            except Exception:
                raise Exception('format error: {0}'.format(param))
            if temp[1] != 'in':
                raise Exception('format error: {0}'.format(param))
            self.value = float(temp[0])
        elif type(param) == float or type(param) == int:
            self.value = float(param)
        else:
            raise Exception('Type error: {0}'.format(type(param)))
    
    def __str__(self):
        ''' str '''
        return '{0} in'.format(self.value)
    
    def __repr__(self):
        ''' repr ''' 
        return 'Inches({0})'.format(self.value)
                 
class Meters:
    '''python meters classs '''
    value = None
    
    def __init__(self,param):
        ''' constructor  '''
        if type(param) == str:
            temp = param.split(" ")
            try:
                float(temp[0])
            except Exception:
                raise Exception('format error: {0}'.format(param))
            if temp[1] != 'm':
                raise Exception('format error: {0}'.format(param))
            self.value = float(temp[0])
        elif type(param) == float or type(param) == int:
            self.value = float(param)
        else:
            raise Exception('Type error: {0}'.format(type(param)))
    
    def __str__(self):
        ''' str '''
        return '{0} m'.format(self.value)
    
    def __repr__(self):
        ''' repr '''
        return 'Meters({0})'.format(self.value)

'''
#2 (1)
for v in [25.8, "25.8 in", "25.8 ft", [], Inches]:
    try:
        print(str(Inches(v)))
    except Exception as e:
        print(e)
       
print(str(Inches(25.8)))
print(str(Meters(25.8)))
print(repr(Inches(25.8)))
print(repr(Meters(25.8)))
print(str(eval(repr(Inches(25.8)))))
print(str(eval(repr(Meters(25.8)))))
m = eval(repr(Meters(25.8)))
print(m.value)

for v in [25.8, "25.8 in", "25.8 m", [], Inches]:
    try:
        print(str(Meters(v)))
    except Exception as e:
        print(e)
'''

'''
#2 (2)
Feets = make_feets_class()
f = Feets['new']('25.8 ft')
print(f['get']('__str__')())
print(to_str(f))
print(f['get']('__repr__')())
print(to_repr(f))
Miles = make_miles_class()
m = Miles['new'](25.8)
print(m['get']('__str__')())
m = eval(to_repr(Miles['new'](25.8)))
print(m['get']('value'))
print(to_repr(Inches(25.8)))
'''

def add_Inches(x,y):
    ''' return repr after adding inches'''
    return to_repr(Inches(x.value + y.value))

def add_Meters(x,y):
    ''' return repr after adding meters'''
    return to_repr(Meters(x.value + y.value))

def add_Meters_Inches(x,y):
    '''return repr after adding meters and inches'''
    return to_repr(Meters(x.value + inches_to_meters(y.value)))

def add_Inches_Meters(x,y):
    ''' return repr after adding inches and meters'''
    return to_repr(Inches(x.value + meters_to_inches(y.value)))

def sub_Inches(x,y):
    ''' return repr after subing inches'''
    return to_repr(Inches(x.value - y.value))

def sub_Meters(x,y):
    ''' return repr after subing meters'''
    return to_repr(Meters(x.value - y.value))

def sub_Meters_Inches(x,y):
    ''' return repr after subing meters and inches'''
    return to_repr(Meters(x.value - inches_to_meters(y.value)))

def sub_Inches_Meters(x,y):
    ''' return repr after subing inches and meters'''
    return to_repr(Inches(x.value - meters_to_inches(y.value)))

def apply(operator_name, x, y):
    ''' apply function, bulild key to use the dictionary '''
    if operator_name == '>':
        operator_name = 'gt'
    if operator_name == '==':
        operator_name = 'eq'
    if type(x) == dict and type(y) == dict:
        tags = (x['get']('__type__'),y['get']('__type__'))
    elif type(x) == dict and type(y) != dict:
        tags = (x['get']('__type__'), type_tag(y))
    elif type(x) != dict and type(y) == dict:
        tags = (type_tag(x),y['get']('__type__'))
    else:
        tags = (type_tag(x),type_tag(y))
    
    key = (operator_name, tags)
    return apply.implementations[key](x, y)

def coerce_apply(operator_name, x, y):
    ''' coere apply function to correct the key '''
    tx = type_tag(x)  #inch
    ty =  type_tag(y) #meters
    if tx != ty:
        if (tx, ty) in coercions:
            y.value = coercions[(tx, ty)](y.value) # x = inches_to_meters value
            ty = tx 
        elif (ty, tx) in coercions:
            x.value = coercions[(ty, tx)](x.value) 
            tx = ty  
        else:
            return 'No coercion possible.'
    else:
        
        if tx == 'Meters':
            key = (operator_name, tx)
            return coerce_apply.implementations[key](x, y)
        elif tx == 'Inches':
            y.value = coercions[(tx, ty)](y.value)
            x.value = coercions[(ty, tx)](x.value)
            tx = 'Meters'
            key = (operator_name, tx)
            return coerce_apply.implementations[key](x, y)
        else:
            return 'No coercion possible.'

    assert tx == ty
    key = (operator_name, tx)
    return coerce_apply.implementations[key](x, y)

def type_tag(x):
    ''' return type of  x '''
    return type_tag.tags[type(x)]

def add_Feets(x,y):
    ''' return feet object after adding feets'''
    feets = make_feets_class()
    feet = feets['new'](x['get']('value')+y['get']('value'))
    return feet

def add_Miles(x,y):
    ''' return shmyton miles object after adding '''
    miles = make_miles_class()
    mile = miles['new'](x['get']('value')+y['get']('value'))
    return mile

def add_Feets_Miles(x,y):
    feets = make_feets_class()
    feet = feets['new'](x['get']('value')+miles_to_feets(y['get']('value')))
    return feet

def add_Miles_Feets(x,y):
    ''' return miles object after adding  miles + feets '''
    miles = make_miles_class()
    mile = miles['new'](x['get']('value')+feets_to_miles(y['get']('value')))
    return mile

def sub_Feets(x,y):
    ''' return shmyton object after subbing feets '''
    feets = make_feets_class()
    feet = feets['new'](x['get']('value')-y['get']('value'))
    return feet

def sub_Miles(x,y):
    ''' return miles object after subbing miles '''
    miles = make_miles_class()
    mile = miles['new'](x['get']('value')-y['get']('value'))
    return mile

def sub_Feets_Miles(x,y):
    ''' return feets object after subbing feets adn miles '''
    feets = make_feets_class()
    feet = feets['new'](x['get']('value')-miles_to_feets(y['get']('value')))
    return feet  
  
def sub_Miles_Feets(x,y):
    ''' return miles object after subbing miles and feets '''
    miles = make_miles_class()
    mile = miles['new'](x['get']('value')-feets_to_miles(y['get']('value')))
    return mile

def greater(x,y):
    ''' greater function, defines which object value is greater '''
    
    if type(x) == dict and type(y) == dict:
        
        if x['get']('__type__') == 'Feets':
            if y['get']('__type__') == 'Feets':
                return x['get']('value') > y['get']('value')
            else:
                return x['get']('value') > miles_to_feets(y['get']('value'))
        else:
            if y['get']('__type__') == 'Miles':
                return x['get']('value') > y['get']('value')
            else:
                return x['get']('value') > feets_to_miles(y['get']('value'))
            
    elif type(x) == dict and type(y) != dict:
        if x['get']('__type__') == 'Feets':
            if type_tag(y) == 'Inches':
                return x['get']('value') > inches_to_feets(y.value)
            else:
                return x['get']('value') > meters_to_feets(y.value)
        else:
            if type_tag(y) == 'Inches':
                return x['get']('value') > inches_to_miles(y.value)
            else:
                return x['get']('value') > meters_to_miles(y.value)
            
    elif type(x) != dict and type(y) == dict:
        
        if y['get']('__type__') == 'Feets':
            if type_tag(x) == 'Inches':
                return y['get']('value') < inches_to_feets(x.value)
            else:
                return y['get']('value') < meters_to_feets(x.value)
        else:
            if type_tag(x) == 'Inches':
                return y['get']('value') < inches_to_miles(x.value)
            else:
                return y['get']('value') < meters_to_miles(x.value)
    else:
        if type_tag(x) == type_tag(y):
            return x.value > y.value
        else:
            if type_tag(x) == 'Inches':
                return x.value > meters_to_inches(y.value)
            else:
                return x.value > inches_to_meters(y.value)
                 
def equal(x,y):
    ''' defines if 2 object values area equel '''
    if type(x) == dict and type(y) == dict:
        
        if x['get']('__type__') == 'Feets':
            if y['get']('__type__') == 'Feets':
                return x['get']('value') == y['get']('value')
            else:
                return x['get']('value') == miles_to_feets(y['get']('value'))
        else:
            if y['get']('__type__') == 'Miles':
                return x['get']('value') == y['get']('value')
            else:
                return x['get']('value') == feets_to_miles(y['get']('value'))
            
    elif type(x) == dict and type(y) != dict:
        if x['get']('__type__') == 'Feets':
            if type_tag(y) == 'Inches':
                return x['get']('value') == inches_to_feets(y.value)
            else:
                return x['get']('value') == meters_to_feets(y.value)
        else:
            if type_tag(y) == 'Inches':
                return x['get']('value') == inches_to_miles(y.value)
            else:
                return x['get']('value') == meters_to_miles(y.value)
            
    elif type(x) != dict and type(y) == dict:
        
        if y['get']('__type__') == 'Feets':
            if type_tag(x) == 'Inches':
                return y['get']('value') == inches_to_feets(x.value)
            else:
                return y['get']('value') == meters_to_feets(x.value)
        else:
            if type_tag(x) == 'Inches':
                return y['get']('value') == inches_to_miles(x.value)
            else:
                return y['get']('value') == meters_to_miles(x.value)
    else:
        if type_tag(x) == type_tag(y):
            return x.value == y.value
        else:
            if type_tag(x) == 'Inches':
                return x.value == meters_to_inches(y.value)
            else:
                return x.value == inches_to_meters(y.value)
    
type_tag.tags = {Inches: 'Inches', Meters: 'Meters',make_feets_class:'Feets', make_miles_class:'Miles'}

apply.implementations = {}

apply.implementations['add',('Inches', 'Inches')] = add_Inches
apply.implementations['add',('Meters', 'Meters')] = add_Meters
apply.implementations['add',('Meters', 'Inches')] = add_Meters_Inches
apply.implementations['add',('Inches', 'Meters')] = add_Inches_Meters
apply.implementations['sub',('Inches', 'Inches')] = sub_Inches
apply.implementations['sub',('Meters', 'Meters')] = sub_Meters
apply.implementations['sub',('Meters', 'Inches')] = sub_Meters_Inches
apply.implementations['sub',('Inches', 'Meters')] = sub_Inches_Meters

apply.implementations['add',('Feets', 'Feets')] = add_Feets
apply.implementations['add',('Miles', 'Miles')] = add_Miles
apply.implementations['add',('Feets', 'Miles')] = add_Feets_Miles
apply.implementations['add',('Miles', 'Feets')] = add_Miles_Feets
apply.implementations['sub',('Feets', 'Feets')] = sub_Feets
apply.implementations['sub',('Miles', 'Miles')] = sub_Miles
apply.implementations['sub',('Feets', 'Miles')] = sub_Feets_Miles
apply.implementations['sub',('Miles', 'Feets')] = sub_Miles_Feets

apply.implementations['gt',('Inches', 'Inches')] = greater
apply.implementations['gt',('Inches', 'Miles')] = greater
apply.implementations['gt',('Inches', 'Meters')] = greater
apply.implementations['gt',('Inches', 'Feets')] = greater
apply.implementations['gt',('Miles', 'Miles')] = greater
apply.implementations['gt',('Miles', 'Meters')] = greater
apply.implementations['gt',('Miles', 'Feets')] = greater
apply.implementations['gt',('Miles', 'Inches')] = greater
apply.implementations['gt',('Meters', 'Miles')] = greater
apply.implementations['gt',('Meters', 'Meters')] = greater
apply.implementations['gt',('Meters', 'Feets')] = greater
apply.implementations['gt',('Meters', 'Inches')] = greater
apply.implementations['gt',('Feets', 'Miles')] = greater
apply.implementations['gt',('Feets', 'Meters')] = greater
apply.implementations['gt',('Feets', 'Feets')] = greater
apply.implementations['gt',('Feets', 'Inches')] = greater

apply.implementations['eq',('Inches', 'Inches')] = equal
apply.implementations['eq',('Inches', 'Miles')] = equal
apply.implementations['eq',('Inches', 'Meters')] = equal
apply.implementations['eq',('Inches', 'Feets')] = equal
apply.implementations['eq',('Miles', 'Miles')] = equal
apply.implementations['eq',('Miles', 'Meters')] = equal
apply.implementations['eq',('Miles', 'Feets')] = equal
apply.implementations['eq',('Miles', 'Inches')] = equal
apply.implementations['eq',('Meters', 'Miles')] = equal
apply.implementations['eq',('Meters', 'Meters')] = equal
apply.implementations['eq',('Meters', 'Feets')] = equal
apply.implementations['eq',('Meters', 'Inches')] = equal
apply.implementations['eq',('Feets', 'Miles')] = equal
apply.implementations['eq',('Feets', 'Meters')] = equal
apply.implementations['eq',('Feets', 'Feets')] = equal
apply.implementations['eq',('Feets', 'Inches')] = equal

coerce_apply.implementations = {}

coerce_apply.implementations[('sub','Meters')] = sub_Meters
coerce_apply.implementations[('add','Meters')] = add_Meters

coercions = {('Meters', 'Inches'): inches_to_meters,('Inches', 'Inches'): inches_to_meters}

'''
#3 (1)
print(apply('add', Inches(1), Meters(1.5)))
print(apply('add', Meters(1.5), Inches(1)))
print(apply('sub', Inches(1), Meters(1.5)))
print(apply('sub', Meters(1.5), Inches(1)))
'''

'''
#3 (2)
Feets = make_feets_class()
Miles = make_miles_class()
print(to_repr(apply('add', Feets['new'](1.5), Miles['new'](1))))
print(to_repr(apply('add',Miles['new'](1), Feets['new'](1.5))))
print(to_repr(apply('sub', Feets['new'](1.5), Miles['new'](1))))
print(to_repr(apply('sub',Miles['new'](1), Feets['new'](1.5))))
'''

'''
#3 (3)
Miles = make_miles_class()
Feets = make_feets_class()
print(to_repr(apply('gt', Miles['new'](1), Inches(1.5))))
print(to_repr(apply('gt', Inches(1.5), Miles['new'](1))))
print(to_repr(apply('>', Feets['new'](1), Inches(1.5))))
print(to_repr(apply('>', Inches(1.5), Feets['new'](1))))
print(to_repr(apply('eq', Feets['new'](1), Inches(feets_to_inches(1)))))
print(to_repr(apply('eq', Inches(1.5), Feets['new'](inches_to_feets(1.5)))))
print(to_repr(apply('==', Feets['new'](1), Inches(1.5))))
print(to_repr(apply('==', Inches(1.5), Feets['new'](1))))
'''

'''
# 3 (4)
print(coerce_apply('add', Meters(1.5), Inches(1)))
print(coerce_apply('add', Inches(1), Meters(1.5)))
print(coerce_apply('sub', Meters(1), Inches(1.5)))
print(coerce_apply('sub', Inches(1.5), Meters(1)))
'''

class ValueExistsException(Exception):
    ''' exception if value already inside the tree '''
    def __init__ (self,x):
        '''constructor '''
        raise Exception('Same Value Exists: {0}'.format(x))

class ValueNotExistsException(Exception):
    '''exception if the value doesnt exist '''
    def __init__ (self,x):
        ''' constructor '''
        raise Exception('Value Not Exists: {0}'.format(to_repr(x)))

class EmptyTreeException(Exception):
    ''' exception while the tree is empty '''
    def __init__ (self):
        ''' constructor '''
        raise Exception('The Tree Is Empty')
 
class TreeNode:
    ''' TreeNode class '''     
    def __init__(self,obj=None,parent=None):
        ''' constructor '''
        self.value = obj
        self.left = None
        self.right = None
        self.parent = parent
        
    def search(self,key):
        ''' search key in treenode'''
        if self.value == None:
            raise EmptyTreeException()
        
        if apply('gt',self.value,key):
            if self.left == None:
                return None
            self = self.left.search(key)
              
        elif apply('gt',key,self.value):
            if self.right == None:
                return None
            self = self.right.search(key)
                
        elif apply('eq',key,self.value):
            return self
        
        return self
    
    def insert(self, obj):
        '''insert nodes into the tree '''
        if self.value == None:
            self.value = obj
        elif apply('gt',self.value,obj):
            if self.left:
                self.left.insert(obj)
            else:
                self.left = TreeNode(obj)
        elif apply('gt',obj,self.value):   
            if self.right:
                self.right.insert(obj)
            else:
                self.right = TreeNode(obj) 
        else:
            raise ValueExistsException(obj)
        
        return self
      
    def __str__(self):
        ''' str '''
        temp = to_repr(self.value)
        if self.right == None:
            if to_repr(self.left):
                temp = temp + ',left={0}'.format(to_repr(self.left))
        elif self.left == None:
            if to_repr(self.right):
                temp = temp + ',right={0}'.format(to_repr(self.right))
        else:
            if to_repr(self.right) and to_repr(self.left):
                temp = temp + ',left={0},right={1}'.format(to_repr(self.left),to_repr(self.right))
        return 'TreeNode({0})'.format(temp)
        
    def __repr__(self): 
        ''' repr '''
        temp = to_repr(self.value)
        if self.right == None:
            if to_repr(self.left):
                temp = temp + ',left={0}'.format(to_repr(self.left))
        elif self.left == None:
            if to_repr(self.right):
                temp = temp + ',right={0}'.format(to_repr(self.right))
        else:
            if to_repr(self.right) and to_repr(self.left):
                temp = temp + ',left={0},right={1}'.format(to_repr(self.left),to_repr(self.right))
        return 'TreeNode({0})'.format(temp)
    
    def successor(self):
        ''' return successor key'''
        key = self
        while key.left is not None:
            key = key.left
        return key
    
    def delete(self, key):
        '''detele node function '''
        if not self:
            return self
        if apply('gt',self.value,key):
            self.left = self.left.delete(key)
        elif apply('gt',key,self.value):
            self.right = self.right.delete(key)
        else:
            if self.left is None:
                node1 = self.right
                self = None
                return node1
            elif self.right is None:
                node1 = self.left
                self = None
                return node1
            node1 = self.right.successor()
            self.value = node1.value
            self.right = self.right.delete(node1.value)
        return self
 
    def height(self):
        ''' treenode height '''
        if self is None:
            return 0
        else:
            if self.left is not None:
                l=self.left.height()
            else:
                l=0
            if self.right is not None:
                r=self.right.height()
            else:
                r=0
            return 1 + l if l>=r else r  
           
    def in_order(self,sortedlist=[]):
        ''' inorder function '''
        if self != None:
            if self.left != None:
                self.left.in_order(sortedlist)
            sortedlist.append(self.value)
            if self.right != None:
                self.right.in_order(sortedlist)
        return sortedlist
    
class BSTree:
    ''' BSTtree class '''
    def delete(self,key):
        '''BST delete key'''
        if self.root.value is None:
            raise EmptyTreeException()
        if type(key) == list or type(key) == tuple:
            for i in range(len(key)):
                if self.search(key[i]) is None:
                    raise ValueNotExistsException(key[i])
                else:
                    self.root.delete(key[i])
                    
        else:
            if self.search(key) is None:
                raise ValueNotExistsException(key)
        return self.root.delete(key)
     
    def height(self):
        ''' treenode height '''
        if self is None:
            return 0
        else:
            if self.root.left is not None:
                l=self.root.left.height()
            else:
                l=0
            if self.root.right is not None:
                r=self.root.right.height()
            else:
                r=0
            return 1 + l if l>=r else r 
    
    def in_order(self):
        ''' BST inorder function '''
        if self.root.value == None:
            raise EmptyTreeException()
        sortedlist = []
        return self.root.in_order(sortedlist)
    
    def search(self,key):
        '''search specific key'''
        if self.root == None:
            raise EmptyTreeException()
        while self.root != None:
            if apply('gt',self.root.value,key):
                self.root = self.root.left
            elif apply('gt',key,self.root.value):
                self.root = self.root.right
            else:
                return self.root
        return None
            
    def __init__(self):
        ''' constructor '''
        self.root = None
        
    def insertroot(self,value):
        ''' insert root into the tree '''
        self.root = TreeNode(value) 

    def insert(self,value):
        ''' insert node '''
        if type(value) == list or type(value) == tuple:
            for i in range(len(value)):
                if self.root == None:
                    self.insertroot(value[i])
                else:
                    self.root.insert(value[i])
        else:
            if self.root == None:
                self.insertroot(value)
            else:
                self.root.insert(value)
        
        return self.root
    
    def __str__(self):
        ''' str '''
        return 'BSTree({0})'.format(self.root)
    
    def __repr__(self):
        ''' repr '''
        return 'BSTree({0})'.format(self.root)

'''
ex 4
Miles = make_miles_class()
Feets = make_feets_class()
tree = BSTree()
print(tree)
tree.insert(Meters(10))
tree.insert(Inches(10))
tree.insert(Feets['new'](10)) 
tree.insert(Miles['new'](10)) 
print(tree)
print(tree.in_order())
print('-- in order print after insert ------------------------------')
for v in tree.in_order():
    if (isinstance(v, dict)):
        print(v['get']('__str__')(), end=" = ")
        print()
    else:
        print(v, end=" = ")
        print(apply('add', Meters(0), v))
tree.delete(Meters(10))
print('-- in order print after delete ------------------------------')
for v in tree.in_order():
    if (isinstance(v, dict)):
        print(v['get']('__str__')(), end=" = ")
        print()
    else:
        print(v, end=" = ")
        print(apply('add', Meters(0), v))
'''
