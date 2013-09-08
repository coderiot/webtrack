webtrack
========

Keep track of changes to any website.

## Requirements
 - lxml
 - cssselect

## Installation
```sh
$ pip install -e git+https://github.com/peterrr/webtrack.git#egg=webtrack
```

## Usage
Get newest article on hackernews:
```
$ webtrack http://news.ycombinator.com/newest ".title a"
```

Only get the 10 newest article on hackernews:
```
$ webtrack http://news.ycombinator.com/newest ".title a" -l 10
```
