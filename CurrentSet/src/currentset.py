import sys
sys.path.insert(0, 'D:/TietoProjects/PythonTasks/CurrentSet/lib')

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
                    if td.text == "Target name":
                        counter += 1
                        continue
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
    HWnames={}
    for col in range(0, len(targets)):
        counter = 0
        for name in targets[col]:
            if counter != 2:
                counter += 1
                continue
            if name not in HWnames:
                HWnames[name] = 1
            else:
                HWnames[name] += 1
            continue
    #for key in sorted(HWnames):
    #    print key, HWnames[key]
    count = 1
    testHW = targets[0][2]
    for target, ip, hw in targets:
        if count == 1:
            count += 1
            print '========== ', hw, ' =========='
        if hw == testHW:
            print target, ip
        else:
            testHW = hw
            print '==========================='
            print '========== ', hw, ' =========='
        #print target, ip, hw

    #for data in range(0, len(targets)):
    #    if data == 0:

    #print targets, len(targets), len(targets[2])


def main():
    with open('currentsets.html') as f:
        report(parse(f))


if __name__ == '__main__':
    main()


