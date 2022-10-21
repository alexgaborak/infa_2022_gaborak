def reduce_last_digit(schislo):
    if schislo.count('.') == 0:
        return str(int(schislo)-1)
    else:
        dot_pos = schislo.find('.')
        digits = len(schislo) - 1

        schislo = schislo.replace('.', '')
        chislo = int(schislo)

        chislo = chislo - 1
        return str(chislo/(10**(digits - dot_pos)))
