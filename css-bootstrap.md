# CSS with Bootstrap

Contributor: **ISA SAMIEZADE-YAZD**

CSS controls the appearance and layout of HTML. Bootstrap provides reusable CSS classes and JavaScript components. It speeds up common layouts, but the developer still chooses meaningful HTML, readable content, and accessible interactions.

## Setup

Add these inside the page's `head`. This example pins Bootstrap 5.3.3; it is an example version, not a claim about the latest release. An internet connection is required for the CDN stylesheet.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="styles.css" rel="stylesheet">
```

Create `styles.css` alongside the page:

```css
body { color: #212529; background: #fff; line-height: 1.6; }
main { padding-block: 2rem; }
a { text-decoration: underline; }
:focus-visible { outline: 3px solid #111; outline-offset: 4px; }
img { max-width: 100%; height: auto; }
```

A selector identifies elements to style; declarations pair properties with values. The cascade considers origin, importance, specificity, and order. Loading custom CSS later helps when competing rules otherwise have equal priority. Avoid relying on `!important` for every override.

## Containers and responsive grid

A `.container` centers content and changes its maximum width at breakpoints. `.container-fluid` stays full width. Bootstrap's grid uses rows and twelve-column proportions. The example stacks cards on small screens and places them side by side at `md` and wider, starting at 768px.

```html
<main class="container">
  <h1>Study topics</h1>
  <div class="row g-4">
    <div class="col-12 col-md-6">
      <article class="card h-100">
        <div class="card-body">
          <h2 class="card-title h4">Python</h2>
          <p class="card-text">Review functions and classes.</p>
          <a href="python.md">Read the Python notes</a>
        </div>
      </article>
    </div>
    <div class="col-12 col-md-6">
      <article class="card h-100">
        <div class="card-body">
          <h2 class="card-title h4">Accessibility</h2>
          <p class="card-text">Check keyboard navigation.</p>
          <a href="accessibility.md">Read accessibility notes</a>
        </div>
      </article>
    </div>
  </div>
</main>
```

`g-4` adds space between columns and rows. Cards group related information; the grid adapts their arrangement. Grid and Card are two choices from the assignment's Bootstrap list. The `h4` class changes visual size while the `h2` element keeps the heading hierarchy.

## Navigation and components

This always-visible navigation works without JavaScript. Use it on `index.html` and `about.html`, moving `aria-current="page"` to the active page's link:

```html
<nav class="nav flex-wrap gap-3" aria-label="Main navigation">
  <a class="nav-link" href="index.html" aria-current="page">Home</a>
  <a class="nav-link" href="about.html">About</a>
</nav>
```

Create those pages when using this navigation; this snippet does not create them. Static cards and grid layouts require only CSS. Collapsible navigation, dropdowns, and accordions require Bootstrap JavaScript. For those, add the matching bundle before `</body>`:

```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
```

Copy component markup from the matching official version, keeping IDs unique and control targets matched. Accordion controls need meaningful labels and accurate expanded states. Bootstrap does not automatically make every page accessible.

## Verify and troubleshoot

Resize below and above 768px and confirm the cards stack without horizontal overflow. Test links and focus with a keyboard, zoom text, and measure contrast in the finished design. Use browser developer tools to identify overridden CSS or failed network requests.

If Bootstrap styling is missing, inspect the stylesheet URL and network access. If a collapse control does nothing, check that the bundle loaded and its target ID exists. If local styling is missing, check `styles.css` spelling and placement. Test the deployed paths as well as the local files.

Sources: [Bootstrap setup](https://getbootstrap.com/docs/5.3/getting-started/introduction/), [Bootstrap grid](https://getbootstrap.com/docs/5.3/layout/grid/), [Bootstrap accordion](https://getbootstrap.com/docs/5.3/components/accordion/), [MDN cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction).

AI assisted with drafting. These are learning examples, not evidence that an individual website has been built or tested.

[Back to documentation](README.md)
