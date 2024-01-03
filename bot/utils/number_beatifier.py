def beatifier(number: int | float) -> str:
    k_number = number / 1_000
    m_number = number / 1_000_000
    b_number = number / 1_000_000_000
    if k_number >= 1 and k_number < 1000:
        return f"{k_number:.1f}k"
    if m_number >= 1 and m_number < 1000:
        return f"{m_number:.1f}m"
    if b_number >= 1 and b_number < 1000:
        return f"{b_number:.1f}b"
    return "0"