# !/usr/bin/python
# reads data.xml and prints depends
# by Eugene Mikhailov
# this is free software :)

import xml.dom.minidom
import string
import sys
from xml.dom.minidom import Node
if len(sys.argv) <= 2:
    print("Insufficient agumetns")
    sys.exit(2)

try:
    doc = xml.dom.minidom.parse(sys.argv[1])
except xml.parsers.expat.ExpatError as err:
    print('Error:', err)
    sys.exit(2)

def get_deps():
    # global doc
    depstring = ""
    try:
        for node in doc.getElementsByTagName("dep"):
            skip = False
            for depp in node.childNodes:
                for detail in depp.childNodes:
                    if detail.parentNode.nodeName == "name":
                        tmp_name = string.strip(detail.nodeValue)
                        if tmp_name.startswith("aaa"):
                            skip = True
                        else:
                            depstring += tmp_name
                    if not skip and detail.parentNode.nodeName == "condition":
                        nv = string.strip(detail.nodeValue)
                        if nv == "more":
                            depstring += ">"
                        elif nv == "less":
                            depstring += "<"
                        elif nv == "notequal":
                            depstring += "!="
                        elif nv == "equal":
                            depstring += "=="
                        elif nv == "atleast":
                            depstring += ">="
                        elif nv == "notmore":
                            depstring += "<="
                    if not skip and detail.parentNode.nodeName == "version":
                        if not detail.nodeValue:
                            depstring += " "
                        else:
                            depstring += string.strip(detail.nodeValue)+" "
        print(string.strip(depstring))
    except Exception as e:
        print("Oh shi~... No data.xml or it is very ugly.", e)
        sys.exit(2)


def get_package_attrs():
    # global doc
    pkgname = pkgver = pkgbuild = pkgarch = ""
    try:
        node = doc.firstChild
        for p in node.childNodes:
            for ptag in p.childNodes:
                if ptag.parentNode.nodeName == "name":
                    pkgname = ptag.nodeValue.strip()
                elif ptag.parentNode.nodeName == "version":
                    pkgver = ptag.nodeValue.strip()
                elif ptag.parentNode.nodeName == "arch":
                    pkgarch = ptag.nodeValue.strip()
                elif ptag.parentNode.nodeName == "build":
                    pkgbuild = ptag.nodeValue.strip()
        print(pkgname+" "+pkgver+" "+pkgarch+" "+pkgbuild)
    except Exception as e:
        print("Oh shi~... No data.xml or it is very ugly.", e)
        sys.exit(2)

def get_maintainer():
    # global doc
    try:
        if not doc.getElementsByTagName("maintainer"):
            raise Exception("Can't find maintainer")
        for node in doc.getElementsByTagName("maintainer"):
            for mtag in node.childNodes:
                for me in mtag.childNodes:
                    if me.parentNode.nodeName == "name":
                        print("Name: "+me.nodeValue.strip())
                    else:
                        raise Exception("Can't find name")
                    if me.parentNode.nodeName == "email":
                        print("Email: "+me.nodeValue.strip())
                    else:
                        raise Exception("Can't find email")
    except Exception as e:
        print("Oh shi~...", e)
        sys.exit(2)

def get_tags():
    taglist = ""
    # global doc
    try:
        for node in doc.getElementsByTagName("tags"):
            for tags in node.childNodes:
                for tag in tags.childNodes:
                    if tag.parentNode.nodeName == "tag":
                        taglist += (tag.nodeValue.strip()+" ")
        print(taglist.strip())
    except Exception as e:
        print("Oh shi~... No data.xml or it is very ugly.", e)
        sys.exit(2)


def get_provides():
    # global doc
    pkgprovides = ""
    try:
        node = doc.firstChild
        for p in node.childNodes:
            for ptag in p.childNodes:
                if ptag.parentNode.nodeName == "provides":
                    pkgprovides = ptag.nodeValue.strip()
        print(pkgprovides)
    except Exception as e:
        print("Oh shi~... No data.xml or it is very ugly.", e)
        sys.exit(2)


def get_conflicts():
    # global doc
    pkgconflicts = ""
    try:
        node = doc.firstChild
        for p in node.childNodes:
            for ptag in p.childNodes:
                if ptag.parentNode.nodeName == "conflicts":
                    pkgconflicts = ptag.nodeValue.strip()
        print(pkgconflicts)
    except Exception as e:
        print("Oh shi~... No data.xml or it is very ugly.", e)
        sys.exit(2)


if sys.argv[2] == "-m":
    get_maintainer()
#   sys.exit(0)
elif sys.argv[2] == "-d":
    get_deps()
#    sys.exit(0)
elif sys.argv[2] == "-p":
    get_package_attrs()
    sys.exit(0)
elif sys.argv[2] == "-t":
    get_tags()
    sys.exit(0)
elif sys.argv[2] == "-P":
    get_provides()
    sys.exit(0)
elif sys.argv[2] == "-C":
    get_conflicts()
    sys.exit(0)

else:
    print("Unknown arg.")
    sys.exit(2)
