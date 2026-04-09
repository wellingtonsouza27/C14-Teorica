def avaliar_forca(senha: str) -> str:
    score = 0

    if len(senha) >= 8:
        score += 1
    if any(c.isupper() for c in senha):
        score += 1
    if any(c.islower() for c in senha):
        score += 1
    if any(c.isdigit() for c in senha):
        score += 1
    if any(c in "!@#$%^&*()" for c in senha):
        score += 1

    if score <= 2:
        return "fraca"
    elif score <= 4:
        return "media"
    else:
        return "forte"