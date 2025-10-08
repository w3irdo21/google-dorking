def create_dorks(filename, batch_size=6, suffix='intitle:"Swagger UI"'):
    with open(filename, "r") as f:
        domains = [line.strip().lstrip("*.") for line in f if line.strip()]

    dorks = []
    for i in range(0, len(domains), batch_size):
        batch = domains[i:i + batch_size]
        dork = "(" + " OR ".join(f"site:{d}" for d in batch) + f") {suffix}"
        dorks.append(dork)

    return dorks


if __name__ == "__main__":
    dorks = create_dorks("domains.txt", batch_size=6, suffix='intitle:"Swagger UI"')
    with open("dorks.txt", "w") as f:
        for dork in dorks:
            f.write(dork + "\n")

    print(f"Generated {len(dorks)} dork lines. Saved to dorks.txt")
