<p align="center">
  <a>
    <img src="assets/logo.png" alt="Logo" width="100" >
  </a>
</p>

<h1 align="center">Public Transports Paris IDF</h1>

<p align="center">
  <p align="center">
    Calculates the shortest paths between two subway station in the Paris public transportation network.
  </p>  
  <p align="center">
    (includes RER and Metro only)
  </p>  
  <p align="center">
    <a href="https://github.com/hugo-HDSF/public_transports_paris_idf/blob/main/transports_paths.svg"><strong>View Exemple »</strong></a>
    .
    <a href="https://github.com/hugo-HDSF/public_transports_paris_idf/issues">Report Bug</a>
    .
    <a href="https://github.com/hugo-HDSF/public_transports_paris_idf/issues">Request Feature</a>
    .
    <img src="https://img.shields.io/github/license/ucan-lab/docker-laravel" alt="License" height="15">  
  </p>
</p>

<div align="center">

![Python](https://img.shields.io/badge/-Python_3.9-3776AB?logo=python&logoColor=white)
![Json](https://img.shields.io/badge/-Json-000000?logo=json&logoColor=white)
![.ENV](https://img.shields.io/badge/-.env-ECD53F?logo=dotenv&logoColor=black)
![Pycharm](https://img.shields.io/badge/-Pycharm-000000?logo=pycharm&logoColor=white)
</div>
<div align="center">

![NetworkX](https://img.shields.io/badge/-NetworkX_3.1-FFD43B?logo=networkx&logoColor=black)
![Matplotlib](https://img.shields.io/badge/-Matplotlib_3.7-FFD43B?logo=matplotlib&logoColor=black)
![FuzzyWuzzy](https://img.shields.io/badge/-FuzzyWuzzy_0.18-FFD43B?logo=fuzzywuzzy&logoColor=black)
![Chardet](https://img.shields.io/badge/-Chardet_5.1-FFD43B?logo=chardet&logoColor=black)
</div>

-----

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Data Sources](#data-source)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Usage](#usage)
    * [Target and Source variables](#target-and-source-variables)
    * [Control variables](#control-variables)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

![Screen Shot](assets/graph_screenshot_thumbnail.png)

This project visualizes the shortest paths between two subway stations in the Paris public transportation network (RER and Metro only). It leverages NetworkX, a powerful library for working with
networks and graphs, to process and analyze the underlying subway network data. The output is a high-resolution SVG image that highlights the shortest path and includes relevant information about the
stations and the lines.

## Built With

* [Python](https://www.python.org/)
* [NetworkX](https://networkx.org/)
* [Matplotlib](https://matplotlib.org/)

## Data Source

* [Data.gouv.fr](https://www.data.gouv.fr/fr/)

### Transports List

#### RER

Added :
<p>
  <span style="white-space:normal">
  <span data-sort-value="A !"></span><img alt="(A)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Paris_transit_icons_-_RER_A.svg/18px-Paris_transit_icons_-_RER_A.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Paris_transit_icons_-_RER_A.svg/27px-Paris_transit_icons_-_RER_A.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Paris_transit_icons_-_RER_A.svg/36px-Paris_transit_icons_-_RER_A.svg.png 2x" data-file-width="250" data-file-height="250">
  <span data-sort-value="B !"></span><img alt="(B)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Paris_transit_icons_-_RER_B.svg/18px-Paris_transit_icons_-_RER_B.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Paris_transit_icons_-_RER_B.svg/27px-Paris_transit_icons_-_RER_B.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Paris_transit_icons_-_RER_B.svg/36px-Paris_transit_icons_-_RER_B.svg.png 2x" data-file-width="250" data-file-height="250">
  <span data-sort-value="C !"></span><img alt="(C)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Paris_transit_icons_-_RER_C.svg/18px-Paris_transit_icons_-_RER_C.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Paris_transit_icons_-_RER_C.svg/27px-Paris_transit_icons_-_RER_C.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Paris_transit_icons_-_RER_C.svg/36px-Paris_transit_icons_-_RER_C.svg.png 2x" data-file-width="250" data-file-height="250">
  <span data-sort-value="D !"></span><img alt="(D)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Paris_transit_icons_-_RER_D.svg/18px-Paris_transit_icons_-_RER_D.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Paris_transit_icons_-_RER_D.svg/27px-Paris_transit_icons_-_RER_D.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Paris_transit_icons_-_RER_D.svg/36px-Paris_transit_icons_-_RER_D.svg.png 2x" data-file-width="250" data-file-height="250">
  <span data-sort-value="E !"></span><img alt="(E)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Paris_transit_icons_-_RER_E.svg/18px-Paris_transit_icons_-_RER_E.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Paris_transit_icons_-_RER_E.svg/27px-Paris_transit_icons_-_RER_E.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Paris_transit_icons_-_RER_E.svg/36px-Paris_transit_icons_-_RER_E.svg.png 2x" data-file-width="250" data-file-height="250">
  </span>
</p>

#### Metro

Added :
<p>
<span style="white-space:normal">
<span data-sort-value="01 !"></span><img alt="(1)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Paris_transit_icons_-_M%C3%A9tro_1.svg/18px-Paris_transit_icons_-_M%C3%A9tro_1.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Paris_transit_icons_-_M%C3%A9tro_1.svg/27px-Paris_transit_icons_-_M%C3%A9tro_1.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Paris_transit_icons_-_M%C3%A9tro_1.svg/36px-Paris_transit_icons_-_M%C3%A9tro_1.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="02 !"></span><img alt="(2)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Paris_transit_icons_-_M%C3%A9tro_2.svg/18px-Paris_transit_icons_-_M%C3%A9tro_2.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Paris_transit_icons_-_M%C3%A9tro_2.svg/27px-Paris_transit_icons_-_M%C3%A9tro_2.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Paris_transit_icons_-_M%C3%A9tro_2.svg/36px-Paris_transit_icons_-_M%C3%A9tro_2.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="03 !"></span><img alt="(3)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Paris_transit_icons_-_M%C3%A9tro_3.svg/18px-Paris_transit_icons_-_M%C3%A9tro_3.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Paris_transit_icons_-_M%C3%A9tro_3.svg/27px-Paris_transit_icons_-_M%C3%A9tro_3.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Paris_transit_icons_-_M%C3%A9tro_3.svg/36px-Paris_transit_icons_-_M%C3%A9tro_3.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="03bis !"></span><img alt="(3bis)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Paris_transit_icons_-_M%C3%A9tro_3bis.svg/18px-Paris_transit_icons_-_M%C3%A9tro_3bis.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Paris_transit_icons_-_M%C3%A9tro_3bis.svg/27px-Paris_transit_icons_-_M%C3%A9tro_3bis.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Paris_transit_icons_-_M%C3%A9tro_3bis.svg/36px-Paris_transit_icons_-_M%C3%A9tro_3bis.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="04 !"></span><img alt="(4)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Paris_transit_icons_-_M%C3%A9tro_4.svg/18px-Paris_transit_icons_-_M%C3%A9tro_4.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Paris_transit_icons_-_M%C3%A9tro_4.svg/27px-Paris_transit_icons_-_M%C3%A9tro_4.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Paris_transit_icons_-_M%C3%A9tro_4.svg/36px-Paris_transit_icons_-_M%C3%A9tro_4.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="05 !"></span><img alt="(5)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Paris_transit_icons_-_M%C3%A9tro_5.svg/18px-Paris_transit_icons_-_M%C3%A9tro_5.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Paris_transit_icons_-_M%C3%A9tro_5.svg/27px-Paris_transit_icons_-_M%C3%A9tro_5.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Paris_transit_icons_-_M%C3%A9tro_5.svg/36px-Paris_transit_icons_-_M%C3%A9tro_5.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="06 !"></span><img alt="(6)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Paris_transit_icons_-_M%C3%A9tro_6.svg/18px-Paris_transit_icons_-_M%C3%A9tro_6.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Paris_transit_icons_-_M%C3%A9tro_6.svg/27px-Paris_transit_icons_-_M%C3%A9tro_6.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Paris_transit_icons_-_M%C3%A9tro_6.svg/36px-Paris_transit_icons_-_M%C3%A9tro_6.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="07 !"></span><img alt="(7)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Paris_transit_icons_-_M%C3%A9tro_7.svg/18px-Paris_transit_icons_-_M%C3%A9tro_7.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Paris_transit_icons_-_M%C3%A9tro_7.svg/27px-Paris_transit_icons_-_M%C3%A9tro_7.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Paris_transit_icons_-_M%C3%A9tro_7.svg/36px-Paris_transit_icons_-_M%C3%A9tro_7.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="07bis !"></span><img alt="(7bis)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Paris_transit_icons_-_M%C3%A9tro_7bis.svg/18px-Paris_transit_icons_-_M%C3%A9tro_7bis.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Paris_transit_icons_-_M%C3%A9tro_7bis.svg/27px-Paris_transit_icons_-_M%C3%A9tro_7bis.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Paris_transit_icons_-_M%C3%A9tro_7bis.svg/36px-Paris_transit_icons_-_M%C3%A9tro_7bis.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="08 !"></span><img alt="(8)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Paris_transit_icons_-_M%C3%A9tro_8.svg/18px-Paris_transit_icons_-_M%C3%A9tro_8.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Paris_transit_icons_-_M%C3%A9tro_8.svg/27px-Paris_transit_icons_-_M%C3%A9tro_8.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Paris_transit_icons_-_M%C3%A9tro_8.svg/36px-Paris_transit_icons_-_M%C3%A9tro_8.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="09 !"></span><img alt="(9)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Paris_transit_icons_-_M%C3%A9tro_9.svg/18px-Paris_transit_icons_-_M%C3%A9tro_9.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Paris_transit_icons_-_M%C3%A9tro_9.svg/27px-Paris_transit_icons_-_M%C3%A9tro_9.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Paris_transit_icons_-_M%C3%A9tro_9.svg/36px-Paris_transit_icons_-_M%C3%A9tro_9.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="10 !"></span><img alt="(10)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Paris_transit_icons_-_M%C3%A9tro_10.svg/18px-Paris_transit_icons_-_M%C3%A9tro_10.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Paris_transit_icons_-_M%C3%A9tro_10.svg/27px-Paris_transit_icons_-_M%C3%A9tro_10.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Paris_transit_icons_-_M%C3%A9tro_10.svg/36px-Paris_transit_icons_-_M%C3%A9tro_10.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="11 !"></span><img alt="(11)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Paris_transit_icons_-_M%C3%A9tro_11.svg/18px-Paris_transit_icons_-_M%C3%A9tro_11.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Paris_transit_icons_-_M%C3%A9tro_11.svg/27px-Paris_transit_icons_-_M%C3%A9tro_11.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Paris_transit_icons_-_M%C3%A9tro_11.svg/36px-Paris_transit_icons_-_M%C3%A9tro_11.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="12 !"></span><img alt="(12)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Paris_transit_icons_-_M%C3%A9tro_12.svg/18px-Paris_transit_icons_-_M%C3%A9tro_12.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Paris_transit_icons_-_M%C3%A9tro_12.svg/27px-Paris_transit_icons_-_M%C3%A9tro_12.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Paris_transit_icons_-_M%C3%A9tro_12.svg/36px-Paris_transit_icons_-_M%C3%A9tro_12.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="13 !"></span><img alt="(13)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Paris_transit_icons_-_M%C3%A9tro_13.svg/18px-Paris_transit_icons_-_M%C3%A9tro_13.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Paris_transit_icons_-_M%C3%A9tro_13.svg/27px-Paris_transit_icons_-_M%C3%A9tro_13.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Paris_transit_icons_-_M%C3%A9tro_13.svg/36px-Paris_transit_icons_-_M%C3%A9tro_13.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="14 !"></span><img alt="(14)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Paris_transit_icons_-_M%C3%A9tro_14.svg/18px-Paris_transit_icons_-_M%C3%A9tro_14.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Paris_transit_icons_-_M%C3%A9tro_14.svg/27px-Paris_transit_icons_-_M%C3%A9tro_14.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Paris_transit_icons_-_M%C3%A9tro_14.svg/36px-Paris_transit_icons_-_M%C3%A9tro_14.svg.png 2x" data-file-width="250" data-file-height="250">
<span data-sort-value="15 !"></span><img alt="(15)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Paris_transit_icons_-_M%C3%A9tro_15.svg/18px-Paris_transit_icons_-_M%C3%A9tro_15.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Paris_transit_icons_-_M%C3%A9tro_15.svg/27px-Paris_transit_icons_-_M%C3%A9tro_15.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Paris_transit_icons_-_M%C3%A9tro_15.svg/36px-Paris_transit_icons_-_M%C3%A9tro_15.svg.png 2x" data-file-width="250" data-file-height="250">
</span>
</p>

to add :
<p>
<span style="white-space:normal">
<span data-sort-value="16 !"></span><a href="/wiki/Ligne_16_du_m%C3%A9tro_de_Paris" title="Ligne 16 du métro de Paris"><img alt="(16)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Paris_transit_icons_-_M%C3%A9tro_16.svg/18px-Paris_transit_icons_-_M%C3%A9tro_16.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Paris_transit_icons_-_M%C3%A9tro_16.svg/27px-Paris_transit_icons_-_M%C3%A9tro_16.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Paris_transit_icons_-_M%C3%A9tro_16.svg/36px-Paris_transit_icons_-_M%C3%A9tro_16.svg.png 2x" data-file-width="250" data-file-height="250"></a>
<span data-sort-value="17 !"></span><a href="/wiki/Ligne_17_du_m%C3%A9tro_de_Paris" title="Ligne 17 du métro de Paris"><img alt="(17)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Paris_transit_icons_-_M%C3%A9tro_17.svg/18px-Paris_transit_icons_-_M%C3%A9tro_17.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Paris_transit_icons_-_M%C3%A9tro_17.svg/27px-Paris_transit_icons_-_M%C3%A9tro_17.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Paris_transit_icons_-_M%C3%A9tro_17.svg/36px-Paris_transit_icons_-_M%C3%A9tro_17.svg.png 2x" data-file-width="250" data-file-height="250"></a>
<span data-sort-value="18 !"></span><a href="/wiki/Ligne_18_du_m%C3%A9tro_de_Paris" title="Ligne 18 du métro de Paris"><img alt="(18)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Paris_transit_icons_-_M%C3%A9tro_18.svg/18px-Paris_transit_icons_-_M%C3%A9tro_18.svg.png" decoding="async" width="18" height="18" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Paris_transit_icons_-_M%C3%A9tro_18.svg/27px-Paris_transit_icons_-_M%C3%A9tro_18.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Paris_transit_icons_-_M%C3%A9tro_18.svg/36px-Paris_transit_icons_-_M%C3%A9tro_18.svg.png 2x" data-file-width="250" data-file-height="250"></a>
</span>
</p>

## Getting Started

To get a local copy up and running, follow these simple steps:

### Prerequisites

Ensure you have Python 3.9+ installed on your system. You can check your Python version by running:

```sh
python --version
```

### Installation

1. Clone the repository
```sh
git clone https://github.com/hugo-HDSF/public_transports_paris_idf.git
```
3. Create a virtual environment (optional). we recommend using Pycharm built in virtual environment.
>PyCharm makes it possible to use the virtualenv tool to create a project-specific isolated virtual environment. Follow [instructions](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html).
4. Install the required packages. (all packages are listed in the [main.py](main.py) file)
>We recommend to try out the new Jetbrains UI and their new redesigned packaging manager support in Python Packages Pycharm tool window. Follow [instructions](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html).
## Usage

### Target and Source variables

Visit the [updated_data.json](updated_data.json) file to see the subway station structure. Select both source and target stations and set global variables according to your chose at the start of the
script:

```source = "garibaldi"```

```target = "mairie d'issy"```

Then run the [main.py](main.py) python script with the according python interpreter configuration.
It will then calculate the shortest paths between these stations and generate a high-resolution SVG image in the same directory.

### Control variables

Set to True if you want to see multiple path options:

```multiple_path_options = True```

set the weight of the changing line penality according to your preferences:

```changing_line_penality = 300```

Set the weight of the walking to nearest station reward (makes sur the algorithm considers station connections as easy paths, we recommend setting it to the sum of the node and edge weight to balance
weight cost):

```walking_to_nearest_station_reward = 55```

Set the weight of the nodes:

```node_weight = 5```

Set the weight of the edges:

```edge_weight = 50```

## Roadmap

See the [open issues](https://github.com/hugo-HDSF/public_transports_paris_idf/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/hugo-HDSF/public_transports_paris_idf/issues/new) to discuss it, or directly create a pull request
  after you edit the [*README.md*](README.md) file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.

## License

Distributed under the MIT License.

## Authors

* **DA SILVA Hugo** - *Student - Fullstack Developer* - [Github](https://github.com/hugo-HDSF/)
* **MOHAMMEDI Tayeb** - *Student - Fullstack Developer* - Github

## Acknowledgements

* [Paris Nanterre University](https://www.parisnanterre.fr/)
* [Data.gouv.fr](https://www.data.gouv.fr/fr/)
* [Img Shields](https://shields.io/)
* [Simple Icons](https://simpleicons.org/)
* [Readme Generator](https://readme.shaankhan.dev/)

###### _Study Project | (BACHELOR) 2022-2023_
