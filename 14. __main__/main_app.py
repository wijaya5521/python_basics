# __main__ define this file is main program in python
'''
main program in other language programming
- C/C++
int main() {
    
}

- in Java
Class main() {
    static void main(){
        
    }
} 
'''

# cek is this file is main program?
# print(__name__)

'''
output :

__main__

'''

import functions

print(f"__name__ dari file main_app.py adalah {__name__}")

'''
when running main_app.py as main program
' python main_app.py' in console

output : 
__name__ dari file functions.py adalah functions
__name__ dari file main_app.py adalah __main__

----------------------------------------------------

when running funtions.py as main program
' python functions.py' in console

output : 
__name__ dari file functions.py adalah __main__

'''