"""Select random images for display."""

import glob
import random

if __name__ == "__main__":
    images = glob.glob("**/*.png", recursive=True)
    images = random.sample(images, 9)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(
            f"""# Designs
This repository contains some of my designs made using Illustrator.
Some of them:
<table>
    <tr>
      <td><img src="{images[0]}"></td>
      <td><img src="{images[1]}"></td>
      <td><img src="{images[2]}"></td>
    </tr>
    <tr>
      <td><img src="{images[3]}"></td>
      <td><img src="{images[4]}"></td>
      <td><img src="{images[5]}"></td>
    </tr>
    <tr>
      <td><img src="{images[6]}"></td>
      <td><img src="{images[7]}"></td>
      <td><img src="{images[8]}"></td>
    </tr>
</table>
"""
        )
