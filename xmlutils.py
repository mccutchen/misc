
import Pyana

def transformPaths(xmlpath, xslpath, outpath=None):
    xmldata = file(xmlpath).read()
    xsldata = file(xslpath).read()
    transformStrings(xmldata, xsldata, outpath)

def transformStrings(xmldata, xsldata, outpath=None):
    results = Pyana.transform2String(xmldata, xsldata)
    if outpath:
        file(outpath, 'w').write(results)
    else:
        print results
