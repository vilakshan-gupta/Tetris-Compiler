build:
	bison -d -r all a2version2.y ; flex extetrickscanner.l ;  gcc extetrickstype.c lex.yy.c a2version2.tab.c -o x2021A7PS2058G

test:
	./x2021A7PS2058G < testinput.tetris 2>/dev/null > output.py
