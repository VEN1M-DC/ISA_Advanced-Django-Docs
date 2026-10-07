---
title: Client Server Architecture and Django
---

# Client Server Architecture and Django

Contributor: **ISA SAMIEZADE-YAZD**. Updated October 7, 2026. Study notes synthesized from the linked course slides with AI assistance. Examples are learning aids, not claims of completing every slide exercise.

## Abstraction and layers

Abstraction exposes a useful interface while hiding lower-level implementation. A browser requests a URL without implementing the server's database access. A Django view uses the ORM without constructing every SQL statement. Learn the Python language, Django's architecture, and how its Python APIs connect that architecture.

| Layer | Responsibility | Portfolio example |
| --- | --- | --- |
| Presentation | Show information and accept input | Browser and HTML templates |
| Logic | Process a request and apply rules | Views, forms, and model methods |
| Persistence | Store and retrieve information | ORM and SQLite |

Architecture describes how components fit together. Design describes their implementation. Layers are logical responsibilities; they do not necessarily require three separate computers.

## Clients servers and peers

A client initiates a request; a server listens and responds. The Django development process and browser can both run on the same computer. In peer-to-peer systems, a participant may perform both roles. DNS resolves names to network addresses; HTTP exchanges web requests and responses. Static sites return prepared assets; dynamic applications run code to generate responses.

`http://127.0.0.1:8000/admin/` uses the loopback address and port 8000. It works on the computer running the server. It is not a public deployment. GitHub hosts the application source; GitHub Pages hosts static documentation.

## HTTP request and response

A request has a method, target, headers, and sometimes a body. A response has a status, headers, and usually content. HTTP is stateless: a new request does not inherently remember the previous one. Session cookies let Django associate subsequent requests with server-side session data. Persistent connections do not make HTTP application stateful.

| Status family | Meaning | Example |
| --- | --- | --- |
| 2xx | Successful handling | 200 page response |
| 3xx | Redirection | 302 redirect to login |
| 4xx | Client-side request/access issue | 404 unknown URL; 403 forbidden |
| 5xx | Server failure | 500 unhandled application error |

Inspect your running app from PowerShell using the actual curl executable:

```powershell
curl.exe -i http://127.0.0.1:8000/admin/login/
curl.exe -I http://127.0.0.1:8000/admin/login/
curl.exe -v http://127.0.0.1:8000/admin/login/
```

`-i` includes response headers and the body. `-I` sends HEAD and retrieves headers. `-v` adds connection and protocol diagnostics; keep cookie or authorization values out of screenshots and commits. Modern HTTP versions can use binary framing, so the slides' ASCII description should not be generalized to all HTTP versions.

## URLs routes and APIs

In `https://example.com:443/projects?major=CSCI-BS`, the scheme is HTTPS, host is example.com, port is 443, path is /projects, and the query parameter is major. HTTPS protects HTTP communication using TLS. A fragment beginning with # is interpreted by the client rather than sent as part of the HTTP request target.

An API defines accepted operations, inputs, outputs, and errors. An HTTP endpoint identifies a resource; a route combines an HTTP method and path. GET parameters often use the query string; POST data can use the request body. Never paste a real API key into published examples. The Movie Database examples in the slides demonstrate searching a resource with parameters, checking its API documentation, and examining a JSON response.

REST is an architectural style built around resources, representations, and a uniform interface. JSON, HTML, and XML are possible representations. JSON uses quoted string keys and supports strings, numbers, booleans, null, arrays, and objects.

| Operation | Typical HTTP method | Illustrative route |
| --- | --- | --- |
| List/read | GET | /projects/ or /projects/1/ |
| Create | POST | /projects/ |
| Replace/update | PUT or PATCH | /projects/1/ |
| Delete | DELETE | /projects/1/ |

These are API design examples; Django admin uses its own HTML form routes and POST operations rather than being this REST API.

## Services frameworks and patterns

Service-oriented architecture combines services with defined interfaces. A service controls its data and exposes operations to other components. API-first design asks which operations and contracts are needed before implementing internals. A modular Django app does not automatically become a separate network service.

Django organizes requests through URL routing, views, models, and templates. Models manage domain data, views process requests, and templates format output. The framework supplies reusable authentication, routing, validation, and development tools.

| Pattern connection in the lecture | Django example |
| --- | --- |
| Active Record concepts | Model instances provide persistence methods |
| Identity Field | Automatic primary key |
| Observer | Signals notify receivers |
| Template Method | Generic class-based views provide overridable steps |
| Template View | HTML templates combine structure and data |
| Command analogy | HttpRequest packages request information |

These are explanatory connections, not a claim that every component exactly implements a named pattern. Creational patterns concern object creation; structural patterns organize components; behavioral patterns coordinate behavior.

## Troubleshooting and checks

If the browser cannot connect, verify the server process and port. If a response is 404, inspect the requested path and URL configuration. A successful login page proves HTTP handling, not that personal Student records exist. Compare the response, server log, and database when testing a complete feature.

## Sources

- [Course slides on client server architecture and Django](https://docs.google.com/presentation/d/1r6e5Gm9r-PjUsj4CLu4hIilHQAemLmZIkuNNJH8Y9cM/edit)
- [Django design philosophies](https://docs.djangoproject.com/en/6.1/misc/design-philosophies/)
- [Django request and response objects](https://docs.djangoproject.com/en/6.1/ref/request-response/)
- [curl manual](https://curl.se/docs/manpage.html)

[Return to documentation home](index.md) · [Continue to models and databases](django-models-databases.md)
