---
layout: default
---

# Web Accessibility

Contributor: **ISA SAMIEZADE-YAZD**

Accessible design helps people understand and operate a website with different abilities, devices, and assistive tools. Requirements vary between individuals; a single design choice does not meet everyone's needs.

## Choices for the assignment audiences

| Audience | Practical choice | How to check |
| --- | --- | --- |
| Autistic people | Keep navigation predictable and avoid unexpected autoplay or flashing content | Compare page navigation and check that media starts only when requested |
| Screen reader users | Use meaningful headings, landmarks, labels, and image alternatives | Read the page with a screen reader and inspect its heading list |
| People with low vision | Use readable contrast and a layout that survives zoom | Check contrast and zoom to 200 percent without losing content |
| People with motor disabilities | Make controls keyboard-operable with visible focus and comfortable targets | Complete navigation using Tab, Shift+Tab, Enter, and Space where appropriate |
| Deaf or hard-of-hearing people | Provide captions for speech and meaningful sounds in videos, plus transcripts for audio | Compare captions or transcript with the full recording |
| People with dyslexia | Use clear wording, short paragraphs, and consistent spacing | Review reading order and avoid long all-capital or justified passages |

These are implementation choices, not claims that user testing has been performed.

## Keyboard and reading example

Place this link before navigation, and use the destination on the page's main content:

```html
<a class="skip-link" href="#main-content">Skip to main content</a>
<main id="main-content" tabindex="-1">
  <h1>Project documentation</h1>
  <p>Choose a topic from the navigation.</p>
</main>
```

```css
.skip-link { position: absolute; left: -10000px; }
.skip-link:focus { position: static; }
:focus-visible { outline: 3px solid #111; outline-offset: 4px; }
body { color: #212529; background: #fff; line-height: 1.6; }
a { text-decoration: underline; }
```

The skip link bypasses repeated navigation. Never remove focus outlines without supplying a visible replacement. Choose focus colors that remain visible on the actual background.

## Contrast and media

WCAG AA requires at least 4.5:1 for ordinary text and 3:1 for large text, with defined exceptions. Do not use color alone to explain errors; include text such as “Enter your email address.” Keep layouts usable on small screens and when text grows.

For media, captions must reflect the actual recording, including important non-speech sounds. A transcript gives a readable alternative. If your page has no audio or video, explain that its information is available as text instead of claiming you added captions.

## Verification and troubleshooting

Test every interactive control without a mouse. Check whether the focus order follows the reading order, whether links make sense out of context, and whether images have useful alternatives. Try narrow widths and zoom. Automated accessibility checks can find some errors, but cannot prove a site is accessible; combine them with manual review and user feedback.

If a control cannot be reached by keyboard, use a native link or button instead of a clickable `div`. If an icon is the only visible label, add an accessible name describing its action. Fix overlapping text with flexible sizing rather than disabling zoom.

Sources: [WAI development tips](https://www.w3.org/WAI/tips/developing/), [WAI design tips](https://www.w3.org/WAI/tips/designing/), [WCAG contrast explanation](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).


[Back to documentation](index.md)
