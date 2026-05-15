from pathlib import Path
p=Path(__file__).resolve().parents[2]/'context/scripts/build_triangle_site.py'
s=p.read_text()
repls={
"Bring your Triangle business into the AI search era.":"Make your Triangle business easier to understand before buyers ever call.",
"Triangle buyers are used to comparing quickly, researching deeply, and expecting clarity. Your website, GBP, service pages, FAQs, and paid landing pages need to help humans and AI systems understand why you are the right local choice.":"In the Triangle, buyers are comfortable doing their homework. They compare, skim, verify, and expect the business to sound competent without overselling. The website has to read like a clear brief: what you do, where you do it, why you are credible, and why the next step is low-friction.",
"A local growth stack built around trust, clarity, and AI visibility.":"A sharper digital base for a market that researches before it reaches out.",
"The website build can be free for qualifying service businesses when paired with the six-month growth partnership.":"The free build creates the base layer: a credible, structured site that monthly marketing can keep improving.",
"Pages, FAQs, schema, internal structure, and Google Business Profile work are shaped so people and AI systems can understand the business faster.":"The content is written to be specific, useful, and structured enough for buyers, Google, maps, and AI summaries to understand without guesswork.",
"Google Ads, local search, and map visibility perform better when the landing pages are clear, credible, and locally specific.":"Ads and local visibility work harder when the landing page already answers the smart questions Triangle buyers bring with them.",
"Educated, tech-aware buyers expect clarity before the call.":"A high-context market needs proof without noise.",
"Same practical growth services, with AI readiness moved to the center.":"Practical services, explained in the plain-spoken Triangle way: clear, useful, and built to compound.",
"Focused pages for the Triangle market.":"Local pages for the Triangle’s real decision zones.",
"Tell us what you want the website and AI visibility to fix.":"Tell us where the current lead path feels unclear.",
"AI-ready marketing support for {name} service businesses.":"Clearer digital visibility for {name} service businesses.",
"{angle} {BRAND} helps businesses in and around {name} look more credible, show up more clearly, and give both customers and AI search systems better information to work with.":"{angle} {BRAND} helps {name}-area businesses turn scattered online signals into a clearer website, cleaner local presence, and stronger AI-search-ready explanation of what they do.",
"Local visibility now has to serve humans and AI.":"Local visibility has to be clear enough for people and structured enough for AI.",
"We build clearer service pages, useful FAQs, local relevance, schema, and Google Business Profile alignment so {name} buyers can understand the business quickly whether they find it through Google, maps, ads, or AI-shaped search results.":"We connect service pages, FAQs, local relevance, schema, and Google Business Profile signals so {name} buyers do not have to work hard to understand the offer.",
"Website structure, offer clarity, local SEO, map visibility, citations, conversion paths, and paid-search landing pages.":"Sharper service explanations, local proof, GBP alignment, citations, conversion paths, and landing pages that respect how Triangle buyers compare options.",
"Free Website Offer for Triangle businesses that need to be found, trusted, and understood by AI search.":"Free Website Offer for Triangle businesses that need a stronger base before marketing can compound.",
"Web Design for Triangle businesses that need to be found, trusted, and understood by AI search.":"Web Design for Triangle businesses that need to sound clear, current, and credible fast.",
"AI Search + Local SEO for Triangle businesses that need to be found, trusted, and understood by AI search.":"AI Search + Local SEO for Triangle businesses that need clearer signals across Google, maps, and answer engines.",
"Google Ads for Triangle businesses that need to be found, trusted, and understood by AI search.":"Google Ads for Triangle businesses that need paid traffic connected to a page that actually earns trust.",
"keeps the work practical: stronger pages, clearer offers, local proof, structured FAQs, GBP alignment, and conversion paths that make the next step obvious.":"keeps the work grounded: specific pages, useful explanations, local proof, structured FAQs, GBP alignment, and conversion paths that do not make buyers think twice.",
"Built as part of a connected growth system, not a one-off tactic.":"Built like a system, not a stack of disconnected marketing chores.",
"Clarify the offer and local audience.":"Clarify the offer for Triangle buyers who compare before contacting.",
"Build pages that serve buyers, Google, maps, and AI answers.":"Write pages that are useful to people and legible to search and AI systems.",
"Keep improving visibility every month after launch.":"Use each month to sharpen the signals instead of letting the site sit still.",
"The goal is to make the business easier to find, easier to understand, easier to trust, and easier to contact.":"The goal is quiet competence: easier to find, easier to understand, easier to trust, and easier to contact.",
"Start with the foundation, then keep improving it.":"Start with the base layer, then keep making the signal clearer.",
"We look at the website, local search presence, Google Business Profile, service pages, and lead path together so each month compounds.":"We look at the website, local search presence, Google Business Profile, service pages, and lead path as one operating system, so each month makes the next one stronger."
}
for a,b in repls.items():
    s=s.replace(a,b)
# update docs/process notes
s=s.replace("Triangle brand: research-blue dominant, sky blue support, innovation green accent. Professional, smart, current, not generic SaaS.","Triangle brand voice: calm, intelligent, specific, and research-aware. It should sound like a clear operator briefing, not hype, not generic agency copy. Research-blue dominant, sky blue support, innovation green accent. Professional, smart, current, not generic SaaS.")
p.write_text(s)
print('triangle voice pass applied')
