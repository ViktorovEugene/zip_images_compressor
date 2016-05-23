import zipfile
import logging


def test_zip(zip_name):
    logging.info('"%s" is zip file => %s', zip_name,
                 zipfile.is_zipfile(zip_name))


def process_zip(zip_name):
    test_zip(zip_name)
