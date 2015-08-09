import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fac3b6da'.decode('hex')
P2P_PORT = 12024
ADDRESS_VERSION = 30
RPC_PORT = 14022
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '7497ea1b465eb39f1c8f507bc877078fe016d6fcb6dfad3a64c98dcc6e1e8496')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: __import__('digibyte_subsidy').GetBlockBaseValue(height)
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('skeinhash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'DGB'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'digibyte') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/digibyte/') if platform.system() == 'Darwin' else os.path.expanduser('~/.digibyte'), 'digibyte.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://digiexplorer.info/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://digiexplorer.info/address/'
TX_EXPLORER_URL_PREFIX = 'http://digiexplorer.info/tx/'
SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**26 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
