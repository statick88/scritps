import xlrd


wb = xlrd.open_workbook("glosario.xls")
info_sh = wb.sheet_by_index(0)
info_tags = [n.replace(" ", "").lower() for n in info_sh.row_values(0)]

entry_sh = wb.sheet_by_index(1)
entry_tags = [n.replace(" ", "").lower() for n in entry_sh.row_values(0)]

result = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<GLOSSARY>\n"

for row in range(1, info_sh.nrows):
    result += "  <INFO>\n"
    for i in range(len(info_tags)):
        tag = info_tags[i].upper()
        val = info_sh.row_values(row)[i]
        result += "    <{0}>{1}</{0}>\n".format(tag, val)
    if entry_sh.nrows > 0:
        result += "    <ENTRIES>\n"
        for x in range(1, entry_sh.nrows):
            result += "      <ENTRY>\n"
            for y in range(len(entry_tags)):
                tag = entry_tags[y].upper()
                if tag == 'ALIASES':
                    result += '        <ALIASES>\n'
                    aliases = entry_sh.row_values(x)[y].split(',')
                    for alias in aliases:
                        result += '          <ALIAS>\n'
                        result += "            <{0}>{1}</{0}>\n".format('NAME', alias)
                        result += '          </ALIAS>\n'
                    result += '        </ALIASES>\n'
                elif tag == 'CATEGORIES':
                    result += '        <CATEGORIES>\n'
                    categories = entry_sh.row_values(x)[y].split(',')
                    for category in categories:
                        result += '          <CATEGORY>\n'
                        result += '            <{0}>{1}</{0}>\n'.format('NAME', category)
                        result += '            <{0}>{1}</{0}>\n'.format('USEDYNALINK', '1')
                        result += '          </CATEGORY>\n'
                    result += '        </CATEGORIES>\n'
                else:
                    val = entry_sh.row_values(x)[y]
                    result += "        <{0}>{1}</{0}>\n".format(tag, val)
            result += "      </ENTRY>\n"
        result += "    </ENTRIES>\n"
    result += "  </INFO>\n"
result += "</GLOSSARY>"

f = open("glosario.xml", "w")
f.write(result)
f.close() 
