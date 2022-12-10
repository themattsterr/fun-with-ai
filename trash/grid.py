import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor, QPainter, QBrush
from PyQt5.QtCore import Qt

class Grid(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the window title and size
        self.setWindowTitle("Grid")
        self.resize(400, 300)

        # Create a 5 by 6 grid of squares
        self.num_rows = 5
        self.num_cols = 6
        self.cell_width = self.width() / self.num_cols
        self.cell_height = self.height() / self.num_rows

    def paintEvent(self, event):
        painter = QPainter(self)

        # Draw each square in the grid
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = col * self.cell_width
                y = row * self.cell_height

                # Set the brush color and draw the rectangle
                brush = QBrush(QColor("#ffffff"))
                painter.setBrush(brush)
                painter.drawRect(x, y, self.cell_width, self.cell_height)

                # Add a letter to the center of each square
                text = "A"
                font = painter.font()
                font.setPointSize(24)
                painter.setFont(font)
                metrics = painter.fontMetrics()
                x_offset = (self.cell_width - metrics.width(text)) / 2
                y_offset = (self.cell_height - metrics.height()) / 2
                painter.drawText(x + x_offset, y + y_offset, text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    grid = Grid()
    grid.show()
    sys.exit(app.exec_())
