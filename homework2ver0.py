P = float(input("մուտքագրեք վարկի գումարի չափը ———>"))
tokos = float(input("տարեկան տոկոսադրույքը % --->"))
i = float(tokos)/100
t = float(12)   # ամսեկանի համար տարին=12ամիսա
T = float(input("ժամկետը ամիս---->"))
n = float(T)/float(t)
l = P*n*i
S = float(P) + float(l)
print("ընդհանուր վճարված գումաը ժամկետի ավարտին կկազմի", S, ", որից", P, "-ը մայր գումար, իսկ", l, "տոկոսագումարը")
