from turtle import *  # 描画環境 turtle をインポート
from rose import *  # plot1.pyと同一フォルダにあるrose.pyをインポート
hideturtle()
rose_window_recursion(
    [[-50, -100],[200, -150], [50, 100], [-200, 150]], 0.9, 40)
done()  # turtleの終了処理