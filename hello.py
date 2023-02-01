import flet
import time
import math


def _time_conversion(t: int):
    """カンマ秒から時間文字列に変換

    Args:
        t (int): カンマ秒（最小時間）

    Returns:
        str: 時間文字列
    """
    splits_: str = str(math.floor(t % 1000)).zfill(3)
    t: int = t // 1000
    seconds_: str = str(math.floor(t % 60)).zfill(2)
    t: int = t // 60
    minutes_: str = str(math.floor(t % 60)).zfill(2)
    t: int = t // 60
    hours_: str = str(math.floor(t % 60)).zfill(1)

    time_str: str = f"{hours_}:{minutes_}:{seconds_}.{splits_}"

    return time_str


def main(page: flet.Page):
    """fletメイン関数

    Args:
        page (flet.Page): _description_
    """
    # windowタイトル
    page.title = "COUNT UP TIMER"

    # windowサイズ
    page.window_width = 600
    page.window_height = 400

    # windowの位置
    page.window_top = 300
    page.window_left = 600

    # window内のコントロールの縦位置
    page.vertical_alignment = flet.MainAxisAlignment.CENTER

    # Textコントロール（一般的にはLabelと呼ばれるもの）
    t = "COUNT UP TIMER"
    text = flet.Text(value=t, size=50, color="gray")

    IS_START = True  # タイマー開始中フラグ

    # 時間
    hours = 0  # 時間
    minutes = 0  # 分
    seconds = 0  # 秒
    splits = 0  # カンマ秒

    # スタート・ストップボタン
    def start_button(e):
        time_ = 0
        while IS_START:
            time_ += 1
            text.value = _time_conversion(time_)
            time.sleep(0.001)
            page.update()

    # リセットボタン
    def reset_button(e):
        global IS_START
        time_ = 0
        text.value = str(time_)
        IS_START = False
        page.update()

    # ページにコントロールを追加
    page.add(
        flet.Row(
            [text],
            # 横位置をセンターにする
            alignment=flet.MainAxisAlignment.CENTER,
        ),
        flet.Row(
            [
                # アイコンボタン
                flet.IconButton(
                    icon=flet.icons.RESTART_ALT_OUTLINED, icon_size=50, tooltip="reset", on_click=reset_button
                ),  # リセットボタン
                flet.IconButton(
                    flet.icons.PLAY_CIRCLE_FILL_OUTLINED, icon_size=50, tooltip="start", on_click=start_button
                ),  # スタートボタン
            ],
            # 横位置をセンターにする
            alignment=flet.MainAxisAlignment.CENTER,
        ),
    )


flet.app(target=main)
