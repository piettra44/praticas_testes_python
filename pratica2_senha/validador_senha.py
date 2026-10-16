"""PRÁTICA 2 — Validador de senha (CAÇA AO BUG).

O tamanho mínimo é inclusivo: senhas com 8 caracteres são aceitas se
atenderem às demais regras.
"""

TAMANHO_MINIMO = 8
SIMBOLOS = "!@#$%&*?"


def validar_senha(senha):
    """Devolve a lista de PROBLEMAS encontrados (lista vazia = senha válida).

    Regras:
      - mínimo de 8 caracteres
      - ao menos 1 letra maiúscula, 1 minúscula, 1 dígito e 1 símbolo (!@#$%&*?)
      - sem espaços
    """
    problemas = []

    if len(senha) < TAMANHO_MINIMO:
        problemas.append("Use no mínimo 8 caracteres.")

    if not any(c.isupper() for c in senha):
        problemas.append("Inclua ao menos uma letra maiúscula.")

    if not any(c.islower() for c in senha):
        problemas.append("Inclua ao menos uma letra minúscula.")

    if not any(c.isdigit() for c in senha):
        problemas.append("Inclua ao menos um dígito.")

    if not any(c in SIMBOLOS for c in senha):
        problemas.append("Inclua ao menos um símbolo (!@#$%&*?).")

    if " " in senha:
        problemas.append("Não use espaço.")

    return problemas


def senha_valida(senha):
    """Atalho: True quando não há nenhum problema."""
    return not validar_senha(senha)
