print('Hello, Django girls!')
#print(2 + 2)
if (3<2):
    print("Soy un idiota")
else:
    print("me estoy divirtiendo")

def hi():
    print('Hi there!')
    print('How are you?')

hi()

def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi("x")

def hi(name):
    print('Bien o no ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('\n')

for i in range(1, 11):
    n = 5
    print(i*n)