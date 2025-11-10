# ReganCipher Review Writing Guide

This guide covers how to write effective, SEO-optimized audio gear reviews that combine measurements with real-world impressions.

## Quick Start Checklist

Before publishing a review, ensure you have:

- [ ] Product measured with at least 3 consistent readings
- [ ] 7-14 days of listening across multiple genres
- [ ] Photos taken (product, packaging, measurements)
- [ ] Comparison with similar products in price range
- [ ] Affiliate links gathered and tested
- [ ] YouTube video recorded and uploaded
- [ ] Markdown file created with proper frontmatter

## File Naming Convention

All review posts must follow this format:

```
_posts/YYYY-MM-DD-product-name-review.md
```

Examples:
- `2025-10-30-qcy-h3-review.md`
- `2025-11-15-moondrop-blessing-3-review.md`
- `2025-12-01-fiio-k11-dac-review.md`

**Rules:**
- Always use lowercase
- Replace spaces with hyphens
- End with `-review.md`
- Date is publication date

## Frontmatter Template

Every review starts with YAML frontmatter. Copy this template:

```yaml
---
layout: review
title: "[Brand] [Model] Review - [One Key Feature]"
date: YYYY-MM-DD
brand: "Brand Name"
model: "Model Name"
price: "$XX.XX"
rating: X.X
verdict: "One-sentence verdict that captures the essence"

image: /assets/images/reviews/product-name.jpg
measurement_url: "https://regancipher.github.io/measurements/?share=Product_Name"
youtube_id: "YOUR_VIDEO_ID"

category: headphones  # headphones, iems, dacs, or accessories
tags:
  - bluetooth
  - anc
  - budget
  - wireless

pros:
  - Specific pro point 1
  - Specific pro point 2
  - Specific pro point 3

cons:
  - Specific con point 1
  - Specific con point 2

affiliate_links:
  - retailer: "Amazon"
    price: "$XX.XX"
    url: "https://amazon.com/dp/XXXXX?tag=your-tag"
  - retailer: "AliExpress"
    price: "$XX.XX"
    url: "https://s.click.aliexpress.com/e/your-link"

comparison_products:
  - name: "Competitor 1"
    url: "/reviews/YYYY/MM/competitor-1-review/"
  - name: "Competitor 2"
    url: "/reviews/YYYY/MM/competitor-2-review/"

excerpt: "SEO-optimized 150-160 character description that includes product name and key benefit."
---
```

### Field Guidelines

**Title:** 
- Include brand and model
- Add one key differentiator or feature
- Keep under 60 characters for SEO
- Examples:
  - "QCY H3 Review - Budget ANC That Punches Above Its Weight"
  - "Moondrop Blessing 3 Review - The New Mid-Fi King?"

**Rating (out of 10):**
- 9.0-10.0: Exceptional, class-leading
- 8.0-8.9: Excellent, highly recommended
- 7.0-7.9: Good, recommended with caveats
- 6.0-6.9: Decent, for specific use cases
- 5.0-5.9: Mediocre, hard to recommend
- Below 5.0: Not recommended

**Verdict:**
- One sentence, under 100 characters
- Capture the essence without spoilers
- Examples:
  - "Best budget ANC headphones under $50"
  - "Excellent tuning held back by mediocre build"
  - "A safe bet for Harman lovers"

**Tags:**
- Use existing tags when possible
- Common tags: bluetooth, wired, anc, open-back, closed-back, budget, mid-fi, summit-fi, v-shaped, neutral, warm, bright

**Pros & Cons:**
- Be specific, not vague
- ✅ Good: "ANC blocks out 85% of subway noise"
- ❌ Bad: "Good ANC"
- Aim for 3-5 of each

## Review Structure

### 1. Introduction (2-3 paragraphs)

Hook the reader and set expectations:

```markdown
The [Product] enters an increasingly crowded [category] market at [price point]. 
[Brand] claims [key marketing points], but how does it actually perform?

I've spent [timeframe] testing the [Product] across [use cases]. This review 
combines objective measurements from my [measurement rig] with real-world listening 
impressions to give you the complete picture.

**TL;DR:** [One paragraph verdict for people who want the quick answer]
```

### 2. What's in the Box (1 paragraph)

Quick unboxing overview:

```markdown
## What's in the Box

The [Product] arrives in [packaging description]. Inside you'll find:
- The [product] itself
- [Cable/accessories]
- [Case/storage]
- [Documentation]

[Comment on packaging quality and accessory value - keep brief]
```

### 3. Build Quality & Comfort (2-3 paragraphs)

Physical assessment:

```markdown
## Build Quality & Comfort

### Build
[Materials, construction, durability concerns, notable design features]

### Comfort
[Fit, weight, pressure points, long-session comfort, different head sizes]
[For IEMs: tip selection, nozzle size, isolation]

### Controls & Features
[Buttons, touch controls, app features, battery life, connectivity]
```

### 4. Sound Quality (This is the meat - 4-6 paragraphs)

Break down by frequency:

```markdown
## Sound Quality

### Frequency Response
[Link to your measurement graph or embed it]

The [Product] follows a [describe tuning - neutral, v-shaped, warm, etc.] tuning 
with [notable deviations from target].

### Bass
[Sub-bass extension, mid-bass punch, texture, bleeding into mids, specific songs tested]
**Tested with:** [Song examples that showcase bass]

### Mids
[Vocal presentation, male vs female, instrument timbre, recession or forwardness]
**Tested with:** [Song examples]

### Treble
[Extension, sibilance, air, detail retrieval, fatigue]
**Tested with:** [Song examples]

### Technicalities
- **Soundstage:** [Width, depth, imaging precision]
- **Detail:** [Micro-detail retrieval, separation]
- **Dynamics:** [Punch, impact, transient response]
```

**Pro Tips:**
- Reference specific songs (artist - track)
- Compare to products at similar price points
- Use descriptive language but avoid audiophile nonsense
- Include both strengths and weaknesses

### 5. Measurements Deep Dive (Optional - for technical reviews)

```markdown
## Measurements Analysis

[Embed your Squiglink measurement]

### Comparison with [Target Curve]
[Detailed analysis of deviations and their audibility]

### vs. Competition
[Graph comparing to similar products with commentary]
```

### 6. Use Cases (2 paragraphs)

Who is this for?

```markdown
## Who Should Buy This?

**Best for:**
- [Specific use case 1 with reasoning]
- [Specific use case 2 with reasoning]

**Skip if:**
- [Deal-breaker scenario 1]
- [Deal-breaker scenario 2]
```

### 7. Final Verdict (2-3 paragraphs)

Wrap it up:

```markdown
## Final Verdict

[Summarize strengths and weaknesses]

At [price], the [Product] [competes/doesn't compete] well with [alternatives]. 
[Final recommendation with caveats]

**Rating: X.X/10**

[One-sentence final thought]
```

### 8. Where to Buy

This is auto-generated from your frontmatter affiliate_links, but you can add commentary:

```markdown
## Where to Buy

[The template will auto-generate buy buttons from your frontmatter]

*Note: Prices may vary. Links are affiliate links that support the site at no cost to you.*
```

## Writing Tips

### Voice & Tone
- **Conversational but authoritative** - you're a knowledgeable friend, not a salesperson
- **Honest about flaws** - readers trust reviewers who point out problems
- **Specific, not vague** - "reduces noise by ~20dB" beats "good noise cancellation"
- **Avoid hype** - no "INSANE BASS" or "DESTROYS the competition"

### SEO Best Practices
- Include product name in first paragraph
- Use H2 headers (##) for main sections
- Include price within first 200 words
- Link to related reviews when relevant
- Alt text for images should describe what's shown
- Keep paragraphs short (2-4 sentences) for readability

### Markdown Formatting

**Bold** for emphasis on key points:
```markdown
**The bass is exceptional at this price.**
```

*Italics* for product names or subtle emphasis:
```markdown
The *QCY H3* competes well with *Sony's WH-CH720N*.
```

Lists for easy scanning:
```markdown
- Clear point 1
- Clear point 2
```

Links to measurements:
```markdown
[View full measurements →]({{ page.measurement_url }})
```

Internal links to other reviews:
```markdown
Similar to the [QCY H2](/reviews/2024/12/qcy-h2-review/), but improved.
```

### Images

Save images to `/assets/images/reviews/product-name-description.jpg`

Include in markdown:
```markdown
![QCY H3 product shot](/assets/images/reviews/qcy-h3-product.jpg)
*The QCY H3 in all its glory*
```

**Image checklist:**
- [ ] Product hero shot (featured image)
- [ ] Unboxing/contents
- [ ] Build quality close-ups
- [ ] Measurement graph (or embed from Squiglink)
- [ ] Size comparison (optional)

Optimize before uploading:
- Resize to max 1920px wide
- Compress to ~200KB per image
- Use .webp if possible, .jpg if not

## YouTube Integration

Add your YouTube video ID to frontmatter:
```yaml
youtube_id: "dQw4w9WgXcQ"
```

Embed in review:
```markdown
{% include youtube-embed.html id=page.youtube_id %}
```

## Publishing Checklist

Before you commit and push:

- [ ] Proofread for typos and grammar
- [ ] Verify all links work
- [ ] Check image paths are correct
- [ ] Confirm affiliate links are correct
- [ ] Test measurement embed loads
- [ ] Verify frontmatter YAML is valid
- [ ] Ensure date is correct in filename
- [ ] Add alt text to all images
- [ ] Review on mobile layout (test locally if possible)

## Git Workflow

```bash
# Create the review
vim _posts/2025-10-30-product-name-review.md

# Add images
cp ~/photos/product.jpg assets/images/reviews/

# Add and commit
git add _posts/2025-10-30-product-name-review.md
git add assets/images/reviews/product-*
git commit -m "Add [Product Name] review"

# Push to GitHub
git push origin main

# Wait 1-2 minutes for GitHub Pages to build
# Check live site
```

## Common Mistakes to Avoid

❌ **Don't:**
- Copy manufacturer marketing text
- Use vague audiophile terms without explanation
- Skip the cons section
- Forget to link to measurements
- Use "I" excessively (some is fine, but don't overdo it)
- Write walls of text without headers

✅ **Do:**
- Back up subjective claims with measurements when possible
- Compare to specific competing products
- Include real song examples
- Be honest about who shouldn't buy this
- Link to related reviews
- Format for scannability

## Example Review Snippet

Here's what a good intro + sound section looks like:

```markdown
The QCY H3 enters the budget ANC market at just $45, promising "studio-quality sound" 
and "industry-leading noise cancellation." Bold claims for such a modest price tag.

I've been daily-driving the H3 for two weeks, testing them on flights, commutes, and 
extended listening sessions. This review combines measurements from my GRAS 43AG rig 
with real-world impressions.

**TL;DR:** The H3 delivers surprising sound quality for the price, with excellent ANC 
that genuinely competes with $100+ models. Build quality is the main compromise, but 
if you can look past the creaky plastic, there's serious value here.

## Sound Quality

### Frequency Response

[Measurement graph]

The H3 follows a pleasant consumer-friendly tuning with boosted bass and slightly 
recessed mids. Treble extends reasonably well without excessive peaks.

### Bass

Sub-bass reaches down to 30Hz with solid extension - impressive for Bluetooth headphones 
in this price range. The mid-bass has good punch without bloating into the lower mids. 

**Tested with:**
- Billie Eilish - "bad guy" - Sub-bass hits hard, clean impact
- Kendrick Lamar - "HUMBLE." - Kick drums have authority without muddiness

Bassheads will be happy, but it's not overwhelming. The bass is well-controlled and 
maintains decent texture even at higher volumes.

[Continue with mids, treble, etc...]
```

## Templates & Shortcuts

Create templates for common sections you reuse:

`~/.vim/templates/review-intro.md`:
```markdown
The [PRODUCT] enters the [CATEGORY] market at [PRICE], promising [KEY_FEATURES]. 

I've spent [TIMEFRAME] testing the [PRODUCT] across [USE_CASES]. This review combines 
objective measurements with real-world listening impressions.

**TL;DR:** [ONE_PARAGRAPH_VERDICT]
```

## Questions?

If something in this guide isn't clear, or you want to suggest improvements:
- Open an issue on GitHub
- Reference this guide in your commits
- Build your own style within these guidelines

Happy reviewing! 🎧
