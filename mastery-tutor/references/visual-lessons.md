# Visual And Interactive Lessons

## Choose The Medium

Use Markdown by default. Choose self-contained HTML when interaction or spatial presentation materially improves understanding, for example:

- manipulable mathematical or scientific models
- animated processes and state transitions
- annotated art or design comparisons
- maps and layered timelines
- geometry, graphs, networks, and system diagrams
- simulations with adjustable parameters
- before-and-after critique or restoration views

Do not create HTML merely to decorate prose. Pair every visual with a learning objective and an activity that requires observation, prediction, manipulation, explanation, or critique.

## Build The Lesson

1. Copy `assets/interactive-lesson-template.html` into the active course's `lessons/` directory.
2. Replace all `{{...}}` placeholders and remove unused demo controls.
3. Use semantic HTML, responsive CSS, and code-native SVG or canvas where appropriate.
4. Keep the lesson self-contained unless external libraries or media provide clear value and the learner accepts the dependency.
5. Add instructions before interactive controls and a text explanation after them.
6. Include an explicit learner task and a checkpoint; do not reveal the answer prematurely.
7. Add source and license information for external images, quotations, data, or artwork.
8. Link the artifact from the course lesson or session record.

For art and history, prefer learner-provided, public-domain, openly licensed, or otherwise authorized images. Preserve attribution and avoid downloading a collection when links or a smaller selected set are enough.

## Accessibility And Robustness

- Support keyboard navigation and visible focus.
- Label controls and announce dynamic values when useful.
- Use sufficient contrast and avoid relying on color alone.
- Respect reduced-motion preferences.
- Provide alt text or a nearby text equivalent for meaningful visuals.
- Make the core explanation usable when JavaScript is unavailable.
- Avoid autoplaying audio, flashing content, and unnecessary animation.
- Preserve layout on narrow screens and at browser zoom.

## Verify The Artifact

- Check that no template placeholders remain.
- Parse or validate the HTML with available tools.
- Open it in a browser when browser tooling is available.
- Exercise every control and keyboard path.
- Confirm the visual behavior supports the stated concept.
- Capture a screenshot only when it helps review layout or visual accuracy.
- Record any unavailable checks in the session handoff.
