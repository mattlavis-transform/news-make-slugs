from classes.database import Database
from classes.story import Story


d = Database()
sql = """
select id, headline, slug from utils.news
-- where 'Tariff notices' = any(themes)
where slug is null
order by validity_start_date
"""
stories = []
params = []
rows = d.run_query(sql, params)
for row in rows:
    story = Story(row)
    stories.append(story)

for story in stories:
    story.make_slug()
