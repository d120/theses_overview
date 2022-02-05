from jinja2 import FileSystemLoader, Environment, select_autoescape
from babel.support import Translations
from csv import DictReader


def load_data():
    fd = open("german.csv")
    g_reader = DictReader(fd, delimiter=";")
    fe = open("english.csv")
    e_reader = DictReader(fe, delimiter=";")

    return g_reader, e_reader


def main():
    loader = FileSystemLoader(".")
    env = Environment(
        loader=loader,
        extensions=["jinja2.ext.i18n"],
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("accordion.html.j2")
    data_d, data_e = load_data()

    translations = Translations.load("locale", ["en"])
    env.install_gettext_translations(translations)
    with open("english.html", "w") as f:
        f.write(template.render(groups=data_e))

    translations = Translations.load("locale", ["de"])
    env.install_gettext_translations(translations)
    template = env.get_template("accordion.html.j2")
    with open("german.html", "w") as f:
        f.write(template.render(groups=data_d))


if __name__ == "__main__":
    main()
