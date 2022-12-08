from django.shortcuts import render
import json
from string import ascii_lowercase as letters


def print_data(formulas):
    for i in range(len(formulas)):
        print(f'{i}: {formulas[i]}')
    ind = int(input('enter formula number: '))
    return formulas[ind]


def get_input(formula):
    non_vars = ['sin', 'cos', 'tan']
    consts = {'g': '9.81', 'G': '(6.75 * (10**-11)'}

    temp = formula
    for x in non_vars:
        if x in temp:
            temp = temp.replace(x, '')

    for x in list(consts.keys()):
        if x in temp:
            temp = temp.replace(x, consts[x])

    var = [x for x in temp if x.lower() in letters]
    vals = {}
    for i in var:
        inp = float(input(f'{i}: '))
        vals[i] = inp

    for x in list(vals.keys()):
        formula = formula.replace(x, str(vals[x]))

    return formula



# Create your views here.
phys = ""


def index(request):
    return render(request, "brochure/index.html")


def cj(request):
    return render(request, 'brochure/class11/chemistry.html')

def mj(request):
    return render(request, 'brochure/class11/maths.html')

def ps(request):
    cha = 0
    if request.method == 'POST':
        cha = request.POST.get('phys')
        chap = int(cha)
        if chap == 5:
            print('chap 5 doesnt exist')
        request.session['chapter'] = f'Chapter_{chap}'
        print(request.session.get('chapter'))
        with open('/Users/rachit/PycharmProjects/cloud_brochure/brochure/data.json', 'r') as f:
            global data
            data = json.load(f)
            data = data[request.session.get('chapter')]
            print(data)

        formula = print_data(data)
        eq_to = formula.index('=')
        LHS = formula[:eq_to]
        RHS = formula[eq_to + 1:]

        print(f'{LHS} = {eval(get_input(RHS))}')
    return render(request, 'brochure/class12/physics.html')


def pj(request):
    print(data)
    return render(request, "brochure/class11/physics.html",{
        "formulas": data
    })

def cs(request):
    return render(request, 'brochure/class12/chemistry.html')

def ms(request):
    return render(request, 'brochure/class12/maths.html')

