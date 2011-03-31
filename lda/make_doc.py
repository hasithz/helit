#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2011 Tom SF Haines

# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.



import lda
import pydoc

doc = pydoc.HTMLDoc()


# Open the document...
out = open('lda.html','w')
out.write('<html>\n')
out.write('<head>\n')
out.write('<title>pylda</title>\n')
out.write('</head>\n')
out.write('<body>\n')


# Openning blob...
readme = open('readme.txt','r').read()
readme = readme.replace('\n','<br/>')
out.write(doc.bigsection('Overview','#ffffff','#7799ee',readme))


# lda functions...
funcs = doc.docroutine(lda.getAlgorithm)
funcs = funcs.replace('&nbsp;',' ')
out.write(doc.bigsection('Functions','#ffffff','#eeaa77',funcs))


# Classes...
classes = ''
classes += doc.docclass(lda.Document)
classes += doc.docclass(lda.Topic)
classes += doc.docclass(lda.Corpus)
classes += doc.docclass(lda.Params)
classes = classes.replace('&nbsp;',' ')
out.write(doc.bigsection('Classes','#ffffff','#ee77aa',classes))


# Close the document...
out.write('</body>\n')
out.write('</html>\n')
out.close()
