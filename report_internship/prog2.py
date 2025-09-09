#!/usr/bin/env python3
import sys
import json
import math
from functools import lru_cache

def solve_query(orig_docs, new_docs):

    N = len(orig_docs)
    M = len(new_docs)

    rel_orig = [d["relevance"] for d in orig_docs]
    cost_orig = [d["cost"]      for d in orig_docs]
    Q0 = sum(rel_orig[i] / (i+1) for i in range(N))
    R0 = sum(cost_orig[i] / math.sqrt(i+1) for i in range(N))

    rel_new  = [d["relevance"] for d in new_docs]
    cost_new = [d["cost"]      for d in new_docs]

    best_rev = R0

    def backtrack(i_orig, used_mask, pos, q_sum, r_sum):
        nonlocal best_rev

        if pos > N:
            used_new = bin(used_mask).count("1")
            if i_orig + used_new == N and q_sum >= Q0:
                best_rev = max(best_rev, r_sum)
            return

        remain = (N - i_orig) + (M - bin(used_mask).count("1"))
        needed = N - pos + 1
        if remain < needed:
            return

        if i_orig < N:
            backtrack(
                i_orig + 1,
                used_mask,
                pos + 1,
                q_sum + rel_orig[i_orig] / pos,
                r_sum + cost_orig[i_orig] / math.sqrt(pos)
            )

        for j in range(M):
            if not (used_mask & (1 << j)):
                backtrack(
                    i_orig,
                    used_mask | (1 << j),
                    pos + 1,
                    q_sum + rel_new[j] / pos,
                    r_sum + cost_new[j] / math.sqrt(pos)
                )

    backtrack(0, 0, 1, 0.0, 0.0)
    return best_rev

def main():
    data = json.load(sys.stdin)
    serps     = data["serpset"]
    new_docs  = data["new_documents"]

    extra_by_query = {}
    for d in new_docs:
        extra_by_query.setdefault(d["query"], []).append(d)

    total_revenue = 0.0
    for serp in serps:
        q = serp["query"]
        orig = serp["results"]
        extras = extra_by_query.get(q, [])
        best = solve_query(orig, extras)
        total_revenue += best

    print(f"{total_revenue:.2f}")

if __name__ == "__main__":
    main()