ReganCipher Blog Setup Guide
This guide will help you integrate the Jekyll blog with your existing Squiglink measurements site.
📁 File Structure
Your repo should look like this after adding the blog:
regancipher.github.io/
│
├── _config.yml                 # Jekyll configuration (NEW)
├── index.html                  # Blog homepage (NEW)
├── Gemfile                     # Ruby dependencies (NEW - see below)
│
├── _layouts/                   # Page templates (NEW)
│   ├── default.html
│   ├── home.html
│   └── review.html
│
├── _includes/                  # Reusable components (NEW)
│   ├── header.html
│   ├── footer.html
│   └── youtube-embed.html
│
├── _posts/                     # Your blog posts (NEW)
│   └── 2025-10-30-qcy-h3-review.md
│
├── assets/                     # Static assets (NEW)
│   ├── css/
│   │   └── main.css
│   └── images/
│       └── reviews/
│
├── measurements/               # Your EXISTING Squiglink setup
│   ├── data/
│   ├── styles/
│   ├── index.html
│   └── ... (all your existing files)
│
└── about.md                    # About page (NEW - optional)
🚀 Installation Steps
Step 1: Add Jekyll Dependencies
Create a Gemfile in your repo root:
rubysource "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins
gem "jekyll-seo-tag"
gem "jekyll-sitemap"
gem "jekyll-feed"
Step 2: Update Your Measurements Link
In your measurements site, add a link back to the blog. Edit measurements/index.html and add something like:
html<a href="/" class="back-to-blog">← Back to Reviews</a>
Step 3: Configure GitHub Pages

Go to your repo settings
Navigate to "Pages"
Set source to: Deploy from branch main (or master)
GitHub will automatically build Jekyll sites

Step 4: Add Your First Review
Copy the sample post structure from _posts/2025-10-30-qcy-h3-review.md and customize it:
markdown---
layout: review
title: "Your Product Name Review"
date: 2025-10-30
brand: "Brand Name"
price: "$XX.XX"
rating: 8.0
verdict: "One-sentence verdict here"

image: /assets/images/reviews/product-name.jpg
measurement_url: "https://regancipher.github.io/measurements/?share=Product_Name"
youtube_id: "YOUR_YOUTUBE_ID"

pros:
  - Pro point 1
  - Pro point 2

cons:
  - Con point 1
  - Con point 2

affiliate_links:
  - retailer: "Amazon"
    price: "$XX.XX"
    url: "https://amazon.com/your-link"

excerpt: "SEO-friendly excerpt for this review"
---

Your markdown content here...
🔗 Integrating Measurements
Option 1: iFrame Embed (Recommended)
Your Squiglink measurements can be embedded using the measurement_url field in your post frontmatter:
yamlmeasurement_url: "https://regancipher.github.io/measurements/?share=Product_Name"
The review template will automatically create an iframe embedding your measurement graph.
Option 2: Direct Link
If you prefer just linking to measurements instead of embedding:
markdown[View full measurements →](https://regancipher.github.io/measurements/?share=Product_Name)
🎨 Customization
Colors
Edit assets/css/main.css to change the color scheme. Key variables are at the top:
css:root {
  --primary-bg: #0d1117;      /* Main background */
  --accent-color: #58a6ff;    /* Links and buttons */
  /* ... etc */
}
Logo
Replace the emoji (🎧) in _includes/header.html with:

Your own emoji
An image: <img src="/assets/images/logo.png" alt="ReganCipher">

Adding Pages
Create new pages by adding markdown files to the root:
markdown---
layout: default
title: About
permalink: /about/
---

## About ReganCipher

Your content here...
📊 SEO Optimization
1. Every Post Should Have:

Descriptive title with product name
Excerpt (appears in search results)
Relevant tags/categories
Featured image

2. URL Structure
Jekyll automatically creates SEO-friendly URLs:
/reviews/2025/10/qcy-h3-review/
3. Internal Linking
Link between reviews and to your measurements:
markdownSimilar to the [QCY H2](/reviews/2024/12/qcy-h2-review/), but with improved ANC.
🔧 Local Testing (Optional)
To test locally before pushing:
bash# Install Jekyll
gem install bundler jekyll

# Navigate to your repo
cd regancipher.github.io

# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# View at http://localhost:4000
📝 Writing Workflow

Create new post in _posts/ folder using naming format: YYYY-MM-DD-title.md
Add frontmatter with all metadata (see sample post)
Write content in markdown
Add images to assets/images/reviews/
Add measurement link from your Squiglink database
Add YouTube embed using video ID
Commit and push to GitHub
Wait 1-2 minutes for GitHub Pages to rebuild
Check live site at regancipher.github.io

🎯 Affiliate Links
For each product, add affiliate links in the frontmatter:
yamlaffiliate_links:
  - retailer: "Amazon"
    price: "$39.99"
    url: "https://amazon.com/dp/XXXXX?tag=your-tag"
  - retailer: "AliExpress"
    price: "$34.99"
    url: "https://s.click.aliexpress.com/e/your-link"
These will automatically display in a "Where to Buy" section with proper nofollow attributes.
🚨 Important Notes
Measurements Directory
The Jekyll config specifically excludes your measurements/ directory from processing, so your Squiglink setup won't be affected.
Image Optimization

Use WebP format when possible for faster loading
Compress images before uploading
Recommended size: 1200x630px for featured images

Git Workflow
bashgit add .
git commit -m "Add [Product] review"
git push origin main
📈 Analytics Setup
Add Google Analytics by editing _config.yml:
yamlgoogle_analytics: UA-XXXXXXXXX-X
🐛 Troubleshooting
Site not building?

Check GitHub Actions tab for build errors
Verify YAML frontmatter syntax
Ensure all liquid tags are closed properly

Measurements not loading?

Verify the measurement_url is correct
Check that the product exists in your Squiglink database
Test the URL directly in browser

Styling looks broken?

Clear browser cache
Check that main.css path is correct
Verify CSS file is committed to repo

🎓 Next Steps

Add more reviews using the sample post as template
Customize colors to match your YouTube branding
Add Google Analytics to track traffic
Create category pages for organizing reviews
Add search functionality (using lunr.js)
Set up email newsletter (using Substack or similar)

📞 Need Help?

Jekyll docs: https://jekyllrb.com/docs/
GitHub Pages: https://docs.github.com/pages
Liquid syntax: https://shopify.github.io/liquid/


Remember: Every commit triggers a rebuild. Changes typically appear within 1-2 minutes on your live site.
