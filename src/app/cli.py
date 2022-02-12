import click
from app.services.user_management import UserManagementService
from infra.redis_user_repository import UserRedisRepository
from im.services.password_hash_service import PasswordHashingService
from im.events.domain_event_publisher import DomainEventPublisher

user_repo = UserRedisRepository()
pwd_hash_srv = PasswordHashingService()
event_publisher = DomainEventPublisher()
user_management_srv = UserManagementService(
    user_repo=user_repo, pwd_hash_srv=pwd_hash_srv, event_publisher=event_publisher
)


@click.group()
def cli():
    pass


@click.command()
@click.option("--username", prompt="Username")
@click.option("--password", prompt="Password")
@click.option("--email", prompt="Email")
def adduser(username: str, password: str, email: str):
    click.echo("Registering new user...")
    try:
        user_management_srv.register_user(username, password, email)
    except Exception as e:
        msg = f"Failed to register user. {e}"
        click.echo(msg)
    else:
        click.echo("User registered successfully .")


@click.command()
def listusers():
    click.echo("Listing all users")
    users = user_management_srv.list_users()
    for user in users:
        click.echo(user)


cli.add_command(adduser)
cli.add_command(listusers)

if __name__ == "__main__":
    cli()
