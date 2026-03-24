#!/usr/bin/env python3
import pathlib
import frontmatter

ROOT = pathlib.Path(__file__).parent.parent
RECIPES = ROOT / "recipes"


def main():
    for path in RECIPES.iterdir():
        post = frontmatter.load(path)
        link = f" - [{post['title']}]({path.relative_to(ROOT)})"
        print(link)


if __name__ == "__main__":
    main()
