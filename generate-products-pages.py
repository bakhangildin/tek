from pathlib import Path
from PIL import Image
import os
import string


def main():
    page_titles = [
        "Современные печи электрошлакового переплава",
        "Печи вакуумного дугового переплава нового поколения",
        "Дуговые печи малой и средней емкости с аллюминиевыми электрододержателями",
        "Агрегаты комплексной обработки стали (печь-ковш) - уникальные решения",
        "Руднотермические печи малой и средней мощности",
        "Печи сопротивления различного назначения, включая вакуумные",
        "Установки электросушки и нагрева футеровки сталеплавильных и промежуточных ковшей",
        "Теплоизолирующие крышки для сталеразливочных ковшей",
        "Система прямого контроля глубины металлической ванны в кристаллизаторах ЭШП и ВДП",
        "Биметаллические (медь-сталь, сталь-сталь) заготовки"
    ]
    for i, title in enumerate(page_titles):
        images = Path(str(i+1) + ".html").read_text()
        template = f"""
        <!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300&display=swap"
      rel="stylesheet"
    />
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" href="assets/favicon.svg" />

    <title>ООО &laquo;ТЭК-98&raquo;</title>
    <meta property="og:title" content="ООО &laquo;ТЭК-98&raquo;" />
    <meta property="og:site_name" content="ООО &laquo;ТЭК-98&raquo;" />
    <meta property="og:type" content="website" />
    <meta name="savepage-title" content="ООО &laquo;ТЭК-98&raquo;" />
    <meta
      name="savepage-description"
      content="ООО &laquo;ТЭК-98&raquo; -
    производство и продажа электротехнического оборудования"
    />
    <link rel="stylesheet" href="./style.css" />
    <link rel="stylesheet" href="./product.css" />
  </head>
  <body>
    <div class="header sticky">
      <div class="header__logo">
        <img src="assets/logo.png" alt="logo" />
      </div>
      <div class="header__menu">
        <div class="header__menu-item">
          <a href="index.html#main" class="header__menu-link">ГЛАВНАЯ</a>
        </div>
        <div class="header__menu-item">
          <a
            href="index.html#products"
            style="color: var(--color-bege-hover)"
            class="header__menu-link"
            >ПРОДУКЦИЯ</a
          >
        </div>
        <div class="header__menu-item">
          <a href="index.html#about" class="header__menu-link">О НАС</a>
        </div>
        <div class="header__menu-item">
          <a href="index.html#patents" class="header__menu-link"
            >ПАТЕНТЫ И НАГРАДЫ</a
          >
        </div>
        <div class="header__menu-item">
          <a href="index.html#contacts" class="header__menu-link">КОНТАКТЫ</a>
        </div>
      </div>
    </div>
    <div class="content">
      <div class="title">{title}</div>
      <div class="content__wrapper">
        <div class="slideshow">
          <div class="slideshow-container">
            {images}
            <a class="prev" onclick="plusSlides(-1)">❮</a>
            <a class="next" onclick="plusSlides(1)">❯</a>
          </div>
          <br />

          <div class="dots" style="text-align: center"></div>
        </div>

        <div class="description">
          <!-- TODO: ADD TEXT -->
        </div>
      </div>
      <div class="buttons__wrapper">
        <a href="{(i)%len(page_titles)}.html" class="button button__left">
          <p>{page_titles[(i-1)%len(page_titles)]}</p>
        </a>
        <a href="{(i+2)%len(page_titles)}.html" class="button button__right">
          <p>{page_titles[(i+1)%len(page_titles)]}</p>
        </a>
      </div>
    </div>

    <div class="footer">
      <p>© 2002 — 2022 ООО «ТЭК-98». Все права защищены.</p>
      <button class="open__modal">Связаться с нами</button>
    </div>

    <dialog>
      <div class="modal__wrapper">
        <div class="modal__header">
          <p class="modal__title">Связаться с нами</p>
          <button class="close__modal">&times;</button>
        </div>
        <form class="form" method="get">
          <label for="name">
            Имя
            <input type="text" name="name" id="name" />
          </label>
          <label for="email">
            Email
            <input type="email" name="email" id="email" />
          </label>
          <label for="phone">
            Телефон
            <input type="tel" name="phone" id="phone" />
          </label>
          <label for="message">
            Сообщение
            <textarea
              name="message"
              id="message"
              cols="30"
              rows="10"
            ></textarea>
          </label>
          <input type="submit" value="Отправить" />
        </form>
      </div>
    </dialog>
  </body>
  <script src="form.js"></script>
  <script src="./slider.js"></script>
</html>
"""
        Path(f"src/{i+1}.html").write_text(template)
    # products_old = os.listdir("products_old")
    # for product in products_old:
    #     idx = int(product.split(".")[0]) - 1
    #     folder_path = "products_old/" + product + "/"
    #     images = os.listdir(folder_path)
    #     # p = "products/" + str(idx+1)
    #     # os.mkdir(p)
    #     res = ""
    #     for i in range(len(images)):
    #         description = sorted(images)[i].replace(".jpg", "").replace(
    #             ".JPG", "").replace(".tif", "")
    #         print(description)
    #         a = sorted(images)[i].split(".")[0]
    #         res += f"""
    #         <div class="mySlides fade">
    #           <img
    #             src="./assets/products/{idx+1}/{a}.jpeg"
    #             style="width: 100%"
    #           />
    #           <div class="text">
    #            {description}
    #           </div>
    #         </div>

    #         """
    #     Path(str(idx+1) + ".html").write_text(res)
    # img = Image.open(folder_path + images[i])
    # img.thumbnail((1000, 1000), Image.ANTIALIAS)
    # img.save(p + "/" + a + ".jpeg", optimize=True, quality=85)


if __name__ == "__main__":
    main()
