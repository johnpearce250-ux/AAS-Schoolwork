# Media Catalogue

Simple Python module that defines media classes and a catalogue:

- `MediaError` — custom exception for media-related errors
- `Movie` — represents a movie (title, year, director, duration)
- `TVSeries` — subclass of `Movie` with `seasons` and `total_episodes`
- `MediaCatalogue` — stores media items and provides a string summary

Usage
-----
Save the file and run the module directly:

```bash
python Media_catalog.py
```

Example
-------
```python
from Media_catalog import Movie, TVSeries, MediaCatalogue

catalogue = MediaCatalogue()
catalogue.add(Movie("The Matrix", 1999, "The Wachowskis", 136))
catalogue.add(Movie("Annie Hall", 1977, "Woody Allen", 93))
catalogue.add(TVSeries("Stranger Things", 2016, "The Duffer Brothers", 51, 4, 34))

print(catalogue)
```

Expected output (approximately):

```
Media Catalogue (3 items):

=== MOVIES ===
1. The Matrix (1999) - 136 min, The Wachowskis
2. Annie Hall (1977) - 93 min, Woody Allen

# TV series (if implemented in output)
```

Exceptions
----------
- `ValueError` is raised by `Movie`/`TVSeries` constructors for invalid fields (empty title, year < 1895, non-positive duration, etc.).
- `MediaError` is raised by `MediaCatalogue.add` when attempting to add a non-`Movie`/`TVSeries` object.

Notes
-----
- The `Media_catalog.py` script includes a small demo guarded by `try/except` that prints validation or media errors to the console.
