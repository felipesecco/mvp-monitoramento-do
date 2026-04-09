import json

eventos = [
    {
        "tipo": "Aposentadoria",
        "texto": "Conceder aposentadoria voluntária a MARIA APARECIDA SOUZA, Analista Judiciária.",
        "orgao": "TRF-1",
        "data_publicacao": "2026-04-08",
        "pessoa": "MARIA APARECIDA SOUZA",
        "observacao": "Aposentadoria voluntária"
    },
    {
        "tipo": "Exoneração",
        "texto": "Exonerar JOÃO CARLOS PEREIRA do cargo em comissão de Assessor Jurídico.",
        "orgao": "CNMP",
        "data_publicacao": "2026-04-08",
        "pessoa": "JOÃO CARLOS PEREIRA",
        "observacao": "Exoneração a pedido"
    },
    {
        "tipo": "Nomeação",
        "texto": "Nomear ANA PAULA FERREIRA para o cargo de Técnica Administrativa.",
        "orgao": "STJ",
        "data_publicacao": "2026-04-08",
        "pessoa": "ANA PAULA FERREIRA",
        "observacao": "Cargo efetivo"
    },
    {
        "tipo": "Posse",
        "texto": "Dar posse a RICARDO ALMEIDA no cargo de Defensor Público Federal.",
        "orgao": "DPF",
        "data_publicacao": "2026-04-07",
        "pessoa": "RICARDO ALMEIDA",
        "observacao": "Posse decorrente de nomeação"
    },
    {
        "tipo": "Afastamento",
        "texto": "Autorizar o afastamento de LUCIANA MENDES para participação em evento internacional.",
        "orgao": "MPF",
        "data_publicacao": "2026-04-07",
        "pessoa": "LUCIANA MENDES",
        "observacao": "Afastamento para evento"
    },
    {
        "tipo": "Concurso",
        "texto": "Publicar edital de concurso público com reserva de vagas para pessoas negras e pessoas com deficiência.",
        "orgao": "TJSP",
        "data_publicacao": "2026-04-06",
        "pessoa": "",
        "observacao": "Ações afirmativas"
    },
    {
        "tipo": "Promoção",
        "texto": "Promover PAULO HENRIQUE LIMA à categoria final da carreira.",
        "orgao": "MPRS",
        "data_publicacao": "2026-04-06",
        "pessoa": "PAULO HENRIQUE LIMA",
        "observacao": "Promoção funcional"
    },
    {
        "tipo": "Indicação",
        "texto": "Indicar FERNANDA COSTA para compor comissão de acompanhamento institucional.",
        "orgao": "CNJ",
        "data_publicacao": "2026-04-05",
        "pessoa": "FERNANDA COSTA",
        "observacao": "Indicação para comissão"
    },
    {
        "tipo": "Eleição",
        "texto": "Convocar eleição para escolha da lista tríplice da administração superior.",
        "orgao": "DPE-RJ",
        "data_publicacao": "2026-04-05",
        "pessoa": "",
        "observacao": "Processo eleitoral interno"
    },
    {
        "tipo": "Aposentadoria",
        "texto": "Aposentar compulsoriamente CARLOS EDUARDO SILVA, nos termos da legislação vigente.",
        "orgao": "TJMG",
        "data_publicacao": "2026-04-04",
        "pessoa": "CARLOS EDUARDO SILVA",
        "observacao": "Aposentadoria compulsória"
    },
    {
        "tipo": "Exoneração",
        "texto": "Exonerar HELENA MARTINS do cargo de confiança vinculado à Presidência.",
        "orgao": "STF",
        "data_publicacao": "2026-04-04",
        "pessoa": "HELENA MARTINS",
        "observacao": "Exoneração de cargo comissionado"
    },
    {
        "tipo": "Nomeação",
        "texto": "Nomear BRUNO TEIXEIRA para exercer o cargo de Assessor de Gabinete.",
        "orgao": "CNJ",
        "data_publicacao": "2026-04-03",
        "pessoa": "BRUNO TEIXEIRA",
        "observacao": "Cargo comissionado"
    },
    {
        "tipo": "Afastamento",
        "texto": "Conceder afastamento a RENATA OLIVEIRA para curso de pós-graduação no exterior.",
        "orgao": "TRF-3",
        "data_publicacao": "2026-04-03",
        "pessoa": "RENATA OLIVEIRA",
        "observacao": "Afastamento para estudo"
    },
    {
        "tipo": "Concurso",
        "texto": "Divulgar resultado preliminar da prova objetiva com detalhamento de vagas reservadas por fase.",
        "orgao": "MPBA",
        "data_publicacao": "2026-04-02",
        "pessoa": "",
        "observacao": "Resultado preliminar"
    },
    {
        "tipo": "Posse",
        "texto": "Registrar a posse de JULIANA BARROS no cargo de Analista do Ministério Público.",
        "orgao": "MPDFT",
        "data_publicacao": "2026-04-02",
        "pessoa": "JULIANA BARROS",
        "observacao": "Posse em cargo efetivo"
    },
    {
        "tipo": "Afastamento",
        "texto": "Autorizar afastamento de EDUARDO NOGUEIRA para representação institucional em congresso jurídico.",
        "orgao": "STJ",
        "data_publicacao": "2026-04-01",
        "pessoa": "EDUARDO NOGUEIRA",
        "observacao": "Representação institucional"
    },
    {
        "tipo": "Indicação",
        "texto": "Indicar MARCELO TAVARES para atuação em grupo de trabalho sobre equidade racial.",
        "orgao": "CNMP",
        "data_publicacao": "2026-04-01",
        "pessoa": "MARCELO TAVARES",
        "observacao": "Grupo de trabalho"
    },
    {
        "tipo": "Promoção",
        "texto": "Promover LÍVIA MONTEIRO por antiguidade à categoria intermediária da carreira.",
        "orgao": "MPGO",
        "data_publicacao": "2026-03-31",
        "pessoa": "LÍVIA MONTEIRO",
        "observacao": "Promoção por antiguidade"
    },
    {
        "tipo": "Exoneração",
        "texto": "Exonerar RAFAEL SOARES do cargo de assessor especial, a pedido.",
        "orgao": "TRF-2",
        "data_publicacao": "2026-03-31",
        "pessoa": "RAFAEL SOARES",
        "observacao": "Exoneração a pedido"
    },
    {
        "tipo": "Nomeação",
        "texto": "Nomear PATRÍCIA LIMA para ocupar cargo em comissão no gabinete da Corregedoria.",
        "orgao": "TJRJ",
        "data_publicacao": "2026-03-30",
        "pessoa": "PATRÍCIA LIMA",
        "observacao": "Cargo em comissão"
    }
]

with open("eventos.json", "w", encoding="utf-8") as f:
    json.dump(eventos, f, indent=2, ensure_ascii=False)

print(f"{len(eventos)} eventos gravados em eventos.json com sucesso.")