from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['unitus_test_argon2d']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//15 # shares
REAL_CHAIN_LENGTH = 24*60*60//15 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 60 # blocks
IDENTIFIER = 'f7df369093939026'.decode('hex')
PREFIX = '7df5bd7eda3cbe60'.decode('hex')
P2P_PORT = 61603
MIN_TARGET = 0
MAX_TARGET = 2**256//10000 - 1
PERSIST = False
WORKER_PORT = 61604
BOOTSTRAP_ADDRS = 'nz.nutty.one'.split(' ')
VERSION_CHECK = lambda v: None if 90604 <= v else 'Unitus version too old. Upgrade to 0.9.7 or newer!'
ALGORITHM = 'Argon2d'