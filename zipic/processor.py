import zipfile
import logging


def check_if_its_zip(zip_name):
    if not zipfile.is_zipfile(zip_name):
        raise TypeError('Expected namely ZIP file.')
    logging.info('"%s" is zip file', zip_name)


def check_zips_for_errors(zip_obj):
    bad_zip_content = zip_obj.testzip()
    if bad_zip_content:
        raise zipfile.BadZipFile("The %s of this ZIP file has the bad CRC." %
                                 bad_zip_content)


def process_zip(zip_name):
    check_if_its_zip(zip_name)
    with zipfile.ZipFile(zip_name, 'r') as zip_obj:
        check_zips_for_errors(zip_obj)