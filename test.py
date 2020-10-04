def countAndSay(n: int) -> str:
    count = 1
    cs = "1"
    
    for _ in range(n-count):
        cs_new = ""
        while cs:
            d = cs[0]
            d_count = 0
            for d_i in cs:
                if d_i == d:
                    d_count += 1
                else:
                    break
            cs_new += str(d_count)+d
            cs = cs[d_count:]
        cs = cs_new
        print(cs)
        
    return cs

print(countAndSay(5))