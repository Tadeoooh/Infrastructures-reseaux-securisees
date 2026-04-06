# TP Infrastructures Réseaux Sécurisées

Ce dépôt contient les travaux pratiques réalisés dans le cadre du cours B3 CS Infrastructures Réseaux Sécurisées.

## Topologie réseau
* [TP1](./TP1)
* [TP2](./TP2)
* [TP3](./TP3)

<img width="1117" height="619" alt="image" src="https://github.com/user-attachments/assets/7e31121d-b4d9-4969-ab51-7de5014c2805" />

L'infrastructure réseau est segmentée en 4 VLANs :
- VLAN 10 — admins (`10.1.10.0/24`)
- VLAN 20 — clients (`10.1.20.0/24`)
- VLAN 30 — servers (`10.1.30.0/24`)
- VLAN 40 — guests (`10.1.40.0/24`)

L'infrastructure est composée d'un routeur Cisco (r1), d'un switch core (core1), de quatre switches access (access1 à access4), de clients VPCS et de VMs Rocky Linux.

- Accès internet via NAT
- Serveur DHCP dédié dnsmasq
