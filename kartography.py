#!/usrr/bin/python

import fiona

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="read from FILE", metavar="FILE")
parser.add_option("-l", "--label",
                  dest="label", default="name",
                  help="label field")
parser.add_option("-w", "--width", dest="width", default="2000",
                  help="svg width output")


(options, args) = parser.parse_args()

input = fiona.open(options.filename, 'r')
f = next(input)
attributes = f['properties'].keys()
input.close()


from kartograph import Kartograph

cfg = {
  "layers": {
      "mylayer": {
          "labeling": { "key": options.label },
          "attributes": attributes,
          "src": options.filename
      }
  },
  "export": {
    "width": int(options.width)
  }
}


K = Kartograph()

filename = options.filename + '.svg'
print filename
K.generate(cfg, outfile=filename)
