import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from pinyin_tone_converter.pinyin_tone_converter import PinyinToneConverter


class PinyinToneConverterWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Pinyin Tone Converter")

        converter = PinyinToneConverter()

        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(18)

        examples = QHBoxLayout()
        examples.setSpacing(24)
        for word in ("mā má mǎ mà").split():
            label = QLabel(word)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            font = QFont(label.font())
            font.setPointSize(32)
            label.setFont(font)
            examples.addWidget(label)
        layout.addLayout(examples)

        input_label = QLabel("Pinyin with numbers:")
        layout.addWidget(input_label)

        self.input_edit = QLineEdit()
        self.input_edit.setPlaceholderText("For example: ni3 hao3")
        self.input_edit.returnPressed.connect(
            lambda: self.convert_input(converter)
        )
        layout.addWidget(self.input_edit)

        result_row = QHBoxLayout()
        self.result_edit = QLineEdit()
        self.result_edit.setReadOnly(True)
        self.result_edit.setPlaceholderText("Converted pinyin")
        result_row.addWidget(self.result_edit)

        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.copy_result)
        result_row.addWidget(copy_button)
        layout.addLayout(result_row)

        self.setCentralWidget(content)

    def convert_input(self, converter: PinyinToneConverter) -> None:
        pinyin_string = self.input_edit.text()
        converted_pinyin = converter.convert_text(pinyin_string)
        self.result_edit.setText(converted_pinyin)

    def copy_result(self) -> None:
        QApplication.clipboard().setText(self.result_edit.text())


def main() -> int:
    app = QApplication(sys.argv)
    window = PinyinToneConverterWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
