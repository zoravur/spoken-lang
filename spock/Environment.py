class Environment:
    # enclosing is the enclosing environment
    def __init__(self, enclosing=None):
        self._variables = {}
        self._enclosing = enclosing

    def get(self, var_name):
        if var_name in self._variables:
            return self._variables[var_name]
        elif self._enclosing:
            return self._enclosing.get(var_name)
        else:
            raise Exception(f"Variable '{var_name}' not defined")
        
    def set(self, var_name, value):
        if var_name in self._variables:
            self._variables[var_name] = value
        elif self._enclosing:
            self._enclosing.set(var_name, value)
        else:
            raise Exception(f"Variable '{var_name}' not declared")
        
    def declare(self, var_name):
        self._variables[var_name] = None

    def __str__(self):
        return f'Environment({self._variables}, enclosing={self._enclosing})'
    

if __name__ == '__main__':
    env = Environment()
    env.declare('x')
    env.set('x', 5)
    print(env.get('x'))
    env2 = Environment(env)
    env2.declare('y')
    env2.set('y', 10)
    print(env2.get('y'))
    print(env2)
    print(env2.get('x'))
    print(env.get('y'))
    print(env.get('z'))