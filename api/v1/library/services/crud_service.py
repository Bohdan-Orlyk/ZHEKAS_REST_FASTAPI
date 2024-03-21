from sqlmodel import Session, select
from sqlalchemy.exc import NoResultFound

from api.v1.library.models.article import Article
from api.v1.library.schemas.schemas import ArticleCreate


def create_article(*, session: Session, article: ArticleCreate) -> Article:
    new_article = Article(**article.model_dump())

    session.add(new_article)
    session.commit()

    return new_article


def get_articles(*, session: Session):
    stmt = select(Article)
    articles = session.exec(stmt)

    return articles


def get_articles_by_author(*, session: Session, authors_id: int):
    stmt = select(Article).where(Article.user_id == authors_id).group_by(Article.id)
    result = session.exec(stmt)

    return result.all()


def delete_article(*, session: Session, article_id: int):
    stmt = select(Article).where(Article.id == article_id)

    result = session.exec(stmt)

    try:
        article_to_delete = result.one()
        session.delete(article_to_delete)
        session.commit()

        return True
    except NoResultFound:
        return False
