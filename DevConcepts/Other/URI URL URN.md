Source: https://auth0.com/blog/url-uri-urn-differences/

# URL (Uniform Resource Locator) - resource address in the internet
Specification: https://datatracker.ietf.org/doc/html/rfc3986

Examples:
- Web page
- Image
- Mailbox


## URL vs Link
Words URL and link are commonly used interchangeably, but they are not the synonyms. URL - is a string that allows to locate a resource. A link (hyperlink) is an HTML element, that allows to load a resource from a given URL.

## Anatomy of a URL

![[Pasted image 20230824101026.png]]

- Scheme: protocol that should be used to access the resource.
- Domain: part that indicates that server hosting the resource. It can be domain or ip address.
- TLD: Right most part of url that classifies resource into categories. There is a list of registered tlds: https://en.wikipedia.org/wiki/Public_Suffix_List 
- Port: protocol port to which to send the request to access the resource.
- Authority: Domain + Port
- Path: path to the resource on the hosting server.
- Parameters: extra information provided to the hosting server.
- Fragment: part that represents specific part inside the resource.



# URI (Uniform Resource Identifier) - identifies resource on the web.
Specification: https://datatracker.ietf.org/doc/html/rfc3986
URL - is a subset of URI

URI might be represented as URL, but it isn't meant to be used to direct to a specific resource. It is mean to identify and describe that resource.

Example of URI https://the-great-chef.com/languages/recipe:
```xml
<?xml version = "1.0" encoding = "UTF-8"?>
<rec:recipe xmlns:recipe = "https://the-great-chef.com/languages/recipe">
  <rec:title>Spaghetti carbonara</rec:title>
  <rec:author>Anonymous</rec:author>
  <rec:ingredients>
    ...
  </rec:ingredients>
</cont:contact>
```


URIs have great relevance in the [Semantic Web](https://en.wikipedia.org/wiki/Semantic_Web) since they are used to identify concepts through the [Resource Description Framework (RDF)](https://en.wikipedia.org/wiki/Resource_Description_Framework).


# URN (Uniform Resource Name) - identifies resource in a permanent way, even if a resource doesn't exist anymore.

Specification: https://datatracker.ietf.org/doc/html/rfc2141

Unlike URL, URN doesn't provide any information about location of resource, but identifies it.

URN is a URI, whose schema is `urn` 

Format:
```urn
urn:<NAMESPACE-IDENTIFIER>:<NAMESPACE-SPECIFIC-STRING>
```


Examples:
```urn
urn:isbn:1234567890
urn:ISSN:0167-6423
urn:ietf:rfc:2648
```




![[Pasted image 20230824110319.png]]