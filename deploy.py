import click
import itertools
import subprocess

EXCLUDED_PATHS = [
    ".git/*",
    ".idea/*",
    __file__,
    "requirements.txt",
]


def main():
    exclusions: list[str] = list(itertools.chain.from_iterable(
        ["--exclude", path]
        for path in EXCLUDED_PATHS
    ))

    cmd = [
        "aws",
        "s3",
        "sync",
        ".",
        "s3://srir.me",
        *exclusions
    ]

    subprocess.check_call(cmd + ["--dryrun"])

    if click.confirm("Deploy?"):
        subprocess.check_call(cmd)


if __name__ == "__main__":
    main()