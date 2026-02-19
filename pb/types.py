from dataclasses import dataclass
from typing import Literal
from os import path


Brand = Literal[
    "Arc'teryx",
    "Cabin Zero",
    "Cotopaxi",
    "Crumpler",
    "Crumpler",
    "Fjallraven",
    "Fjallraven",
    "Goruck",
    "MaH",
    "Patagonia",
    "Topo Designs",
]
"List of knonw brands. To be updated if a new backpack is added."


@dataclass
class Specs:
    h: float
    "Height in cm."

    w: float
    "Width in cm."

    d: float
    "Depth in cm."

    V: int
    "Volume in litres."

    W: int
    "Weight in grams."


@dataclass
class Backpack:
    brand_name: tuple[Brand, str]

    specs: Specs

    link: str
    """
    Last known sales/demo link.
    """

    price_sgd: int
    """
    Estimated price in SGD.
    """

    @property
    def height(self) -> float:
        return self.specs.h

    @property
    def width(self) -> float:
        return self.specs.w

    @property
    def depth(self) -> float:
        return self.specs.d

    @property
    def brand(self) -> str:
        return self.brand_name[0]

    @property
    def name(self) -> str:
        return self.brand_name[1]

    @property
    def file_stem(self) -> str:
        def sanitize(x):
            x = x.lower().encode("ascii", errors="ignore").decode()
            return x.replace(" ", "").replace(".", "-")

        stem = sanitize(self.name)
        brand = sanitize(self.brand)
        return brand + "--" + stem

    @property
    def asset_dir(self) -> str:
        """
        Filename of the markdown file.
        """
        return path.join("assets", self.file_stem)

    @property
    def filepath(self) -> str:
        """
        Filename of the markdown file.
        """
        return path.join("bp", self.file_stem + ".md")

    def markdown_row(self) -> list[str]:
        def link(url, display):
            return f"[{url}]({display})"

        return [
            "%s / %s" % (link(self.brand, self.link), link(self.name, self.filepath)),
            str(self.height),
            str(self.width),
            str(self.depth),
            str(self.specs.W),
            str(self.specs.V),
            str(self.price_sgd),
        ]

    @staticmethod
    def markdown_header() -> list[str]:
        return ["Name", "H/cm", "W/cm", "D/cm", "W/g", "V/L", "Price/$SGD"]
