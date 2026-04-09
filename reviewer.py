import ast

def analyze_code(code):
    bugs = []
    performance = []
    style = []
    security = []

    # ── Basic checks ─────────────────────────────
    if "print(" in code and "debug" in code.lower():
        style.append("Remove debug print statements before production.")

    if "==" in code and "if" not in code:
        bugs.append("Possible misuse of comparison operator.")

    if "password" in code.lower():
        security.append("Hardcoded password detected.")

    if "eval(" in code:
        security.append("Use of eval() is dangerous.")

    if "for" in code and "range(len(" in code:
        performance.append("Use direct iteration instead of range(len()).")

    if len(code) > 500:
        performance.append("Code is long — consider modularizing into functions.")

    return bugs, performance, style, security


def generate_refactor(code):
    return "# Refactored version\n" + code


def review_code(code, language, focus_areas, depth, api_key=None, include_refactor=True):
    bugs, performance, style, security = analyze_code(code)

    score = 100
    score -= len(bugs) * 10
    score -= len(security) * 10
    score -= len(performance) * 5
    score -= len(style) * 3

    score = max(score, 0)

    return {
        "score": score,
        "summary": "Basic static analysis completed.",
        "bugs": bugs,
        "performance": performance,
        "style": style,
        "security": security,
        "refactored_code": generate_refactor(code) if include_refactor else None
    }