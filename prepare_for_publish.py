from pathlib import Path
import os
import glob
import htmlmin
import cssmin


def main():
    src = Path("src")
    prod = Path("cp1251")
    for path in glob.glob(str(src.joinpath("*.html"))):
        print("processing", path)
        code = Path(path).read_text(encoding="utf-8")
        res = htmlmin.minify(
            code,
            remove_comments=True,
            remove_empty_space=True
        )
        res = code
        try:
            prod.joinpath(path.split("/")[-1]).write_text(res, "cp1251")
        except:
            prod.joinpath(path.split("/")[-1]).write_text(res, "utf-8")
            print("ERROR", path)

    for path in glob.glob(str(src.joinpath("*.css"))):
        print("processing", path)
        code = Path(path).read_text(encoding="utf-8")
        res = htmlmin.minify(
            code,
            remove_comments=True,
            remove_empty_space=True
        )
        prod.joinpath(path.split("/")[-1]).write_text(res)

    for path in glob.glob(str(src.joinpath("*.js"))):
        print("processing", path)
        code = Path(path).read_text(encoding="utf-8")
        prod.joinpath(path.split("/")[-1]).write_text(code)


if __name__ == "__main__":
    main()
