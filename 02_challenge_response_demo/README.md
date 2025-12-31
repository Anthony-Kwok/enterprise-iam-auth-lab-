# Challenge–Response Authentication Demo

This demo simulates how a client authenticates without sending a password.

- The server sends a random challenge
- The client computes a response using its password
- The server verifies the response independently

The password never crosses the network.

This behavior mirrors enterprise authentication systems such as Kerberos and NTLMv2.
