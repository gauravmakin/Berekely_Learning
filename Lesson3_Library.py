public_var = 12
_private_var = 34

__all__ = ['public_var', '_private_var']

def public_func():
    sum_pub_priv = public_var + _private_var
    print("Public. The sum is {}".format(sum_pub_priv))

def _private_func():
    print('This is a private function')
    
class public_class:
    print("This is a public class")
class _private_class():
    print("This is a private class")


#public_func()