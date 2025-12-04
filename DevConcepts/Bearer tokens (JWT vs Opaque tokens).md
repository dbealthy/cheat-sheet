Source: https://www.permit.io/blog/a-guide-to-bearer-tokens-jwt-vs-opaque-tokens


Opaque tokens:
- Better control
- More secure
- Simple revocation
- Good for internal systems with long lived tokens 


JWT:
- Faster (no extra db/auth service lookup)
- Stateless
- No built in mechanism to revoke tokens
- Good for public apis with short lived tokens