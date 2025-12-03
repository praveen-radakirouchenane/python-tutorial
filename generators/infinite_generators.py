def infinte_gen():
    count =1

    while True:
        yield(f"count is {count}")
        count+=1

call_infinte_gen = infinte_gen()
for _ in range(5):
    print(next(call_infinte_gen))