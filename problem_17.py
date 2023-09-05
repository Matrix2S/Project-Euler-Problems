
z1 = ["one","two","three","four","five","six","seven","eight","nine"]
z2 = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
z3 = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

one2nine = len("".join(z1))
one2nineteen = one2nine + len("".join(z2))                                      # +10 To 19
one2ninetynine = one2nineteen + len("".join(z3))*10 + len("".join(z1))*8        # +20 To 99


oneTo999 = len("".join(z1))*100 + len("hundred")*900 + len("and")*891 + one2ninetynine*10
total = oneTo999 + len("onethousand")

print(total)

