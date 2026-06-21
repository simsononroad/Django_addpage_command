# Django Custom Management Command: addpage / Egyedi Django Management Command: addpage

---

## Part 1: English Description

A custom Django management command (`python manage.py addpage`) designed to accelerate workflow by automating the creation of new pages (URLs, views, and HTML templates) within your project. It utilizes Jinja2 templates to generate code snippets and appends them to your existing files.

### Features

* **Automatic URL Registration:** Appends the new route to your `urls.py` file.
* **View Generation:** Creates the required view function in your `views.py` file based on a pre-defined Jinja template.
* **HTML Template Creation:** Generates an empty HTML file inside the `templates/` directory.

---

### Prerequisites & Structure

The command expects a specific project structure and the following dependencies to function correctly:

#### 1. Dependencies

The script relies on the `jinja2` package for template rendering. If you haven't installed it yet, run:

```bash
pip install jinja2

```

#### 2. Expected File Structure

Because the script uses relative paths, it assumes your project is organized as follows:

```text
your_django_project/
│
├── management/
│   └── commands/
│       └── addpage.py  <-- This script
│   └── temps/          <-- Storage for your Jinja2 templates
│       ├── urls_temp.jinja
│       └── view_temp.jinja
|
│
├── templates/          <-- Destination directory for new HTML files
│
├── urls.py             <-- Target file for new URLs
└── views.py            <-- Target file for new view functions

```

> **Important Note:** The closing bracket (`]`) in your `urls.py` file must be on its own line. The script removes this line before appending the new URL pattern to maintain valid syntax.

---

### Usage

You can execute the command via Django's standard `manage.py` file.

#### Basic Usage

If you only provide the path argument, the script will automatically name the view function and the HTML file based on that path.

```bash
python manage.py addpage contact/

```

* **URL:** `contact/`
* **View Name:** `contact`
* **HTML File:** `templates/contact.html`

> **Warning:** The `path` argument must end with a trailing slash (`/`), otherwise the script will raise a `CommandError`.

#### Advanced Usage (Custom Names)

If you want to specify custom names for your view function or HTML file, you can use the optional flags:

```bash
python manage.py addpage products/ --viewname get_all_products --htmlname product_list

```

* **URL:** `products/`
* **View Name:** `get_all_products`
* **HTML File:** `templates/product_list.html` (The `.html` extension is added automatically if omitted).

---

#### How it Works Behind the Scenes

1. **Validation:** Checks if the path ends with a `/`.
2. **Cleanup:** Opens `urls.py` and removes the closing `]` bracket.
3. **Rendering:** Populates the `temps/urls_temp.jinja` and `temps/view_temp.jinja` templates with your arguments.
4. **File Writing:** Appends the rendered URL to `urls.py`, appends the view to `views.py`, and touches a new empty file in the `templates/` folder.

---

---

## 2. rész: Magyar leírás

Ez a script egy egyedi Django management command (`python manage.py addpage`), amely megkönnyíti és felgyorsítja az új aloldalak (URL-ek, nézetek/views és HTML sablonok) létrehozását a projektedben. Jinja2 sablonok alapján automatikusan generálja a kód részleteket, és fűzi hozzájuk a meglévő fájlokhoz.

### Funkciók

* **Automatikus URL regisztráció:** Hozzáadja az új útvonalat a `urls.py` fájlhoz.
* **Nézet (View) generálás:** Létrehozza a szükséges view függvényt a `views.py` fájlban egy előre megírt Jinja sablon alapján.
* **HTML sablon létrehozása:** Létrehoz egy üres HTML fájlt a `templates/` mappában.

---

### Előfeltételek és Struktúra

A parancs elvárja, hogy a következő struktúra és függőségek meglegyenek a projektben:

#### 1. Függőségek

A script a `jinja2` könyvtárat használja a sablonkezeléshez. Ha még nincs telepítve:

```bash
pip install jinja2

```

#### 2. Elvárt fájlstruktúra

A parancs relatív útvonalakat használ, így az alábbi struktúrát feltételezi:

```text
your_django_project/
│
├── management/
│   └── commands/
│       └── addpage.py  <-- Ez a script
│   └── temps/          <-- Itt kell lenniük a Jinja2 sablonoknak
│       ├── urls_temp.jinja
│       └── view_temp.jinja
│
├── templates/          <-- Ide fognak készülni a HTML fájlok
│
├── urls.py             <-- Ide fűzi be az új URL-t
└── views.py            <-- Ide fűzi be az új view-t

```

> **Fontos megjegyzés:** A `urls.py` fájl végén a lezáró szögletes zárójelnek (`]`) külön sorban kell lennie, mert a script ezt a sort törli, mielőtt hozzáfűzi az új URL mintát!

---

### Használat

A parancsot a Django megszokott `manage.py` fájlján keresztül tudod futtatni.

#### Alapértelmezett használat

Ha csak a path-t (elérési utat) adod meg, a script a path alapján automatikusan elnevezi a view függvényt és a HTML fájlt is.

```bash
python manage.py addpage kapcsolatisor/

```

* **URL:** `kapcsolatisor/`
* **View neve:** `kapcsolatisor`
* **HTML fájl:** `templates/kapcsolatisor.html`

> **Figyelem:** A `path` argumentum végén kötelező kitenni a `/` (per) jelet, különben a script hibát fog dobni!

#### Haladó használat (Egyedi nevek megadása)

Ha szeretnéd pontosan szabályozni, hogy mi legyen a view vagy a HTML fájl neve, használhatod az opcionális flag-eket:

```bash
python manage.py addpage termekek/ --viewname get_all_products --htmlname termek_lista

```

* **URL:** `termekek/`
* **View neve:** `get_all_products`
* **HTML fájl:** `templates/termek_lista.html` (A `.html` kiterjesztést a script automatikusan hozzáadja, ha lehagyod).

---

#### Hogyan működik a háttérben?

1. **Validálás:** Ellenőrzi, hogy a megadott útvonal `/` jellel végződik-e.
2. **Tisztítás:** Megnyitja a `urls.py` fájlt, és eltávolítja a lezáró `]` jelet, hogy az új URL-t be tudja illeszteni a listába.
3. **Renderelés:** A `temps/urls_temp.jinja` és `temps/view_temp.jinja` sablonokból behelyettesíti a megadott változókat.
4. **Fájlírás:** Hozzáírja a legenerált URL-t a `urls.py`-hoz, hozzáírja a legenerált view-t a `views.py`-hoz, valamint létrehoz egy új, üres állományt a `templates/` mappában a megadott HTML névvel.
