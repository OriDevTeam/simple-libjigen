# simple-libjigen

A partial implementation of `libjigen-rust` only for data format handling

If you just want to read/write, visualize and convert data formats,
this is the convenience tool


## Usage
To check which commands are available type:
> python main.py --help

## Converting
Converting from a format to another is simple, for example converting a **map**
from Legacy format to JSON
> python main.py --from-format=legacy --convert --target=json --out='result-directory/' map --source='map-directory'

Or converting a unified racedata file from Legacy to JSON
> python main.py --from-format=legacy --convert --target=json --out='result-directory/' script racedata 'racedata-path' --parted=False

### Formats
| Format       | Legacy | JSON | XML | CSV |
|--------------|--------|------|-----|-----|
| Map          | ✔️     | ⚠️   | ❌   | ❌   |
| Item Proto   | ❌      | ❌    | ⚠️  | ⚠️  |
| Mob Proto    | ❌      | ❌    | ⚠️  | ⚠️  |
| Script Files | ⚠️     | ⚠️   | ❌   | ❌   |

**Note**: ⚠️ means that implementation is in progress️

You can type the 'help' command to see the available format groups
> python main.py --help

## Warning Notes
**Optimization**: simple-libjigen is not optimized for performance (parsing/converting lacking optimization),
if you require speed check the low level equivalent `libjigen-rust`

**Exceptions**: There are not many checks for exceptions when parsing,
the library expects that the given data obeys the involved formats
