import shutil
import os
import zipfile
import pytest


@pytest.fixture
def test_add_in_zip_file():
        os.chdir('resources')
        with zipfile.ZipFile('archive.zip', 'w') as zp:
            zp.write('file_txt.txt')
            zp.write('file1.xls')
            zp.write('file2.xlsx')
            zp.write('file_book.pdf')

        if not os.path.isdir('../tmp'):
            os.mkdir('../tmp')
        shutil.move('archive.zip', os.path.join('../tmp', 'archive.zip'))
        yield