<br/>
<p align="center">
  <a href="https://github.com/ShaanCoding/ReadME-Generator">
    <img src="assets/logo.png" alt="Logo" width="100" >
  </a>

<h3 align="center">Public Transports Paris IDF</h3>

  <p align="center">
    Calculates the shortest paths between two subway station in the Paris public transportation network (includes RER and Metro only).
    <br/>
    <br/>
    <a href="https://github.com/hugo-HDSF/transports_paris_idf/transports_paths.svg"><strong>View Exemple »</strong></a>
    .
    <a href="https://github.com/hugo-HDSF/transports_paris_idf/issues">Report Bug</a>
    .
    <a href="https://github.com/hugo-HDSF/transports_paris_idf/issues">Request Feature</a>
  </p>
</p>

<div align="center">

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Pycharm](https://img.shields.io/badge/-Python-000000?logo=pycharm&logoColor=white)
![Homebrew](https://img.shields.io/badge/-Homebrew-FBB040?logo=homebrew&logoColor=black)
![.ENV](https://img.shields.io/badge/-.ENV-ECD53F?logo=dotenv&logoColor=black)
![Json](https://img.shields.io/badge/-Json-000000?logo=json&logoColor=white)
</div>
<div align="center">

![Math](https://img.shields.io/badge/-Math-000000?logo=math&logoColor=white)
![NetworkX](https://img.shields.io/badge/-NetworkX-FFD43B?logo=networkx&logoColor=black)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-FFD43B?logo=matplotlib&logoColor=black)
![FuzzyWuzzy](https://img.shields.io/badge/-FuzzyWuzzy-FFD43B?logo=fuzzywuzzy&logoColor=black)
![Chardet](https://img.shields.io/badge/-Chardet-FFD43B?logo=chardet&logoColor=black)
![heapq](https://img.shields.io/badge/-heapq-FFD43B?logo=heapq&logoColor=black)
</div>

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

* [Data.Gouv](https://www.data.gouv.fr/fr/)

## Transports list

### RER
Added :
<br>
<span style="white-space:normal">
<span data-sort-value="A !"></span><a href="/wiki/Ligne_A_du_RER_d%27%C3%8Ele-de-France" title="Ligne&nbsp;A du RER d'Île-de-France"><img alt="(A)" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Paris_transit_icons_-_RER_A.svg/18px-Paris_transit_icons_-_RER_A.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Paris_transit_icons_-_RER_A.svg/27px-Paris_transit_icons_-_RER_A.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Paris_transit_icons_-_RER_A.svg/36px-Paris_transit_icons_-_RER_A.svg.png 2x" data-file-width="250" data-file-height="250"></a></span>
<span style="white-space:nowrap"><span data-sort-value="B !"></span><a href="/wiki/Ligne_B_du_RER_d%27%C3%8Ele-de-France" title="Ligne&nbsp;B du RER d'Île-de-France"><img alt="(B)" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Paris_transit_icons_-_RER_B.svg/18px-Paris_transit_icons_-_RER_B.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Paris_transit_icons_-_RER_B.svg/27px-Paris_transit_icons_-_RER_B.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Paris_transit_icons_-_RER_B.svg/36px-Paris_transit_icons_-_RER_B.svg.png 2x" data-file-width="250" data-file-height="250"></a></span>
<span style="white-space:nowrap"><span data-sort-value="C !"></span><a href="/wiki/Ligne_C_du_RER_d%27%C3%8Ele-de-France" title="Ligne&nbsp;C du RER d'Île-de-France"><img alt="(C)" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Paris_transit_icons_-_RER_C.svg/18px-Paris_transit_icons_-_RER_C.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Paris_transit_icons_-_RER_C.svg/27px-Paris_transit_icons_-_RER_C.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Paris_transit_icons_-_RER_C.svg/36px-Paris_transit_icons_-_RER_C.svg.png 2x" data-file-width="250" data-file-height="250"></a></span>
<span style="white-space:nowrap"><span data-sort-value="D !"></span><a href="/wiki/Ligne_D_du_RER_d%27%C3%8Ele-de-France" title="Ligne&nbsp;D du RER d'Île-de-France"><img alt="(D)" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/54/Paris_transit_icons_-_RER_D.svg/18px-Paris_transit_icons_-_RER_D.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/54/Paris_transit_icons_-_RER_D.svg/27px-Paris_transit_icons_-_RER_D.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/54/Paris_transit_icons_-_RER_D.svg/36px-Paris_transit_icons_-_RER_D.svg.png 2x" data-file-width="250" data-file-height="250"></a></span>
<span style="white-space:nowrap"><span data-sort-value="E !"></span><a href="/wiki/Ligne_E_du_RER_d%27%C3%8Ele-de-France" title="Ligne&nbsp;E du RER d'Île-de-France"><img alt="(E)" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Paris_transit_icons_-_RER_E.svg/18px-Paris_transit_icons_-_RER_E.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Paris_transit_icons_-_RER_E.svg/27px-Paris_transit_icons_-_RER_E.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Paris_transit_icons_-_RER_E.svg/36px-Paris_transit_icons_-_RER_E.svg.png 2x" data-file-width="250" data-file-height="250"></a></span>
</span>

### Metros
Added :
<br>
<span style="white-space:normal">
<span data-sort-value="01 !"></span><a href="/wiki/Ligne_1_du_m%C3%A9tro_de_Paris" title="Ligne&nbsp;1 du métro de Paris"><img alt="(1)" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/30/Paris_transit_icons_-_M%C3%A9tro_1.svg/18px-Paris_transit_icons_-_M%C3%A9tro_1.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/30/Paris_transit_icons_-_M%C3%A9tro_1.svg/27px-Paris_transit_icons_-_M%C3%A9tro_1.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/30/Paris_transit_icons_-_M%C3%A9tro_1.svg/36px-Paris_transit_icons_-_M%C3%A9tro_1.svg.png 2x" data-file-width="250" data-file-height="250"></a>
<span data-sort-value="02 !"></span><a href="/wiki/Ligne_2_du_m%C3%A9tro_de_Paris" title="Ligne&nbsp;2 du métro de Paris"><img alt="(2)" src="//upload.wikimedia.org/wikipedia/commons/thumb/d/da/Paris_transit_icons_-_M%C3%A9tro_2.svg/18px-Paris_transit_icons_-_M%C3%A9tro_2.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/da/Paris_transit_icons_-_M%C3%A9tro_2.svg/27px-Paris_transit_icons_-_M%C3%A9tro_2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/d/da/Paris_transit_icons_-_M%C3%A9tro_2.svg/36px-Paris_transit_icons_-_M%C3%A9tro_2.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="03 !"></span><a href="/wiki/Ligne_3_du_m%C3%A9tro_de_Paris" title="Ligne&nbsp;3 du métro de Paris"><img alt="(3)" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/01/Paris_transit_icons_-_M%C3%A9tro_3.svg/18px-Paris_transit_icons_-_M%C3%A9tro_3.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/01/Paris_transit_icons_-_M%C3%A9tro_3.svg/27px-Paris_transit_icons_-_M%C3%A9tro_3.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/01/Paris_transit_icons_-_M%C3%A9tro_3.svg/36px-Paris_transit_icons_-_M%C3%A9tro_3.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="03bis !"></span><a href="/wiki/Ligne_3_bis_du_m%C3%A9tro_de_Paris" title="Ligne&nbsp;3bis du métro de Paris"><img alt="(3bis)" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/49/Paris_transit_icons_-_M%C3%A9tro_3bis.svg/18px-Paris_transit_icons_-_M%C3%A9tro_3bis.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/49/Paris_transit_icons_-_M%C3%A9tro_3bis.svg/27px-Paris_transit_icons_-_M%C3%A9tro_3bis.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/49/Paris_transit_icons_-_M%C3%A9tro_3bis.svg/36px-Paris_transit_icons_-_M%C3%A9tro_3bis.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="04 !"></span><a href="/wiki/Ligne_4_du_m%C3%A9tro_de_Paris" title="Ligne&nbsp;4 du métro de Paris"><img alt="(4)" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/76/Paris_transit_icons_-_M%C3%A9tro_4.svg/18px-Paris_transit_icons_-_M%C3%A9tro_4.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/76/Paris_transit_icons_-_M%C3%A9tro_4.svg/27px-Paris_transit_icons_-_M%C3%A9tro_4.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/76/Paris_transit_icons_-_M%C3%A9tro_4.svg/36px-Paris_transit_icons_-_M%C3%A9tro_4.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="05 !"></span><a href="/wiki/Ligne_5_du_m%C3%A9tro_de_Paris" title="Ligne&nbsp;5 du métro de Paris"><img alt="(5)" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/54/Paris_transit_icons_-_M%C3%A9tro_5.svg/18px-Paris_transit_icons_-_M%C3%A9tro_5.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/54/Paris_transit_icons_-_M%C3%A9tro_5.svg/27px-Paris_transit_icons_-_M%C3%A9tro_5.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/54/Paris_transit_icons_-_M%C3%A9tro_5.svg/36px-Paris_transit_icons_-_M%C3%A9tro_5.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="06 !"></span><a href="/wiki/Ligne_6_du_m%C3%A9tro_de_Paris" title="Ligne&nbsp;6 du métro de Paris"><img alt="(6)" src="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Paris_transit_icons_-_M%C3%A9tro_6.svg/18px-Paris_transit_icons_-_M%C3%A9tro_6.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Paris_transit_icons_-_M%C3%A9tro_6.svg/27px-Paris_transit_icons_-_M%C3%A9tro_6.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Paris_transit_icons_-_M%C3%A9tro_6.svg/36px-Paris_transit_icons_-_M%C3%A9tro_6.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="07 !"></span><a href="/wiki/Ligne_7_du_m%C3%A9tro_de_Paris" title="Ligne&nbsp;7 du métro de Paris"><img alt="(7)" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/21/Paris_transit_icons_-_M%C3%A9tro_7.svg/18px-Paris_transit_icons_-_M%C3%A9tro_7.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/21/Paris_transit_icons_-_M%C3%A9tro_7.svg/27px-Paris_transit_icons_-_M%C3%A9tro_7.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/21/Paris_transit_icons_-_M%C3%A9tro_7.svg/36px-Paris_transit_icons_-_M%C3%A9tro_7.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="07bis !"></span><a href="/wiki/Ligne_7_bis_du_m%C3%A9tro_de_Paris" title="Ligne&nbsp;7bis du métro de Paris"><img alt="(7bis)" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Paris_transit_icons_-_M%C3%A9tro_7bis.svg/18px-Paris_transit_icons_-_M%C3%A9tro_7bis.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Paris_transit_icons_-_M%C3%A9tro_7bis.svg/27px-Paris_transit_icons_-_M%C3%A9tro_7bis.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Paris_transit_icons_-_M%C3%A9tro_7bis.svg/36px-Paris_transit_icons_-_M%C3%A9tro_7bis.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="08 !"></span><a href="/wiki/Ligne_8_du_m%C3%A9tro_de_Paris" title="Ligne&nbsp;8 du métro de Paris"><img alt="(8)" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Paris_transit_icons_-_M%C3%A9tro_8.svg/18px-Paris_transit_icons_-_M%C3%A9tro_8.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Paris_transit_icons_-_M%C3%A9tro_8.svg/27px-Paris_transit_icons_-_M%C3%A9tro_8.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Paris_transit_icons_-_M%C3%A9tro_8.svg/36px-Paris_transit_icons_-_M%C3%A9tro_8.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="09 !"></span><a href="/wiki/Ligne_9_du_m%C3%A9tro_de_Paris" title="Ligne&nbsp;9 du métro de Paris"><img alt="(9)" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/10/Paris_transit_icons_-_M%C3%A9tro_9.svg/18px-Paris_transit_icons_-_M%C3%A9tro_9.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/10/Paris_transit_icons_-_M%C3%A9tro_9.svg/27px-Paris_transit_icons_-_M%C3%A9tro_9.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/10/Paris_transit_icons_-_M%C3%A9tro_9.svg/36px-Paris_transit_icons_-_M%C3%A9tro_9.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="10 !"></span><a href="/wiki/Ligne_10_du_m%C3%A9tro_de_Paris" title="Ligne 10 du métro de Paris"><img alt="(10)" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/24/Paris_transit_icons_-_M%C3%A9tro_10.svg/18px-Paris_transit_icons_-_M%C3%A9tro_10.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/24/Paris_transit_icons_-_M%C3%A9tro_10.svg/27px-Paris_transit_icons_-_M%C3%A9tro_10.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/24/Paris_transit_icons_-_M%C3%A9tro_10.svg/36px-Paris_transit_icons_-_M%C3%A9tro_10.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="11 !"></span><a href="/wiki/Ligne_11_du_m%C3%A9tro_de_Paris" title="Ligne 11 du métro de Paris"><img alt="(11)" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Paris_transit_icons_-_M%C3%A9tro_11.svg/18px-Paris_transit_icons_-_M%C3%A9tro_11.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Paris_transit_icons_-_M%C3%A9tro_11.svg/27px-Paris_transit_icons_-_M%C3%A9tro_11.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Paris_transit_icons_-_M%C3%A9tro_11.svg/36px-Paris_transit_icons_-_M%C3%A9tro_11.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="12 !"></span><a href="/wiki/Ligne_12_du_m%C3%A9tro_de_Paris" title="Ligne 12 du métro de Paris"><img alt="(12)" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Paris_transit_icons_-_M%C3%A9tro_12.svg/18px-Paris_transit_icons_-_M%C3%A9tro_12.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Paris_transit_icons_-_M%C3%A9tro_12.svg/27px-Paris_transit_icons_-_M%C3%A9tro_12.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Paris_transit_icons_-_M%C3%A9tro_12.svg/36px-Paris_transit_icons_-_M%C3%A9tro_12.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="13 !"></span><a href="/wiki/Ligne_13_du_m%C3%A9tro_de_Paris" title="Ligne 13 du métro de Paris"><img alt="(13)" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Paris_transit_icons_-_M%C3%A9tro_13.svg/18px-Paris_transit_icons_-_M%C3%A9tro_13.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Paris_transit_icons_-_M%C3%A9tro_13.svg/27px-Paris_transit_icons_-_M%C3%A9tro_13.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Paris_transit_icons_-_M%C3%A9tro_13.svg/36px-Paris_transit_icons_-_M%C3%A9tro_13.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="14 !"></span><a href="/wiki/Ligne_14_du_m%C3%A9tro_de_Paris" title="Ligne 14 du métro de Paris"><img alt="(14)" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Paris_transit_icons_-_M%C3%A9tro_14.svg/18px-Paris_transit_icons_-_M%C3%A9tro_14.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Paris_transit_icons_-_M%C3%A9tro_14.svg/27px-Paris_transit_icons_-_M%C3%A9tro_14.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Paris_transit_icons_-_M%C3%A9tro_14.svg/36px-Paris_transit_icons_-_M%C3%A9tro_14.svg.png 2x" data-file-width="250" data-file-height="250"></a>
<span data-sort-value="15 !"></span><a href="/wiki/Ligne_15_du_m%C3%A9tro_de_Paris" title="Ligne 15 du métro de Paris"><img alt="(15)" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/55/Paris_transit_icons_-_M%C3%A9tro_15.svg/18px-Paris_transit_icons_-_M%C3%A9tro_15.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/55/Paris_transit_icons_-_M%C3%A9tro_15.svg/27px-Paris_transit_icons_-_M%C3%A9tro_15.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/55/Paris_transit_icons_-_M%C3%A9tro_15.svg/36px-Paris_transit_icons_-_M%C3%A9tro_15.svg.png 2x" data-file-width="250" data-file-height="250"></a>
</span>

to add :
<br>
<span style="white-space:normal">
<span data-sort-value="16 !"></span><a href="/wiki/Ligne_16_du_m%C3%A9tro_de_Paris" title="Ligne 16 du métro de Paris"><img alt="(16)" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/46/Paris_transit_icons_-_M%C3%A9tro_16.svg/18px-Paris_transit_icons_-_M%C3%A9tro_16.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/46/Paris_transit_icons_-_M%C3%A9tro_16.svg/27px-Paris_transit_icons_-_M%C3%A9tro_16.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/46/Paris_transit_icons_-_M%C3%A9tro_16.svg/36px-Paris_transit_icons_-_M%C3%A9tro_16.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="17 !"></span><a href="/wiki/Ligne_17_du_m%C3%A9tro_de_Paris" title="Ligne 17 du métro de Paris"><img alt="(17)" src="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Paris_transit_icons_-_M%C3%A9tro_17.svg/18px-Paris_transit_icons_-_M%C3%A9tro_17.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Paris_transit_icons_-_M%C3%A9tro_17.svg/27px-Paris_transit_icons_-_M%C3%A9tro_17.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Paris_transit_icons_-_M%C3%A9tro_17.svg/36px-Paris_transit_icons_-_M%C3%A9tro_17.svg.png 2x" data-file-width="250" data-file-height="250"></a> 
<span data-sort-value="18 !"></span><a href="/wiki/Ligne_18_du_m%C3%A9tro_de_Paris" title="Ligne 18 du métro de Paris"><img alt="(18)" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Paris_transit_icons_-_M%C3%A9tro_18.svg/18px-Paris_transit_icons_-_M%C3%A9tro_18.svg.png" decoding="async" width="18" height="18" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Paris_transit_icons_-_M%C3%A9tro_18.svg/27px-Paris_transit_icons_-_M%C3%A9tro_18.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Paris_transit_icons_-_M%C3%A9tro_18.svg/36px-Paris_transit_icons_-_M%C3%A9tro_18.svg.png 2x" data-file-width="250" data-file-height="250"></a>
</span>

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
git clone https://github.com/hugo-HDSF/PUBLIC_transports_paris_idf.git
```

3. Create a virtual environment (optional). we recommend using poycharms built in virtual environment.

4. Install the required packages. (all packages are listed in the main.py file)

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

```walking_to_nearest_station_reward = 20```

Set the weight of the nodes:

```node_weight = 5```

Set the weight of the edges:

```edge_weight = 50```

## Roadmap

See the [open issues](https://github.com/hugo-HDSF/transports_paris_idf/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/hugo-HDSF/transports_paris_idf/issues/new) to discuss it, or directly create a pull request
  after you edit the [*README.md*](README.md) file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.

## License

Distributed under the MIT License.

## Authors

* **DA SILVA Hugo** - *Student - fullstack developer* - [Github](https://github.com/hugo-HDSF/)
* **MOHAMMEDI Tayeb** - *Student - fullstack developer* - Github

## Acknowledgements

* [Paris Nanterre University](https://www.parisnanterre.fr/)
* [Img Shields](https://shields.io/)
* [Simple Icons](https://simpleicons.org/)
* [Readme Generator](https://readme.shaankhan.dev/)
