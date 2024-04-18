from sqlmodel import Session, select
from sqlalchemy.exc import NoResultFound, IntegrityError

from api.v1.library.models import Article, User
from api.v1.library.schemas.schemas import ArticleCreate, CreateUser


def create_article(*, session: Session, article: ArticleCreate, user_id: int) -> Article:
    new_article = Article(user_id=user_id, **article.model_dump())

    session.add(new_article)
    session.commit()

    return new_article


def get_articles(*, session: Session):
    stmt = select(Article).limit(5)
    articles = session.exec(stmt)

    return articles


def get_articles_by_author(*, session: Session, authors_id: int):
    stmt = select(Article).where(Article.user_id == authors_id).group_by(Article.id)
    result = session.exec(stmt)

    return result.all()


def delete_article(*, session: Session, article_id: int, user_email: str):
    stmt = (select(Article, User)
            .join(User)
            .where(Article.id == article_id)
            .where(User.email == user_email))

    result = session.exec(stmt)

    article_to_delete = result.first()
    if article_to_delete:
        session.delete(article_to_delete[0])
        session.commit()

        return True
    return False


def create_user(*, session: Session, user_schema: CreateUser) -> User | bool:
    new_user = User(**user_schema.model_dump())
    try:
        session.add(new_user)
        session.commit()

        return new_user
    except IntegrityError:
        return False


def get_auth_user(*, session: Session, user_email: str):
    stmt = select(User).where(User.email == user_email)

    try:
        result = session.exec(stmt)
        user = result.one()

        return user
    except NoResultFound:
        return None


def get_user_with_articles(*, session: Session):
    stmt = select(User)  # .where(User.email == user_schema.email)

    user_with_articles = session.exec(stmt)

    return user_with_articles
