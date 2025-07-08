
After reviewing this Extreme ONE OS Security Configuration Guide, I've identified several areas for improvement in consistency, tone, and grammar. Here are the key issues and fixes:

## Consistency Issues:

1. **Procedural Introduction Consistency**
    - Some sections begin with "To [action]:" while others don't. All procedural sections should follow the same pattern.
    - Recommendation: Use "To [action]:" consistently for all procedure introductions.
2. **List Punctuation**
    - Some bulleted lists end items with periods while others don't.
    - Recommendation: Use periods only for complete sentences in lists, not for fragments.
3. **Note Formatting**
    - The document uses "Note:" text instead of the note icon (📝) defined in the style guide.
    - All instances should use the proper icon format.

## Specific Corrections:

### Page 8 - Certificate Operations Section:

**Before:** "Importing Certificates" **After:** "Importing Certificates:" (add colon for consistency)

### Page 9 - Reserved SSL Profiles:

Add periods to the bulleted list items since they are complete sentences:

- "Used by gRPC server instances for generated certificates."
- "Stores CA certificates downloaded during secure Zero Touch Provisioning workflows."
- "Contains CA certificates necessary for firmware updates and copy operations using HTTPS."

### Page 15 - Password Policies Section:

**Before:** "Configure password policies to enforce security requirements:" **After:** "To configure password policies to enforce security requirements:"

### Page 19 - SSH Key Management:

**Before:** "Configure SSH host keys" **After:** "Configure SSH host keys:" (add missing colon)

### Page 20 - SSH Client Public Key Authentication:

Standardize the headings:

- "Importing SSH Client Keys" → "To import SSH client keys:"
- "Direct Public Key Configuration" → "To configure public keys directly:"

### Page 22 - 802.1X Authentication:

Add missing colons to section headings:

- "Global 802.1X Enable" → "To enable 802.1X globally:"
- "Interface 802.1X Configuration" → "To configure 802.1X on an interface:"

### Page 24 - Certificate Management Best Practices:

Remove periods from the numbered list items that are fragments:

1. "Use separate SSL profiles for different services"
2. "Monitor certificate expiry with alerts" (etc.)

### Throughout the Document:

Replace all instances of "Note:" with the proper note icon (📝) as defined in the style guide.

## Grammar Corrections:

1. **Page 12 - JWT Token Requirements:** The bullet points should use consistent formatting. Change to:
    - `sub`: Subject (username)
    - `role`: User role (e.g., admin, user)
    - `exp`: Expiration timestamp
    - `iat`: Issued at timestamp
2. **Page 26 - Certificate Problems:** Under "Certificate import fails," standardize the list format by removing periods from fragments.

## Tone Improvements:

The document maintains a professional, technical tone throughout, which is appropriate for a security configuration guide. However, consider adding brief introductory sentences to major sections to provide context for readers.

These changes will improve the document's consistency and readability while maintaining its technical accuracy and professional tone.

[Start your own conversation](/project/01971714-7e5a-7781-bbca-2c5b169e9f00)