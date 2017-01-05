# coding:utf-8
# Copyright

import logging
import re

logging.basicConfig(filename='temp.log',
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
module_logger = logging.getLogger('test_log_info')
module_logger.setLevel(logging.INFO)


def test_l():
    module_logger.info('log_pre_definded')
    a = 1
    b = 0
    for i in range(3, -5, -1):
        module_logger.info(i)
        y = a / i

    return a / b


if __name__ == '__main__':
    try:
        test_l()
        module_logger.info('log_finished')
        module_logger.info('logg_info:')
    except ZeroDivisionError:
        module_logger.exception('logg_excep: ')

    with open('temp.log', 'r') as f:
        x = f.read()
        s0 = re.compile(r'INFO (\d+)')
        if re.findall(s0, x):
            yy = re.findall(s0, x)
            zz = len(yy) - 1
        else:
            module_logger.info('Not find')

    print('you got it: %s' % yy[zz])
