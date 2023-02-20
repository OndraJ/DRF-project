# DRF-project


## Webová aplikace v Django

`POST` - akceptuje CSV soubory a uloží je do databáze.

`GET` - HTML stránka, kde jsou všechny transakce.

## Příklad CSV souboru

```
reference,timestamp,amount,currency,description
10000001,2023-01-11T03:00:01Z,20000,CZK,
10000002,2023-01-11T09:00:00Z,-100,CZK,Lekárna Hradčanská
10000003,2023-01-11T10:10:10Z,-1337,CZK,Lidl
10000004,2023-01-11T12:00:00Z,-220,CZK,Šenkýrna
10000005,2023-01-11T13:00:01Z,-100,CZK,Kofii
10000006,2023-01-11T17:00:00Z,-12000,CZK,Servis Škoda Praha
10000007,2023-01-11T13:00:01Z,100,CZK,Pepa
```

## Soubor se nahraje pomocí curl
```
curl -X POST -H 'Content-Type:text/csv' --data-binary @"absolute_path\transactions.csv" http://localhost:8000/transactions/
```
