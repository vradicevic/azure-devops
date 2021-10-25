import click
var=
@click.command(help="This is hello app")
@click.option("--name",prompt="I need name",help="Need name")
@click.option("--color",prompt="I need color",help="Need color")

def hello(name,color):
    if name == "Thor":
        click.echo("Thor you r always red")
            
    else:
        click.echo(click.style(f"Hello {name}",fg=color))

if __name__ == "__main__":
    hello()
