# Варіянт 8
# Чи є рядок капсом?

# Вбудований метод - isupper()


UP_ALPH = list(map(chr, range(65, 91))) + [" "]

def is_uppercase (str):
    isUpBoolean = True
    
    for str_ch in str:
        if str_ch in UP_ALPH:
            continue
        else:
            isUpBoolean = False
    
    print("\"", str, "\" is uppercase:", isUpBoolean)
    
is_uppercase("YOUR TEXT HERE")