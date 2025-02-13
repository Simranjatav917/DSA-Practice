import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    article_views_df = views[views['author_id'] == views['viewer_id']].drop_duplicates()
    article_views_df= article_views_df[['author_id']].drop_duplicates().sort_values(by='author_id')
    return article_views_df[['author_id']].rename(columns={'author_id': 'id'})