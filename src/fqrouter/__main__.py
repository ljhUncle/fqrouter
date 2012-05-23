import argparse
import logging
from fqrouter.node import ping_pong

root_parser = argparse.ArgumentParser(description="Qin Fen's Router")
root_parser.add_argument('--debug', action='store_const', const=True, default=False)
sub_parsers = root_parser.add_subparsers()
ping_parser = sub_parsers.add_parser('ping')
ping_parser.add_argument('host')
ping_parser.add_argument('port', type=int)
ping_parser.set_defaults(handle_by=ping_pong.ping)
pong_parser = sub_parsers.add_parser('pong')
pong_parser.add_argument('port', type=int)
pong_parser.set_defaults(handle_by=ping_pong.pong)
args = root_parser.parse_args()

logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO, format='[%(levelname)s] %(asctime)s %(message)s')
args.handle_by(args)