import os
import zipfile
import logging
import tempfile
import shlex
from subprocess import Popen, PIPE


def check_if_its_zip(zip_name):
    if zipfile.is_zipfile(zip_name):
        logging.info('"%s" is a zip file', zip_name)
        return True
    logging.info('"%s" is not a zip file', zip_name)
    return False


def check_zips_for_errors(zip_obj):
    bad_zip_content = zip_obj.testzip()
    if bad_zip_content:
        raise zipfile.BadZipFile("The %s of this ZIP file has the bad CRC." %
                                 bad_zip_content)


def get_zips_png_file_names(zip_object):
    return [name for name in zip_object.namelist() if name[-4:] == '.png']


def process_image_file(image_name):
        logging.info("Processing PNG file...")
        command_line = '/usr/bin/pngquant --ext ".png" --force 256 "%s"' % \
                       image_name
        args = shlex.split(command_line)
        with Popen(args, stderr=PIPE) as popen_obj:
            outs, errs = popen_obj.communicate(timeout=60)
            if popen_obj.returncode != 0:
                if b"Not a PNG file" in errs:
                    err = '"%s" is not a PNG file.' % image_name
                    raise TypeError(err)
                else:
                    err = 'the "pngquant" subprocess runninghas failed with ' \
                          'the next error message\n%s"' % errs
                    raise ChildProcessError(err)

        logging.info("Finished!")


def process_zip_file(zip_name):
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


def process_file(file_name):
    if check_if_its_zip(file_name):
        process_zip_file(file_name)
    else:
        process_image_file(file_name)
