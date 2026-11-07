# Test results

These are real observations from local testing on 7 November 2026. They are not benchmark claims.

| Test | Input | Result | Observation |
|---|---|---|---|
| Telugu/code-mixed transcription | A short synthetic Telugu narration about a caller appearing as “Dad” | Passed | Gnani Prisma returned a readable Telugu transcript. English loanwords such as “phone”, “number”, and “call” appeared in Latin script. User review remains necessary. |
| Complaint draft generation | Corrected transcript plus incident type, date/time, and “No” for money transferred | Passed | The app produced a structured draft with an unverified-note warning. |
| Privacy consent | Audio selected without the consent checkbox | Passed | The browser blocked transcription and required the checkbox. |
| Repeat transcription after consent | Same synthetic recording with consent selected | Passed | The transcript returned successfully again. |
| Second synthetic recording | A short Telugu narration about a caller claiming to be from a bank | No usable transcript returned | The app displayed its fallback message. This outcome is retained honestly; the user can type the description manually and continue. |
| Empty-draft prevention | No incident description entered | Implemented; pending browser check | The app should focus the description field and ask the user to add text instead of creating an empty draft. |

## Still to test

- A deliberately unclear/noisy recording, with the result recorded honestly.
- An unsupported or oversized file, to confirm the error message.
