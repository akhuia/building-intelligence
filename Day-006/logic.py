is_raining = True
have_umbrella = False

print(f"Raining? {is_raining}")
print(f"Umbrella {have_umbrella}")

print()

if is_raining and have_umbrella:
    print("Go outside")

elif is_raining:
    print("Take an umbrella first")

else:
    print("Go outside")

