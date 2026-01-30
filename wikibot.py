import click
from mylib.bot import scrape


@click.command()
@click.option("--name", help="web page to scrape")
def cli(name):
    results = scrape(name)
    click.echo(click.style(f"{results}:", bg="blue", fg="white"))


if __name__ == "__main__":
    cli()
