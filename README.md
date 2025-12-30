# Enterprise IAM Authentication Lab

This repository demonstrates how enterprise authentication works without transmitting passwords over the network. It is designed to showcase practical IAM, Active Directory, and authentication security knowledge expected of an enterprise infrastructure security engineer.

## Lab Objectives

This lab teaches and demonstrates:

1. How enterprise authentication works without sending passwords.
2. Challenge–response authentication mechanisms (conceptually Kerberos / NTLMv2).
3. Why replay attacks fail and the importance of one-time challenges.
4. How stolen hashes or credentials can be abused (pass-the-hash).
5. Mapping lab demonstrations to real enterprise AD/Kerberos infrastructure.
6. Defensive measures for protecting credentials and authentication flows.

## Skills Demonstrated

By completing this lab, you will demonstrate:

- Understanding of enterprise IAM architecture.
- Ability to simulate and explain authentication flows.
- Awareness of credential theft techniques and mitigation.
- Knowledge of Active Directory and Kerberos security controls.
- Understanding of attack/defense scenarios.


## How to Run the Demo

1. Install Python 3.10+.
2. Navigate to the demo folder:
   cd 02_challenge_response_demo
3. Start the server:
   python server.py
4. Open a new terminal and run the client:
   python client.py
5. Observe authentication succeeding without the password ever being transmitted.

## Key Takeaways

- Passwords are never sent over the network.
- The client proves knowledge of the password using a one-time challenge.
- Replay attacks fail because challenges are unique.
- Stolen hashes can be abused if proper protections are not in place.
- This lab mirrors core principles of Kerberos and NTLMv2 authentication.

## References

- Microsoft Docs: Active Directory Authentication - https://learn.microsoft.com/en-us/windows-server/identity/active-directory
- Kerberos: The Network Authentication Protocol - https://web.mit.edu/kerberos/
- NTLMv2 Challenge/Response
- Pass-the-Hash Attack Techniques
