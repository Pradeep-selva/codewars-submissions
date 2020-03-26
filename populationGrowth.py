def nb_year(p0, percent, aug, p):
    years=0
    rate= percent/100.0
    while(p0<p):
        print("{}+{}*{}+{}= ".format(p0,rate,p0,aug))
        p0=p0+(rate*p0)+aug
        print(p0)
        years+=1

    return years

print(nb_year(1500, 5, 100, 5000))