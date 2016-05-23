import os
import zipfile
import logging
import tempfile


def check_if_its_zip(zip_name):
    if not zipfile.is_zipfile(zip_name):
        raise TypeError('Expected namely ZIP file.')
    logging.info('"%s" is zip file', zip_name)


def check_zips_for_errors(zip_obj):
    bad_zip_content = zip_obj.testzip()
    if bad_zip_content:
        raise zipfile.BadZipFile("The %s of this ZIP file has the bad CRC." %
                                 bad_zip_content)


def get_zips_png_file_names(zip_object):
    return [name for name in zip_object.namelist() if name[-4:] == '.png']


def process_zip(zip_name):
    check_if_its_zip(zip_name)
    zip_obj = zipfile.ZipFile(zip_name, 'r')
    zip_obj_abs_path = os.path.abspath(zip_obj.filename)

    curr_cwd = os.getcwd()

    try:

        check_zips_for_errors(zip_obj)
        zips_png_names = get_zips_png_file_names(zip_obj)
        logging.info("PNG files in given zip =>\n%s",
                     ', '.join(zips_png_names))

        with tempfile.TemporaryDirectory(suffix='_zip') as tmpdirname:
            zip_obj.extractall(tmpdirname, zips_png_names)
            zip_obj.close()

            os.chdir(tmpdirname)

            logging.info("Processing PNG files...")

            with os.popen('find . -name "*.png" -exec '
                          'pngquant --ext ".png" --force 16 {} \;'):
                pass

            logging.info("Update the source archive...")

            with os.popen('zip -r %s "%s"' % (zip_obj_abs_path,
                                              '" "'.join(zips_png_names))
                          ) as file_:
                console_run_result = file_.read()

            logging.info('"zip" console call:\n\t%s',
                         '\n\t'.join(console_run_result.split('\n')))

    finally:
        os.chdir(curr_cwd)
        zip_obj.close()
