# House Cleaning Pro LLC Website

Static website for House Cleaning Pro LLC, serving Charlotte, Monroe, Waxhaw, Fort Mill, and surrounding communities.

## Local preview

Open `index.html` directly, or run a local server:

```bash
python -m http.server 4173
```

Then open `http://127.0.0.1:4173/`.

## Form delivery

The estimate and newsletter forms POST to FormSubmit and deliver submissions to
`hcleaningpro123@gmail.com`, with a testing copy to `atyom.khmyz@gmail.com`
through the `_cc` field. Each form has its own email subject. Newsletter
requests are emailed for manual handling; they do not create a mailing list.

After the first submission, open the activation email from FormSubmit in that
mailbox and confirm the recipient address to enable delivery. FormSubmit handles
reCAPTCHA, then redirects to the full website URL through `_next`, preserving
the GitHub Pages project path or the current custom domain. Without JavaScript,
the return URL defaults to `https://housecleaningpro.github.io/house-cleaning-pro-website/`.
Test delivery from the hosted website after activation.

## Included

- Responsive single-page website
- Custom 404 page
- Local fonts and static CSS
- LocalBusiness, WebSite, WebPage, and FAQ structured data
- Open Graph and Twitter sharing image
- `robots.txt` and `sitemap.xml`
