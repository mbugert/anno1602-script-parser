# Grammar and Parser Generator for Anno 1602 Scripts
This repo contains:
* a [grammar](parser/io/script/grammar.lark) that accepts all COD and GAD files in Anno 1602 KE (Königs-Edition)
* a feature-complete [interpreter](parser/io/script/interpreter.py) for `HAEUSER.COD`, `FIGUREN.COD` that spits out plain python objects

Parser generation uses the [lark parsing toolkit](https://github.com/lark-parser/lark).
The resulting parser is LALR, despite the chaotic script language. Parsing is still relatively slow (4 seconds for all of the game's files, see below), but at least the code is maintainable.

For more details on the script language format, see https://github.com/Green-Sky/anno16_docs/blob/master/file_formats/script.md

## Usage
Needs python>=3.9.
```bash
git clone https://github.com/mbugert/anno1602-script-parser
cd anno1602-script-parser
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# in line 7, enter the root directory of your 1602 KE install
nano parser/test/base.py

# interpret all HAEUSER.COD, FIGUREN.COD, parse all GAD/INC files
python -m unittest discover parser/test
```

Sample output:
```commandline
❯ python -m unittest discover parser/test

figuren.cod:

{'FIGUR': {0: {'Gfx': 0,
               'Id': 0,
               'Kind': <CharacterType.UNUSED: 1>,
               'Speedtyp': 0,
               'Stirbtime': 2.5},
           <Character.SOLDAT1: 2>: {'ANIM': {0: {'AnimAdd': 1,
                                                 'AnimAnz': 8,
                                                 'AnimOffs': 0,
                                                 'AnimSpeed': 80,
                                                 'Kind': <AnimationType.ENDLESS: ...
.
haeuser.cod:

{'BAUINFRA': {<InfrastructureLevel.INFRA_SCHULE: 4>: {'BGruppe': 1,
                                                      'Minwohn': 100},
              <InfrastructureLevel.INFRA_WIRT: 5>: {'BGruppe': 1,
                                                    'Minwohn': 50},
              <InfrastructureLevel.INFRA_KIRCHE: 6>: {'BGruppe': 2,
                                                      'Minwohn': 150},
              <InfrastructureLevel.INFRA_BADE: 7>: {'BGruppe': 2,
                      ...
..
----------------------------------------------------------------------
Ran 3 tests in 4.064s

OK

```

## Todos for the future

- [ ] implement `include_ref` in [interpreter.py](parser/io/script/interpreter.py) to support interpreting most GAD files
- [ ] implement `property_index_ref` in [interpreter.py](parser/io/script/interpreter.py) to support `CTRL.GAD`

## License
MIT license
