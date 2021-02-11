# -*- coding: utf-8 -*-
from glr import GLRParser

def parse_dict(g_fname):
    file = open(g_fname, 'rb')
    onstring = file.read().split("\n")
    dictionaries = dict()
    for item in onstring:
        item = item.decode('utf-8')
        key = item.split(" ")[0]
        value = item.split(" ")[1:]
        dictionaries[key] = value
    file.close()
    return dictionaries
def parse_gram(gram_fname):
    grammar = u"\n "

    file = open(gram_fname, 'rb')
    onstring = file.read().split("\n")

    for item in onstring:
        grammar += ' ' + item+ '\n '
    grammar = grammar.replace("  \n","")
    file.close()
    return grammar

def res(text, g_fname, gram_fname):
    glr = GLRParser(parse_gram(gram_fname), dictionaries=parse_dict(g_fname), debug=False)
    return glr

if __name__ == "__main__":
    lib_fname = 'my_dictionaries.txt'
    g_fname = 'my_grammar.txt'
    #text = u"на вешалке висят пять зеленых курток. и вонючая шляпа. и красных пальто веселый слон"
    text = u"Биотехнология – это использование микроорганизмов, биологических систем или биологических процессов в промышленном производстве. В настоящее время при помощи бактерий получают целый ряд веществ: инсулин, гормон роста и др. Человеческий ген встроенный в геном бактерии обеспечивает синтез гормона."
    glr = res(text, g_fname, lib_fname)
    for parsed in glr.parse(text):
        print "FOUND:", parsed