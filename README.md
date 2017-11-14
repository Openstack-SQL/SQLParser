# SQLParser
Module for parsing SQL

## Architecture 

```
.
├── data  // data for testing
│   ├── requests.txt
│   ├── requests_without_LR.txt
│   └── someR.txt
├── __init__.py
├── LICENSE
├── Main.py
├── Metrics.py  // The listener which collect the metrics 
├── parser      // The antlr4 parser
│   ├── __init__.py
│   ├── Sql.g4  // The grammar file used by antlr4
│   ├── SqlLexer.py 
│   ├── SqlLexer.tokens
│   ├── SqlListener.py
│   ├── SqlParser.py
│   └── Sql.tokens
├── README.md
├── SqlReportProcessor.py // A class processing the sql request to generate the report
├── SqlReport.py // The object containing the metrics
└── Test_Grammar.py
```

## Generating the parser
To generate the parser you will need antlr4 and the antlr4 python runtime

Please see http://www.antlr.org/download.html

the python runtime is also needed to run the project

## Collecting the metrics

*SqlReportProcessor.py* can generate an SqlReport object which contains metrics
extracted from sql requests. The requests to be analysed are simple String.

*Metrics.py* is a listener which is activated during the parsing of the sql requests.

## Improving the listener

The listener methods are writen in *Metrics.py*

Antlr4 offers two types of methods for listener :
    
    - enterTOKEN 
    - exitTOKEN

For a given token, the first one is activated when we start to parse the token and
the second one is activated when the token parsing is done.

TOKEN correspond to the rules specified in the grammar file *Sql.g4*