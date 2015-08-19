import sys
sys.path.insert(0, '../lib')

# Wrapper for ElementTree
# api: http://docs.python.org/2/library/xml.etree.elementtree.html
import ElementSoup as ES


def parse(fobj):
    '''
    Parse HTML file and extract targets data
    '''

    root = ES.parse(fobj)
    tbllst = root.findall('.//table')
    for elem in tbllst[0][0]:  # iterating over table/tbody/tr elements
        if elem.tag == 'tr':
            field = 1
            for td in elem:
                if field == 1:
                    if td.text == "Target name":
                        field = field + 1
                        continue
                    print td.text
                    field = field + 1
                elif field == 3:
                    if td.text == "Target IP":
                        field = field + 1
                        continue
                    print td.text
                    field = field + 1
                elif field == 10:
                    if td.text == "HW type":
                        field = field + 1
                        continue
                    print td.text
                    field = field + 1
                field = field + 1


def report(targets):
    '''
    Generate targets report to standard output in the form:
    <HW type>

    <Target name> <Target IP>
    <Target name> <Target IP>
    ...
    <Target name> <Target IP>

    <HW type>

    <Target name> <Target IP>
    <Target name> <Target IP>
    ...
    <Target name> <Target IP>
    ...

    '''

    # !!!Your code here!!!


def main():
    with open('currentsets.html') as f:
        report(parse(f))


if __name__ == '__main__':
    main()


