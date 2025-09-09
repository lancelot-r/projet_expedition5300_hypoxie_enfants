def main():
    import sys
    n = int(sys.stdin.readline())
    
    # Cas trivial n=1 : pas de paires → toujours match nul
    if n == 1:
        print("0.000 1.000 0.000")
        return
    
    # On code les symboles O=1 (pile) et R=0 (face).
    # dp_prev[prev][d] = probabilité -- prev ∈ {0,1}, d = (X-Y) + offset
    offset = n  # pour indexer les différences d ∈ [-n..+n]
    size = 2*offset + 1
    dp_prev = [ [0.0]*size for _ in range(2) ]
    
    # Après le 1er lancer, pas de paire, probabilité 0.5 pour chacun des deux états
    dp_prev[0][offset] = 0.5  # prev = R (0), d = 0
    dp_prev[1][offset] = 0.5  # prev = O (1), d = 0
    
    # Itération pour chaque nouveau lancer
    for _ in range(2, n+1):
        dp_cur = [ [0.0]*size for _ in range(2) ]
        for prev in (0, 1):
            for di in range(size):
                p = dp_prev[prev][di]
                if p == 0.0:
                    continue
                # on tire R (0)
                # si prev==O (1) et curr==R (0) → X+1 → d+1
                nd = di + (1 if prev==1 else 0)
                dp_cur[0][nd] += p * 0.5
                # on tire O (1)
                # si prev==O (1) et curr==O (1) → Y+1 → d-1
                nd = di - (1 if prev==1 else 0)
                dp_cur[1][nd] += p * 0.5
        dp_prev = dp_cur
    
    # Regrouper selon le signe de (X-Y)
    pA = p0 = pB = 0.0
    for prev in (0, 1):
        for di in range(size):
            prob = dp_prev[prev][di]
            if prob == 0.0:
                continue
            d = di - offset
            if d > 0:
                pA += prob
            elif d == 0:
                p0 += prob
            else:
                pB += prob
    
    # Affichage avec trois décimales (tolérance 1e-3)
    print(f"{pA:.6f} {p0:.6f} {pB:.6f}")

if __name__ == "__main__":
    main()
