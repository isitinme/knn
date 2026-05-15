# knn

A small Python module that implements a basic k-nearest neighbors search over a fixed set of user preferences.

The module defines a `KNN` class with:
- Euclidean distance calculation between users
- Adding new users and their coordinate vectors
- Finding the `k` closest neighbors for a given user

## Requirements

- Python 3
- `numpy`

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Run

Use the script with two command-line arguments: a username and the number of neighbors `k`.

```bash
python knn.py Priyanka 2
```

Example output:

```text
Closest 2 neighbors of the user Priyanka are: [('Alina', 2.828), ('Morpheus', 4.472)]
```

## Notes

- The current dataset is defined in `knn.py` as `user_preferences`.
- The script expects an existing username from that dataset.
- The output is a list of the nearest users and their Euclidean distances.
