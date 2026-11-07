# ReportSathi Telugu

ReportSathi is a privacy-aware prototype that helps a Telugu-speaking user prepare an **editable** draft after a suspected cyber-fraud or impersonation incident.

## What it does

1. A user uploads a short Telugu or Telugu-English audio description.
2. Gnani Prisma transcribes the audio.
3. The user reviews and corrects the transcript.
4. The user selects incident details and creates a structured, copyable complaint draft.
5. The app points users who may have lost money or shared credentials to their bank, the 1930 cyber-fraud helpline, and the National Cyber Crime Reporting Portal.

## Gnani AI technology

The application uses Gnani Prisma through its Speech-to-Text REST API:

- Endpoint: `POST https://api.vachana.ai/stt/v3`
- Model: `prisma-v3.0`
- Language hints: `te-IN,en-IN`
- Output style: `codemix`, which keeps English terms in Latin script when appropriate.

The user’s API key remains in a local `.env` file and is never placed in source code.

## Important limits

- ReportSathi does **not** identify or prove that a caller is a scammer.
- It does **not** submit a complaint to a government system.
- It does **not** store uploaded audio or complaint drafts.
- The transcript must be reviewed by the user before it is used.
- The demo uses only synthetic, consented sample audio.

## Run locally

1. Create `.env` next to `app.py`:

   ```text
   GNANI_API_KEY=your_private_key
   ```

2. Install dependencies:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

3. Start the app:

   ```powershell
   .\.venv\Scripts\python.exe app.py
   ```

4. Open `http://127.0.0.1:5000`.

## Privacy

Never enter or upload OTPs, PINs, passwords, bank-account numbers, Aadhaar numbers, or someone else’s voice without consent.

## Official references

- [Gnani Speech-to-Text REST documentation](https://docs.gnani.ai/api/STT/speech-to-text)
- [National Cyber Crime Reporting Portal](https://cybercrime.gov.in)
