python = set(input("Enter Python Programming USNs: ").split())
data = set(input("Enter Data Science USNs: ").split())

print("Both:", python & data)
print("Only Python Programming:", python - data)
print("Only Data Science:", data - python)
print("At least one:", python | data)
print("Exactly one:", python ^ data)
print("Total unique students:", len(python | data))
