import logging

logFmt = logging.Formatter('%(asctime)s\t%(levelname)s -- %(filename)s:%(lineno)s -- %(message)s')
log = logging.getLogger('Extract_AI')

fHdlr = logging.FileHandler(r'log_AI.txt')
fHdlr.setFormatter(logFmt)
log.addHandler(fHdlr)
cHdlr = logging.StreamHandler()
cHdlr.setFormatter(logFmt)
log.addHandler(cHdlr)

log.setLevel(logging.INFO)

log.info('Load Done - Entity ' + 'TEST AI' + ' Done')
log.error(" ERROR -- > JSON element (" ") has no destination ")