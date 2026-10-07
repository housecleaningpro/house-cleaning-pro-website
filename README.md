# House Cleaning Pro LLC Website

Static website for House Cleaning Pro LLC, serving Charlotte, Monroe, Waxhaw, Fort Mill, and surrounding communities.

## Local preview

Run a local server from the project directory:

```bash
python -m http.server 4173
```

Then open `http://127.0.0.1:4173/`.

Opening `index.html` directly via `file://` is suitable only for viewing the
layout. FormSubmit requires a web server to submit forms. With JavaScript
enabled, the page explains this limitation and preserves the entered details.

## Form delivery

The estimate and newsletter forms POST to FormSubmit and deliver submissions to
`hcleaningpro123@gmail.com`, with a testing copy to `artyom.khmyz@gmail.com`
through the `_cc` field. Each form has its own email subject. Newsletter
requests are emailed for manual handling; they do not create a mailing list.

After the first submission, open the activation email from FormSubmit in that
mailbox and confirm the recipient address to enable delivery. With JavaScript,
both forms use FormSubmit's AJAX endpoint and display sending, success, or error
messages on the same page. Buttons are disabled while sending; failed requests
preserve the entered details. A success response resets the form.
Without JavaScript, normal FormSubmit submission and reCAPTCHA remain available,
with `_next` returning to `https://cleaningproclt.com/`.
Test real email delivery from the hosted website after activation.

## Custom domain

The production address is `https://cleaningproclt.com/`. The root `CNAME`
file configures this domain for branch-based GitHub Pages publishing.
In repository Settings > Pages, confirm the custom domain is
`cleaningproclt.com` (required separately for Actions-based publishing).

At NameSilo, replace parking records for the root and `www` with:

| Type | Host | Value |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | housecleaningpro.github.io |

Use a blank host for the root if NameSilo requires it. Preserve unrelated
email and verification records. Once DNS checks pass and GitHub issues the
certificate, enable Enforce HTTPS in Settings > Pages.

## Included

- Responsive single-page website
- Custom 404 page
- Local fonts and static CSS
- LocalBusiness, WebSite, WebPage, and FAQ structured data
- Open Graph and Twitter sharing image
- `robots.txt` and `sitemap.xml`
