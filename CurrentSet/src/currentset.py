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
    #Data ={"Target name":"", "Target IP":"", "HW type":""}
    Targets=[]
    IPs=[]
    HW=[]
    allData=[]
    test2 = []
    tbllst = root.findall('.//table')
    for elem in tbllst[0][0]:  # iterating over table/tbody/tr elements
        if elem.tag == 'tr':
            counter = 1
            test=[]
            for td in elem:
                if counter == 1:
                    Targets.append(td.text)
                    test.append(td.text)
                    counter += 1
                elif counter == 3:
                    IPs.append(td.text)
                    test.append(td.text)
                    counter += 1
                elif counter == 10:
                    HW.append(td.text)
                    if td.text != None:
                        test.append(td.text)
                    counter += 1
                else:
                    counter += 1
            if len(test) == 3:
                test2.append(test)
                
    test2.sort(key=lambda item: (item[2], item[0]), reverse=False)
    #allData = sorted(allData, key = lambda item: (item[0], item[1]))
                
    return test2


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


