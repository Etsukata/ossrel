OSSrel
======

OSS relationship visualization

![alt tag](https://raw.github.com/Etsukata/ossrel/master/img/sample.png)

OVERVIEW
--------

This software visualizes OSS project relationship by counting up the number of
common developer's commits. The relationship is visualized with Chord Diagram.
Each path in chord diagram shows the relevance of OSS projects of endpoint
nodes.


DEMO
----

Interactive WEB page example is available at [HERE](http://etsukata.com/ossrel/).


Visualize relationship between projects you choose
--------------------------------------------------

clone ossrel and 'ln -s' to git repositories you choose to ./repos:

    # git clone https://github.com/Etsukata/ossrel.git
    # cd ossrel
    # mkdir repos
    # ln -s /path/to/git/repoA ./repos/repoA
    # ln -s /path/to/git/repoB ./repos/repoB
    # ln -s /path/to/git/repoC ./repos/repoC

then run scrpt:

    # ./run.sh
    # firefox index.html

THANKS TO
---------

ossrel uses mbosock's [Chord Diagram](http://bl.ocks.org/mbostock/4062006)
d3js example to visualization.
