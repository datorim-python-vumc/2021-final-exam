# Noslēguma darbs

- Izveidot klasi ``Deposit``, kurai ir atribūti ``deposit`` (sākotnējā noguldīguma summa), ``term`` (noguldījuma termiņš gados), ``rate`` (gada procentu likme, decimālskaitlis, 5%=0.05), klasei ir metode ``interest()``, kas aprēķina peļņu noguldījuma termiņa beigās.
```py
deposit = Deposit(
    deposit=1000,
    term=2,
    rate=0.05,
)

interest = deposit.interest()
print(interest)

# interest = 102.5

```

- Izveidot Django projekctu, izveidot aplikāciju ``deposits``
- Izveidot modeli ``Deposit``, kuram ir lauki (fields): ``deposit``, ``term``, ``rate``, ``interest``.
- Izveidot view, kas pie metodes ``GET`` renderēs HTML formu, kurā ir nepieciešams ievadīt ``deposit``, ``term`` un ``rate``. Kad forma tiek iesniegta (metode ``POST``), tiek veidots jauns klases ``Deposit`` objekcts. Datubāzei tiek pievienots jauns ieraksts. Forma tiek parādīta uz '/deposit/new'.
- Izveidot view, kas renderēs sarakstu ar visiem tabulas ``deposits`` ierakstiem. Saraksts tiek parādīts uz '/'.
- Izveidot view, kas renderēs informāciju par konkrētu ``deposits`` tabulas ierakstu. Tas tiek parādīts uz '/deposit/<primary key>'
- Izdarīt tā, lai iesniedzot formu uz '/deposit/new', tiek atvērts saraksts ar visiem tabulas ``deposits`` ierakstiem.
- Izdarīt tā, lai sarakstā ar visiem tabulas ``deposits`` ierakstiem, uzspiežot uz kādu no saraksta elementiem, tiek atvērta lapa ar informāciju par konkrētu ``deposits`` tabulas ierakstu.
