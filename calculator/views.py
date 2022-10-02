from django.shortcuts import render

# Create your views here.

def round_arr(lst, n):

    for d in range(len(lst)):
        lst[d] = [round(x, n) for x in lst[d]]
    
    return lst


def index(response):
    
    n = ""
    vars = []
    res = []
    n1 = 0
    arr_src = []
    arr_res = []
    msg = ""
    steps = {}
    show_steps = False
    

    if response.method == "POST":
        if response.POST.get("generate"):
            if response.POST.get("variables") != "":
                n = int(response.POST.get("variables"))
                vars = list(range(1, n + 1))
                res =  list(range( n + 2))
                n1 = n+1

                for i in range(1, n+1):
                    dim = []
                    for j in range(1, n+2):
                        dim.append('')
                    arr_src.append(dim)

        if response.POST.get("run") or response.POST.get("steps"):

            if response.POST.get("steps"):
                show_steps = True

            try:
                n = int(response.POST.get("n"))
            except ValueError:
                msg = "No matrix identified"
                return render(response,
                    'calculator/index.html',
                    {'vars' : vars, 
                        'res' : res, 
                        'n': n, 
                        'n1' : n1,
                        'arr_src' : arr_src,
                        'arr_res' : arr_res,
                        'msg' : msg,
                        'steps': steps })
                
            vars = list(range(1, n + 1))
            res =  list(range( n + 2))
            n1 = n+1
            
            for i in range(1, n+1):
                dim = []
                for j in range(1, n+2):
                    xn = response.POST.get("e"+str(i)+"x"+str(j))
                    dim.append(xn)
                arr_src.append(dim)
                arr_res = arr_src.copy()

                for eqs in range(len(arr_res)):
                    arr_res[eqs] = list(map(float, arr_res[eqs]))
            try:
                step = 0
                for eq in range(len(arr_res)):
                    
                    if arr_res[eq][eq]  != 1:

                        round_arr(arr_res, 2)
                        
                        step += 1
                        det = "Divide Row "+str(eq+1)+" by "+str(arr_res[eq][eq])

                        arr_res[eq] = [x/arr_res[eq][eq] for x in arr_res[eq]]

                        round_arr(arr_res, 2)

                        steps["Step " + str(step)] = [det, arr_res.copy()]



                    for v in range(len(arr_res)):
                        if v != eq:
                        
                            step += 1

                            if arr_res[v][eq] == 1:
                                det = "Subtract Row "+str(v+1)+" with Row "+str(eq + 1)
                            elif arr_res[v][eq] == -1:
                                det = "Add Row "+str(v+1)+" with Row "+str(eq + 1)
                            elif arr_res[v][eq] > 1:
                                det = "Subtract Row "+str(v+1)+" with "+ str(arr_res[v][eq]) +" multiplied by Row "+str(eq + 1)
                            elif arr_res[v][eq] < -1:
                                det = "Add Row "+str(v+1)+" with "+ str(arr_res[v][eq] * (-1)) +" multiplied by Row "+str(eq + 1)

                            arr_res[v] = list(map(lambda x,y: x-(arr_res[v][eq])*y, arr_res[v], arr_res[eq] ))

                            round_arr(arr_res, 2)

                            steps["Step " + str(step)] = [det, arr_res.copy()]
                    
                        
            except ZeroDivisionError:
                msg = "The elimination process is terminated due to the existence of row with all zero members"

    arr_exp = [['1', '0', 'a13', 'a14', 'y1'],
               ['0', '1', 'a23', 'a24', 'y2'],
               ['0', '0', 'a33', 'a34', 'y3'],
               ['0', '0', 'a43', 'a44', 'y4'],
    ]

    arr_avo = [['a11', 'a12', 'a13', 'a14', 'y1'],
               ['a21', 'a22', '5', 'a24', 'y2'],
               ['a31', 'a32', '-5', 'a34', 'y3'],
               ['a41', 'a42', 'a43', 'a44', 'y4'],
    ]

    return render(response,
     'calculator/index.html',
     {'vars' : vars, 
        'res' : res, 
        'n': n, 
        'n1' : n1,
        'arr_src' : arr_src,
        'arr_res' : arr_res,
        'msg' : msg,
        'steps': steps,
        'len_res' : len(arr_res),
        'show_steps' : show_steps,
        'arr_exp' : arr_exp,
        'arr_avo' : arr_avo })