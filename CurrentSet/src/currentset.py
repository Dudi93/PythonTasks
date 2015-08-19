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
    data = []
    tbllst = root.findall('.//table')
    for elem in tbllst[0][0]:  # iterating over table/tbody/tr elements
        if elem.tag == 'tr':
            counter = 1
            temp=[]
            for td in elem:
                if counter == 1:
                    temp.append(td.text)
                    counter += 1
                elif counter == 3:
                    temp.append(td.text)
                    counter += 1
                elif counter == 10:
                    if td.text != None:
                        temp.append(td.text)
                    counter += 1
                else:
                    counter += 1
            if len(temp) == 3:
                data.append(temp)
                
    data.sort(key=lambda item: (item[2], item[0]), reverse=False)
    #allData = sorted(allData, key = lambda item: (item[0], item[1]))
                
    return data


def report(targets):
    '''
    Generate targets report to standard output in the form:
    <HW type>

    <Target name> <Target IP>
    <Target name> <Target IP>
    ...
    <Target name> <Target IP>

    <HW type>
object
    <Target name> <Target IP>
    <Target name> <Target IP>
    ...
    <Target name> <Target IP>
    ...return 

    '''
    
    #dwa fory tu dopierdolic i chuj bedzie kurwa
    print targets
    
    #sorted1=sorted(targets, key=lambda item: item(9))
    #sorted2=sorted(targets, key=lambda item: item(0))
    
    #for elem in sorted1:
        #if elem
    #    print elem


def main():
    with open('currentsets.html') as f:
        report(parse(f))


if __name__ == '__main__':
    main()


