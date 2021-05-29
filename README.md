# whois-rest

A RESTful `whois`.

## Installation

```bash
$ pip install poetry
$ poetry install

$ uvicorn app:app
INFO:     Started server process [64616]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Usage

```bash
$ curl localhost:8000/api/v1/google.com
{
  "hostname": "google.com",
  "raw": "...",
  "status": [
    "ACTIVE",
    "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited",
    "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
    "clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited",
    "serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited",
    "serverTransferProhibited https://icann.org/epp#serverTransferProhibited",
    "serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited",
    "clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)",
    "clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)",
    "clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)",
    "serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)",
    "serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)",
    "serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)"
  ],
  "nameServers": [
    "NS1.GOOGLE.COM",
    "NS2.GOOGLE.COM",
    "NS3.GOOGLE.COM",
    "NS4.GOOGLE.COM",
    "ns4.google.com",
    "ns2.google.com",
    "ns1.google.com",
    "ns3.google.com"
  ],
  "created": "1997-09-15T04:00:00",
  "updated": "2019-09-09T15:39:04",
  "expires": "2028-09-14T04:00:00",
  "registrar": "MarkMonitor Inc.",
  "registrantName": null,
  "registrantOrganization": "Google LLC",
  "registrantAddress": null,
  "registrantCity": null,
  "registrantState": "CA",
  "registrantZipcode": null,
  "registrantCountry": "US",
  "dnssec": "unsigned"
}
```
