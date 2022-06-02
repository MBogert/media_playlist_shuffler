import unittest
import util as u
import playlist
import re


# To Test
# python -m unittest test.py

# || util.py || #

class IsDirectoryTest(unittest.TestCase):

    def test_is_true(self):
        self.assertTrue(u.is_directory('/folder/folder'))

    def test_is_false(self):
        self.assertFalse(u.is_directory('/folder/file.format'))


class IsValidFormatTest(unittest.TestCase):

    def test_valid_format_simple_path(self):
        self.assertTrue(u.is_valid_format(u.SUPPORTED_VIDEO_FORMATS, '/folder/video.mov'))

    # e.g. filename with a period-character
    def test_valid_format_esoteric_path(self):
        self.assertTrue(u.is_valid_format(u.SUPPORTED_VIDEO_FORMATS, '/folder/video.videoweehee.mov'))

    def test_invalid_format(self):
        self.assertFalse(u.is_valid_format(u.SUPPORTED_VIDEO_FORMATS, '/folder/photo.png'))

    def test_invalid_path(self):
        self.assertFalse(u.is_valid_format(u.SUPPORTED_VIDEO_FORMATS, '/folder/invalid_file'))


class GetFileFormatTest(unittest.TestCase):

    def test_valid_filename(self):
        self.assertEqual(u.get_file_format('folder/video.mp4'), '.mp4')

    # e.g. multiple period's in name
    def test_esoteric_filename(self):
        self.assertEqual(u.get_file_format('folder/video.videoweehee.mp4'), '.mp4')

    def test_invalid_filename(self):
        self.assertEqual(u.get_file_format('folder/invalid_file'), '')


# || playlist.py || #
class GetFilepathsTest(unittest.TestCase):

    def create_filepaths(self):
        media_list = ['video_1.mp4', 'video_2.mp4', 'photo_1.jpg', 'photo_2.png', 'photo_3.tiff', 'photo_4.jpg',
                      'photo_5.png', 'photo_7.jpg', 'photo_8.jpg']
        user_input = (u.PHOTO_FORMAT, 4)
        return playlist.get_filepaths(media_list, user_input)

    # List of photo and video media will return the appropriate number of filepaths, without any invalid formats
    def test_verify_length(self):
        self.assertEqual(len(self.create_filepaths()), 4)

    def test_verify_formats(self):
        filepaths = self.create_filepaths()
        invalid_paths = []
        for file in filepaths:
            if re.search('.\.mp4', file):
                invalid_paths.append(file)
        self.assertFalse(invalid_paths)



