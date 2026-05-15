from pathlib import Path
p=Path(__file__).resolve().parents[2]/'context/scripts/build_triangle_site.py'
s=p.read_text()
s=s.replace("<h1>{name} for Triangle businesses that need to be found, trusted, and understood by AI search.</h1>","<h1>{name} for Triangle businesses that need clearer signals in a research-heavy market.</h1>")
s=s.replace("<h1>Free Website Offer for Triangle businesses that need to be found, trusted, and understood by AI search.</h1>","<h1>Free Website Offer for Triangle businesses that need a stronger base before marketing can compound.</h1>")
s=s.replace("<h1>Web Design for Triangle businesses that need to be found, trusted, and understood by AI search.</h1>","<h1>Web Design for Triangle businesses that need to sound clear, current, and credible fast.</h1>")
s=s.replace("<h1>AI Search + Local SEO for Triangle businesses that need to be found, trusted, and understood by AI search.</h1>","<h1>AI Search + Local SEO for Triangle businesses that need clearer signals across Google, maps, and answer engines.</h1>")
s=s.replace("<h1>Google Ads for Triangle businesses that need to be found, trusted, and understood by AI search.</h1>","<h1>Google Ads for Triangle businesses that need paid traffic connected to a page that actually earns trust.</h1>")
p.write_text(s)
print('fixed service h1 voice')
