from abc import ABC, abstractmethod
import subprocess
import mimetypes
import logging


class FileViewer(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def view(self):
        pass


class ImageViewer(FileViewer):
    def __init__(self, path):
        super().__init__(path)

    def view(self):
        subprocess.run(['explorer', self.path])


class TextBuffer:
    def __init__(self):
        self.text = ""

    def read_from_file(self, path):
        with open(path) as file:
            self.text = file.read()


class TextStats:
    def __init__(self):
        self.number_of_lines = 0
        self.number_of_words = 0
        self.number_of_nonalpha = 0

    def __str__(self):
        return f"number of lines {self.number_of_lines} \n" \
            f"number of words {self.number_of_words} \n" \
            f"number of nonalpha {self.number_of_nonalpha}"

    def compute(self, text):
        temp = text.splitlines()
        for line in temp:
            self.number_of_lines += 1
            for _ in line.split():
                self.number_of_words += 1
            for letter in line:
                if letter.isalpha():
                    self.number_of_nonalpha += 1


class TextViewer(FileViewer, TextBuffer):
    def __init__(self, path):
        FileViewer.__init__(self, path)
        TextBuffer.__init__(self)

    def view(self):
        subprocess.run(['notepad', self.path])

    def read_from_file(self):
        super().read_from_file(self.path)

    def get_data(self):
        stats = TextStats()
        self.read_from_file()
        stats.compute(self.text)
        return stats


class ViewerCreator:
    def __init__(self):
        pass

    def _detect_viewer_type(self, path):
        file_type = mimetypes.guess_type(path)
        file_type = file_type[0].split('/')
        if file_type[0] == 'text':
            return TextViewer
        elif file_type[0] == 'image':
            return ImageViewer
        else:
            logging.error(f'Wrong type of file: {path}')
            exit(1)

    def create_viewer(self, path):
        file_type = self._detect_viewer_type(path)
        if file_type == TextViewer:
            return TextViewer(path)
        elif file_type == ImageViewer:
            return ImageViewer(path)


def main():
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)
    creator = ViewerCreator()
    text = creator.create_viewer("C:\\Users\\PK\\Downloads\\da1.txt")
    image = creator.create_viewer("C:\\Users\\PK\\Pictures\\Alita.jpg")
    # wrong = creator.create_viewer("C:\\Users\\PK\\Documents\\1.docx")
    image.view()
    text.view()


if __name__ == "__main__":
    main()
