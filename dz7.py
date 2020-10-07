import platform
import logging


logging.basicConfig(level=logging.INFO,
                    filename="app_test2.log",
                    filemode="w")
logging.info("Information about System")

logging.info((f'Version           : ', {platform.python_version()} ))
logging.info((f'Version tuple     : ', {platform.python_version_tuple()}))

logging.info((f'Compiler          : ', {platform.python_compiler()}))
logging.info((f'Build             : ', {platform.python_build()}))


logging.info((f'System            : ', {platform.system()}))
logging.info((f'Node              : ', {platform.node()}))
logging.info((f'Release           : ', {platform.release()}))
logging.info((f'Version           : ', {platform.version()}))
logging.info((f'Machine           : ', {platform.machine()}))
logging.info((f'Processor         : ', {platform.processor()}))

logging.info((f'Interpreter       : ', {platform.architecture()}))