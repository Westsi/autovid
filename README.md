<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Westsi/autovid">
    <img src="readme_images/Autovid-logos.jpeg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">AutoVid</h3>

  <p align="center">
    A bot that takes script inputs and makes Discord videos!
    <br />
    <a href="https://github.com/Westsi/autovid"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Westsi/autovid">View Demo</a>
    ·
    <a href="https://github.com/Westsi/autovid/issues">Report Bug</a>
    ·
    <a href="https://github.com/Westsi/autovid/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src="readme_images/Autovid-logos_black.png" alt="Logo" height=150>
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Movie.py][Movie.py]][Movie-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* [python 3](https://www.python.org/downloads/)
* [ffmpeg](https://ffmpeg.org/download.html)
* install packages from `requirements.txt`
  ```sh
  pip install -r requirements.txt
  ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/Westsi/autovid.git
   ```
2. Enable the Youtube Data API at [Google Cloud Console](https://console.cloud.google.com/)

3. Make an OAuth Consent screen with sensitive scope `./auth/youtube`.

4. Create OAuth client ID credentials and paste them in a new file `client_secrets.json`. Don't worry, the `.gitignore` file will stop it from being uploaded.
    ```json
    {
    "web": {
        "client_id": "CLIENT-ID-HERE",
        "client_secret": "CLIENT-SECRET-HERE",
        "redirect_uris": [],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token"
        }
    }
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The `template_script.txt` and `template_script_metadata.json` files are templates for scripts. You can make your own, but if they are named differently then you will need to change the names of the files accessed in `main.py` lines `52` and `53`.

```python
script = load_script("YOUR-SCRIPT.txt")
script_json = load_script_json("YOUR-SCRIPT-METADATA.json")
```

Right now, there is only one sound type - `boom`. Notification sounds wil automatically play on a new message. There are 6 profile pictures in `/pfp` but you can add your own. The default folder for profile pictures is `/pfp`. The `links` section in `template_script_metadata.json` only needs to be filled out for those messages that should be links. All others will default to being `false`. Remember that JSON `true` and `false` are lowercase, while Python's are uppercase.
<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Other Video Types
- [ ] Custom Errors
- [ ] Other Sounds

See the [open issues](https://github.com/Westsi/autovid/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - westsi@protonmail.com

Project Link: [https://github.com/Westsi/autovid](https://github.com/Westsi/autovid)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Westsi](https://westsi.pages.dev)
* [yokharian for Discord Message Generation Code](https://github.com/yokharian/ImageDis)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Westsi/autovid.svg?style=for-the-badge
[contributors-url]: https://github.com/Westsi/autovid/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Westsi/autovid.svg?style=for-the-badge
[forks-url]: https://github.com/Westsi/autovid/network/members
[stars-shield]: https://img.shields.io/github/stars/Westsi/autovid.svg?style=for-the-badge
[stars-url]: https://github.com/Westsi/autovid/stargazers
[issues-shield]: https://img.shields.io/github/issues/Westsi/autovid.svg?style=for-the-badge
[issues-url]: https://github.com/Westsi/autovid/issues
[license-shield]: https://img.shields.io/github/license/Westsi/autovid.svg?style=for-the-badge
[license-url]: https://github.com/Westsi/autovid/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png


[Python]: https://img.shields.io/badge/Python-yellow?style=for-the-badge&logo=python
[Python-url]: https://www.python.org/
[Movie.py]: https://img.shields.io/badge/movie.py-red?style=for-the-badge&logo=python&logoColor=white
[Movie-url]: https://zulko.github.io/moviepy/
