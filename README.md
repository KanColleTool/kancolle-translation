kancolle-translation
====================

This repository attempts to create a community-driven, complete translation of KanColle's in-game text. It's mainly used by KanColleTool, but may be used by other tools as well.

Reporting untranslated lines
----------------------------

### Manually

If you're using KanColleTool, see below for how it auto-generates this data.  
If you're using something else, or if you're interested in interfacing with this database yourself, read on.

The translation database is a JSON array of objects in the following format:

```json
[
    {
        "ctx": "api_name",
        "orig": "母港",
        "src": "/kcsapi/api_start2"
    }
]
```

The keys are as follows:

* __ctx__ - The closest enclosing key
* __orig__ - Original Japanese line
* __src__ - Source URL it was found at, minus domain

Ensure that there is an entry for the line you found, go to this repo's [Issues page](https://github.com/KanColleTool/kancolle-translation/issues), and open a new issue.

The body __must include all this information__, not just the untranslated line - we need the `ctx` and `src` keys as well. For readability, we ask that you add the data in a fenced code block, like this:

    ```json
    [
        {
            "ctx": "api_name",
            "orig": "母港",
            "src": "/kcsapi/api_start2"
        }
    ]
    ```

Issues missing ctx and src information __will be closed immediately__. We need this information!

### Using KanColleTool

In your caches directory, there will be a file called `untranslated.json`. The exact location of this file varies depending on your OS:

OS      | Location
------- | ------------------------------
Windows | %APPDATA%/KanColleTool/cache
Mac     | ~/Library/Caches/KanColleTool
Linux   | ~/.cache/KanColleTool

Using the fenced code block syntax above, copypaste the contents of this file into a new [Issue](https://github.com/KanColleTool/kancolle-translation/issues).

Translation workflow
--------------------

If you have a translation to contribute, please do!

Note that if the line is untranslated, it will almost certainly be accepted (assuming it doesn't contain glaring grammatical errors), but if you're correcting someone else's translation, please provide a short explanation for why your version is more suitable.

### Using tltool

`tltool.py` is a tool for working with the translation database. It requires Python 2.7+, but doesn't rely on any outside libraries.

The basic workflow for using tltool is as follows:

* `./tltool missing en patch.json`  
  Exports all lines missing an `en` (English) translation to the file `patch.json`.
* __Edit untranslated lines__
  Simply open up `patch.json` (or whatever you called it), and fill in the `en` key for the lines you'd like to contribute. If you don't know a good translation, leave it blank.
* `./tltool merge en patch.json`
  Merges your changes back into the main database.

### Manually

If you don't have Python installed, or you prefer to work with the database manually, you may edit `translation.json` yourself to add language keys to lines of your choice.

This method may be faster, but makes it harder to get an overview of lines in need of translation, and will not provide automatic syntax checking right away.

Submitting a patch
------------------

To submit your finished patch, you have two choices.

### Send a pull request
If you're comfortable working with Git**, you may [fork the repository](https://help.github.com/articles/fork-a-repo/) and send a pull request with your changes.

Your pull request will be validated by Travis-CI, so you will get an error if you try to submit a broken database.

### Open an issue
If not, you may instead [open an issue](https://github.com/KanColleTool/kancolle-translation/issues) including your patch.

Please use fenced code blocks (see "Reporting untranslated lines" -> "Manual" for an example), and omit all entries you haven't provided a translation for to reduce its size.

An example:

    ```json
    [
        {
            "ctx": "api_name",
            "en": "Submarine Warfare",
            "orig": "海上護衛戦",
            "src": "/kcsapi/api_start2"
        }
    ]
    ```
