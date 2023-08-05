# The Ripe Tomato 🍅
[![Build Passing](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/NonvegPanda/Tomato-Sorter-EB/actions)
[![Docker Pulls](https://img.shields.io/docker/pulls/aaxyat/tomatosorter)](https://hub.docker.com/r/aaxyat/tomatosorter)
[![GitHub Stars](https://img.shields.io/github/stars/NonvegPanda/Tomato-Sorter-EB?style=social)](https://github.com/NonvegPanda/Tomato-Sorter-EB/stargazers)


This is a machine learning based web application that helps to predict whether a tomato is ripe or unripe. It utilizes a model trained on Keras and provides an easy-to-use interface for uploading a tomato image and receiving the prediction.

![Screenshot](./screenshot.png)

## Table of Contents
1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Contributors](#contributors)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

Ensure that you have the following installed on your local machine:

- Python 3.7+
- Flask
- Tensorflow 2.x
- Keras

## Installation 
### Running with Docker

```bash
# Pull the Docker image:
docker pull aaxyat/tomatosorter

# Run the application using Docker:
docker run -d -p 5000:5000 aaxyat/tomatosorter
```
After running the above command, visit http://localhost:5000 in your web browser.

### Direct Installation 
Clone the repo:

```bash
git clone https://github.com/NonvegPanda/TheRipeTomato.git
cd TheRipeTomato
```

Create a new Python virtual environment:

```bash
python -m venv env
```

Activate the virtual environment:

On Windows:

```bash
.\env\Scripts\activate
```

On MacOS/Linux:

```bash
source env/bin/activate
```

Next, install the dependencies:

```bash
pip install -r requirements.txt
```

Before running the project, please ensure that long paths are enabled on Windows. To enable long paths, follow the steps below:

1. Open the Local Group Policy Editor (press Win + R, type `gpedit.msc` and hit Enter).
2. Navigate to: Computer Configuration > Administrative Templates > System > Filesystem > NTFS.
3. Double click the Enable NTFS long paths option and enable it.

If the Local Group Policy Editor is not available in your version of Windows, try this method:

1. Open the Registry Editor (press Win + R, type `regedit` and hit Enter).
2. Navigate to: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`
3. Right-click the value `LongPathsEnabled` and select Modify.
4. Change Value data to `1` and click OK.

Start the Flask development server:

```bash
python app.py
```

Navigate to [http://localhost:5000](http://localhost:5000) in your browser.

## Contributors

- [Yubhaskar Baral](https://github.com/NonvegPanda)
- [Ayush Bhattarai](https://github.com/Aaxyat)

Your contributions are always welcome! Feel free to improve existing code, documentation or implement new features. Please open an issue to propose your changes if they are substantial. 😃

---

Made with ♥ by Yubhaskar Baral and Ayush Bhattarai
