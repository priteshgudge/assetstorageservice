import errno
import os
from werkzeug.utils import secure_filename


def save_file(file, directory):
    """
    Save file in a directory. Create directory if not present.
    :param file: file object
    :param directory: directory to store file
    :return: file path where file is stored
    """

    # http://werkzeug.pocoo.org/docs/0.11/utils/#werkzeug.utils.secure_filename
    filename = secure_filename(file.filename)
    file_path = "{}/{}".format(directory, filename)

    # Write to file even if dir doesn't exist
    # http://stackoverflow.com/questions/23793987/python-write-file-to-directory-doesnt-exist
    try:
        os.makedirs(directory)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(directory):
            pass
        else:
            raise

    file.save(file_path)

    return file_path
