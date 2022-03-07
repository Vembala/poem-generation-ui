"""main"""

from text_box import TextBox
from output_label import OutputLabel
from layout import VerticalBox
from central_widget import CentralWidget

text_box = TextBox()
output_label = OutputLabel()
vertical_box = VerticalBox(text_box, output_label,)
central_widget = CentralWidget(vertical_box,)
