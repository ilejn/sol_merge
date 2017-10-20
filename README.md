### PURPOSE

Solidity (Ethereum programming language) has source file _import_ concept (like e.g. Python)
This is convenient while sometimes it is needed to have dependencies all together,
as a single file.

This is the problem sol_merge.py addresses.


### USAGE

sol_merge.py solves very simple problem (see LIMITATIONS) and it is very simple itself.
Developing took an hour of work or so.

The only command line parameter - source  filename which is a starting point.
Result is put to stdout.


```
python sol_merge.py --source Contract.sol
```

python2 and python3 are fine

### LIMITATIONS

Constructs
```
import * as symbolName from "filename";
```
or
```
import {symbol1 as alias, symbol2} from "filename";
```
are not supported (work as regular import ignoring rename part)
