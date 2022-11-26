import re
from classes.database import Database


class Story:
    def __init__(self, row):
        self.id = row[0]
        self.headline = row[1]
        self.slug = row[2]

    def make_slug(self):
        self.slug = self.headline.lower()
        self.slug = self.slug.replace(" ", "_")
        self.slug = self.slug.replace("-", "_")
        self.slug = re.sub(r'[\(\)]', "", self.slug)
        print(self.id, self.slug)
        d = Database()
        sql = """
        update utils.news set slug = %s where id = %s
        """
        params = [self.slug, self.id]
        d.run_query(sql, params)
