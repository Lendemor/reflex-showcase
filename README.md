# What is it?

This is just a simple project showcasing all the Reflex components.

The full page fit in a single file, you can either:
- clone the project then follow "How to use"
- copy the file `reflex_showcase.py`


It's purpose is to be used by contributors to [Reflex](https://github.com/reflex-dev/reflex) so they can easily check if any of their PR has detrimental impact on some components.

As much as possible, this repo will try to avoid using workaround, so as not to hide any potential problem.

# How to use?

## I) Standalone

### A) With virtualenvwrapper

1. `git clone git@github.com:Lendemor/reflex-showcase.git`
1. `mkvirtualenv reflex-showcase`
2. `pip install git+https://github.com/reflex-dev/reflex@main`
4. `reflex init`
5. `reflex run`

> For more complete steps on running Reflex, visit the official repo !

### B) With something else

Send me the steps on how you'd set it up, and I'll gladly add it

## II) Inside reflex main project
### A) Unix system

Steps:
- `cd ~/workspace/`
- `git clone git+https://github.com/reflex-dev/reflex.git`
- `git clone git@github.com:Lendemor/reflex-showcase.git`
- `cd reflex`
- `mkdir -p "examples/showcase"`
- `cd examples/showcase`
- `poetry run reflex init`
- `cd ~/workspace/`
- ```ln -sf `pwd`/reflex-showcase/reflex_showcase/reflex_showcase.py reflex/examples/showcase/showcase/showcase.py```

# Preview

![A preview of Reflex Showcase](https://github.com/Lendemor/reflex-showcase/raw/master/preview.png)
