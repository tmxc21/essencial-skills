#!/usr/bin/env python3
"""Gera um arquivo .ics com os prazos de um caso, com alertas 7 e 2 dias antes.

Uso:
  python3 gerar_ics.py saida.ics "Nome do caso" "AAAA-MM-DD|Título do prazo|Descrição" ["AAAA-MM-DD|..."]

Cada prazo vira um evento de dia inteiro. Funciona em Google Agenda, Outlook e iPhone.
"""
import sys
import uuid
from datetime import datetime, timedelta, timezone


def esc(texto: str) -> str:
    return (texto.replace("\\", "\\\\").replace(";", "\\;")
            .replace(",", "\\,").replace("\n", "\\n"))


def evento(caso: str, data: str, titulo: str, descricao: str) -> str:
    inicio = datetime.strptime(data, "%Y-%m-%d").date()
    fim = inicio + timedelta(days=1)
    agora = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    linhas = [
        "BEGIN:VEVENT",
        f"UID:{uuid.uuid4()}@super-assessor-juridico",
        f"DTSTAMP:{agora}",
        f"DTSTART;VALUE=DATE:{inicio:%Y%m%d}",
        f"DTEND;VALUE=DATE:{fim:%Y%m%d}",
        f"SUMMARY:{esc(f'⚖ {caso}: {titulo}')}",
        f"DESCRIPTION:{esc(descricao)}",
    ]
    for dias in (7, 2):
        linhas += [
            "BEGIN:VALARM",
            "ACTION:DISPLAY",
            f"DESCRIPTION:{esc(f'{titulo} em {dias} dias')}",
            f"TRIGGER:-P{dias}D",
            "END:VALARM",
        ]
    linhas.append("END:VEVENT")
    return "\r\n".join(linhas)


def main() -> None:
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    saida, caso, prazos = sys.argv[1], sys.argv[2], sys.argv[3:]
    eventos = []
    for item in prazos:
        partes = item.split("|")
        data, titulo = partes[0], partes[1]
        descricao = partes[2] if len(partes) > 2 else ""
        eventos.append(evento(caso, data, titulo, descricao))
    conteudo = "\r\n".join([
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Super Assessor Juridico//PT-BR",
        "CALSCALE:GREGORIAN",
        *eventos,
        "END:VCALENDAR",
    ]) + "\r\n"
    with open(saida, "w", encoding="utf-8", newline="") as f:
        f.write(conteudo)
    print(f"{len(eventos)} prazo(s) gravado(s) em {saida}")


if __name__ == "__main__":
    main()
