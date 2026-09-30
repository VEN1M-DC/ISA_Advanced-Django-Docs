# Semantic HTML

Contributor: **ISA SAMIEZADE-YAZD**

HTML describes a page's structure and meaning. CSS controls presentation; JavaScript adds behavior. Semantic elements help browsers and assistive technology understand content instead of relying only on its appearance.

## Choose elements by purpose

| Element | Use |
| --- | --- |
| `header` | Introductory content |
| `nav` | Major navigation links |
| `main` | The page's main content |
| `section` | A related group of content, usually with a heading |
| `article` | Content that can stand on its own |
| `footer` | Closing information |
| `a` | Navigate to a URL |
| `button` | Perform an action |

Use headings in a logical hierarchy rather than choosing heading levels for font size. A `div` is useful when a grouping has no more specific meaning.

## Small page example

This example links to the other documentation pages in this repository. Save it as an HTML file in the repository root to try it locally; these links open Markdown source unless a documentation host renders them.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Development study notes</title>
</head>
<body>
  <header>
    <h1>Development study notes</h1>
    <nav aria-label="Main navigation">
      <a href="README.md">All topics</a>
      <a href="python.md">Python</a>
    </nav>
  </header>
  <main>
    <!-- Group related learning goals under a descriptive heading. -->
    <section aria-labelledby="goals">
      <h2 id="goals">Learning goals</h2>
      <ul>
        <li>Set up a project environment.</li>
        <li>Build pages with clear structure.</li>
      </ul>
      <p>Read the <a href="accessibility.md">accessibility guide</a>.</p>
    </section>
  </main>
  <footer><p>Study notes by ISA SAMIEZADE-YAZD</p></footer>
</body>
</html>
```

## Forms and images

Associate a visible label with its control; a placeholder is not a replacement for a label. This is a markup example, not a working submission form:

```html
<label for="topic">Topic to review</label>
<input id="topic" name="topic" type="text" autocomplete="off">
```

For an informative image, describe its purpose in `alt`. Use `alt=""` for a purely decorative image. Keep essential explanations as text rather than embedding them only in pictures. See [Accessibility](accessibility.md).

## Check and troubleshoot

Open the page in a browser and check its title, heading order, links, and keyboard navigation. Validate markup with the [W3C HTML checker](https://validator.w3.org/nu/). Fix duplicate IDs, missing closing tags, and broken relative paths. Filenames can be case-sensitive on the host even if they work on Windows.

In Django, templates produce HTML sent to the browser. Template expressions are processed by Django; opening a template directly as a local file does not run that processing.

Sources: [MDN semantics](https://developer.mozilla.org/en-US/docs/Glossary/Semantics), [WAI development tips](https://www.w3.org/WAI/tips/developing/).

AI assisted with drafting and checking these examples. Review and practice before submitting personal explanations.

[Back to documentation](README.md)
