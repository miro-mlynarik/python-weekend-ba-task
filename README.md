# Python weekend entry task

### Solution description
CLI usage: python solution.py [-h] [--bags BAGS] [--roundtrip] [--stops STOPS] [--stay STAY] csvfile origin destination

positional arguments:
| Argument name | type    | Description                  | Example                      |
|---------------|---------|------------------------------|------------------------------|
| `csvfile`     | string  | Flights dataset in csv format| example/example3.csv         |
| `origin`      | string  | Origin airport code          | WUE                          |
| `destination` | string  | Destination airport code     | JBN                          |

optional arguments:
| Argument name | type    | Description                    | Example                      |
|---------------|---------|--------------------------------|------------------------------|
| `--bags`      | int     | Number of bags                 | --bags=2                     |
| `--roundtrip` | string  | Return trip flag               | --roundtrip                  |
| `--stops`     | int     | Maximum number of stops        | --stops=3                    |
| `--stay`      | int     | Number of nights in destination| --stay=5                     |

 

