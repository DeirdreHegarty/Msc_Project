#!/bin/bash

pandoc --standalone \
--pdf-engine=xelatex \
	--template MaynoothUniversity.tex \
       	--bibliography bibliography.bib \
	--csl ieee.csl \
	-o /tmp/thesis.pdf \
	thesis_draft_1.md \
	&& open /tmp/thesis.pdf
