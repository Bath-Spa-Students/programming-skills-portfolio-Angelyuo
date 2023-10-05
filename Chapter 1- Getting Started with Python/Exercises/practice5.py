print("""Repeat after me!
      """)
while True:
    i = input("I... ")
    if i.upper() == "I":
        l = input("Love... ")
        if l.upper() == "LOVE":
            b = input("Bath... ")
            if b.upper() == "BATH":
                s = input("Spa... ")
                if s.upper() == "SPA":
                    print(i,l,b,s)
                    break