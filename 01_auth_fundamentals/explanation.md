# Authentication Fundamentals

Enterprise authentication systems do not send passwords across the network.

Instead, they use challenge–response mechanisms that allow a client to prove it knows a secret without revealing it.

## Authentication vs Authorization

- Authentication: Verifying identity (Who are you?)
- Authorization: Determining permissions (What can you do?)

This lab focuses on authentication.

## Why Passwords Are Never Sent

- Prevents credential exposure via network sniffing
- Stops replay attacks
- Protects accounts even if the network is compromised

## Challenge–Response

1. Server sends a random challenge
2. Client computes a response using its password
3. Server independently verifies the response
4. Password never leaves the client

The challenge changes every login, preventing replay attacks.

## Salt vs Challenge

- Salt: Protects stored passwords, usually static
- Challenge: Sent during login, changes every attempt, prevents replay attacks

