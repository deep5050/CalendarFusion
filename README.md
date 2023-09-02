<p align=center>
  <p align=center>
  <img align=center src=https://github.com/deep5050/random-shits-happen-here/assets/27947066/e517f3c6-90e5-4ad7-a919-2723f54ba54e width=250px >
</p>
  <h3 align="center">Calendar Fusion</h3>
  <p align="center">
    A Python module to generate fancy markdown table-based calendar
  <br/>

<br />
  <a href="https://github.com/deep5050/CalendarFusion/graphs/contributors">
  <img src="https://img.shields.io/github/contributors/deep5050/CalendarFusion.svg?style=flat-square">
  </a>
  <a href="https://github.com/deep5050/CalendarFusion/network/members">
  <img src="https://img.shields.io/github/forks/deep5050/CalendarFusion.svg?style=flat-square">
  </a>
  <a href="https://github.com/deep5050/CalendarFusion/stargazers">
  <img src="https://img.shields.io/github/stars/deep5050/CalendarFusion.svg?style=flat-square">
  </a>
  <a href="https://github.com/deep5050/CalendarFusion/issues">
  <img src="https://img.shields.io/github/issues/deep5050/CalendarFusion.svg?style=flat-square">
  </a>
  <a href="https://github.com/deep5050/CalendarFusion/blob/master/LICENSE.txt">
  <img src="https://img.shields.io/github/license/deep5050/CalendarFusion.svg?style=flat-square">
  </a> 
  <a href="https://linkedin.com/in/othneildrew">
  <img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555">
  </a>
        <br/><a href="https://github.com/deep5050/CalendarFusion"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/deep5050/CalendarFusion/issues">Report Bug</a>
    ·
    <a href="https://github.com/deep5050/CalendarFusion/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Installation](#installation)
* [Usage](#usage)
* [Version History](#version-history)
* [Contributing](#contributing)
* [Support](#support)
* [License](#license)
* [Contact](#contact)
* [Related Works](#related-works)


<!-- ABOUT THE PROJECT -->
## About The Project

Display a Calendar as you like. Add links, styles, emojis, etc. 


## Installation

`pip3 install CalendarFusion`



## Documentation

See the [Docs](docs/CalendarFusion.md) here ⬅️ 

<!-- USAGE EXAMPLES -->
## Example usages

### initialize

```python
from CalendarFusion import CalendarFusion
cf = CalendarFusion.CalendarFusion()
```

|Mon|Tue|Wed|Thu|Fri|Sat|Sun|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
||1|2|3|4|5|6|
|7|8|9|10|11|12|13|
|14|15|16|17|18|19|20|
|21|22|23|24|25|26|27|
|28|29|30|31||||


```python
cf = CalendarFusion(year=2023,
                    month=2,
                    fill_calendar=True,
                    weekno=True,
                    start_from_sunday=False,
                    lang="ja"
                    )
print(cf.table())
```
|週|月|火|水|木|金|土|日|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|5|30|31|1|2|3|4|5|
|6|6|7|8|9|10|11|12|
|7|13|14|15|16|17|18|19|
|8|20|21|22|23|24|25|26|
|9|27|28|1|2|3|4|5|



### `link()`

Add a link to the dates.

```python
entity = {}
entity[date(2023,8,12)] = "https://google.com"
entity[date(2023,8,2)] = "https://bing.com"
entity[date(2023,8,25)] = "https://google.com"
entity[date(2023,8,10)] = "https://google.com"
cf.link(urls=entity)
```

|Mon|Tue|Wed|Thu|Fri|Sat|Sun|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
||1|[2](https://bing.com)|3|4|5|6|
|7|8|9|[10](https://google.com)|11|[12](https://google.com)|13|
|14|15|16|17|18|19|20|
|21|22|23|24|[25](https://google.com)|26|27|
|28|29|30|31||||


### `style()`

Add formatting styles to the dates.

```python
selected_dates = [date(2023,8,23),
                  date(2023,8,1),
                  date(2023,8,27),
                  date(2023,7,31),
                  date(2023,8,20),
                  date(2023,8,7)
                  ]
                  
print(cf.style(style="quote",selected=selected_dates))
```
|Mon|Tue|Wed|Thu|Fri|Sat|Sun|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
||`1`|2|3|4|5|6|
|`7`|8|9|10|11|12|13|
|14|15|16|17|18|19|`20`|
|21|22|`23`|24|25|26|`27`|
|28|29|30|31||||

### `selective()`

Selective formatting

```python
selected_dates = [date(2023,8,23),
                  date(2023,8,1),
                  date(2023,8,27),
                  date(2023,7,31),
                  date(2023,8,20),
                  date(2023,8,7)
                  ]
print(cf.selective(selected=selected_dates,not_selected_date_text="."))
```
|Sun|Mon|Tue|Wed|Thu|Fri|Sat|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|.|31|1|.|.|.|.|
|.|7|.|.|.|.|.|
|.|.|.|.|.|.|.|
|20|.|.|23|.|.|.|
|27|.|.|.|.|.|.|

```python
print(cf.selective(selected=selected_dates,
             not_selected_date_text=":red_circle:",
             selected_date_text=":green_circle:"
             ))
```
|Sun|Mon|Tue|Wed|Thu|Fri|Sat|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|:red_circle:|:green_circle:|:green_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|
|:red_circle:|:green_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|
|:red_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|
|:green_circle:|:red_circle:|:red_circle:|:green_circle:|:red_circle:|:red_circle:|:red_circle:|
|:green_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|:red_circle:|



## Version History

`v1.0.0` Initial release


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch 
3. Commit your Changes 
4. Push to the Branch 
5. Open a Pull Request


## Support

All Kinds Of Supports Are Welcome :raised_hands:! The Most Basic Way To Show Your Support Is To Star :star2: The Project, Or To Raise Issues :speech_balloon: You Can Also Support This Project By [**becoming a sponsor on GitHub**](https://github.com/sponsors/deep5050) :clap: Or By Making A [**Paypal**](https://paypal.me/deep5050) Donation :)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Dipankar Pal - dipankarpal5050@gmail.com



## Related Works

[Radioactive](https://github.com/deep5050/radio-active) : A CLI-based internet radio player

[NaughtyLust](https://github.com/deep5050/NaughtyLust) : Awesome Nautilus Scripts For Linux.

[qikQR](https://github.com/deep5050/qikQR) : Minimal QR Code Generator App Made With Electron.

[cppcheck-action](https://github.com/deep5050/cppcheck-action) : Check Security Flaws In Your C/C++ Codes Right From GitHub Action Workflows.

[autopy-lot](https://github.com/deep5050/autopy-lot) : GitHub Action Setup To Convert Jupyter Notebooks To Python Scripts And Markdowns.

<div align=center>
<p align=center><img align=center src="https://raw.githubusercontent.com/liyasthomas/templates/master/assets/logo.gif" alt="unicorn" width="400">
</p>
<p align=center>Happy Coding</p>
  
<p align=center><img align=center  src="https://visitor-badge.laobi.icu/badge?page_id=deep5050.CalendarFusion" alt="Visitors">  </p>

</div>
