# keras model 导出图片的example
# 适用于 Python 3.x 情形
# windows http://www.graphviz.org/ 下载官方的msi or exe
# pip install graphviz
# dot -v 测试是否安装成功
# pip install pydotplus

from keras.utils.vis_utils import plot_model
from keras.models import Model
import os
# python pydot-plus 未定位到Grahpviz;
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# model keras model
plot_model(Model, to_file='model1.png',show_shapes=True);
