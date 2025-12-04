**Subject (Principal / Identity)** - An entity that requests access - human, service, process, or device. Typically has an id (`user:alice`, `service:arm`)

**Resource** - The object being protected: data, service, endpoint, device, etc. E.g. `document:invoice-1234`

**Action** - The verb subject wants to perform on a resource (create, read, delete, submit-for-review)

**Context** (Environment / Conditions) - Additional data, that affect decisions: time, ip, device, geo, attributes

**Policy** - A set of rules that specify who can do what. 
Authority that evaluates claims, roles, permissions, scopes and context.
Used in PDPs (Policy Decision Points), PBAC/ABAC frameworks.
It may look like:
```
allow {
  input.user.department == input.resource.department
  input.action == "read"
  input.time < "18:00"
}

```

**Permission** - A specific allowed (or denied) operation. E.g. `read:document`.

**Role** - A named collection of permissions (or other roles) that can be assigned to a subject.

**Scope** - A named _coarse-grained_ capability that client or token is allowed to do. Express what a token can be used for. It provides least privilege access for clients. Usually represented as plain strings (invoices:read). Client often requests scopes from IdP and gets token with embedded scopes.

**Claim** - Peace of information about a user or token, baked into a token (typically a JWT), claims are data, no permissions. E.g. sub, iss, exp, email, name, locale, permissions, roles, groups, tenant_id, department, ... In other words keys in JWT or similar token that describe a sabject.


**PDP** - Policy Decision Point. Local or remote service/library/class that evaluates policy and decides whether access is allowed or not.

**PEP** - Policy Enforcement Point. Service/class/library that enforces the access. It might be the domain application itself.

**IdP** - Identity provider


**Roles vs Scopes** - Roles are assigned to a subject, whereas scopes are provided by the client to get a token with fine-grained access or some broad access. The difference is that scopes are delegated (client asks for scopes), whereas roles are given to a user.

Roles are a part of user identity.
Scopes live in a token and may be different per token and per client.

Roles are often mapped to permissions
Scopes may map to permissions, but they don't have to. Sometimes scope maps 1:1 to a permission (`documents.read` -> `document:read`), Other times scope maps to a bundle of permissions. Scopes are about API surface and not business level permissions.


Scopes are often used for OAuth consent and coarse API gating.


Tenant - Isolated users or groups of users. Multi tenant system means. Many customers use a single app, but each customer's data is isolated from others. (Account, Workspace, Company, Organization, etc...)

Users -> belong to tenant
Resources -> belong to tenant
Policies -> evaluated within Tenant boundary
Admins operate within their tenant


Application = building
Tenant = apartment in the building
