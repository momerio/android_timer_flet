import flet
import time


def main(page: flet.Page):
    """fletメイン関数

    Args:
        page (flet.Page): _description_
    """
    # windowタイトル
    page.title = "Hello World"

    # windowサイズ
    page.window_width = 600
    page.window_height = 400

    # windowの位置
    page.window_top = 300
    page.window_left = 600

    # window内のコントロールの縦位置
    page.vertical_alignment = flet.MainAxisAlignment.CENTER

    # Textコントロール（一般的にはLabelと呼ばれるもの）
    t = "Hello world!"
    text = flet.Text(value=t, size=50, color="gray")

    # クリックイベント
    def start_button(e):
        time_ = 0
        while True:
            time_ += 1
            print(time_)
            time.sleep(1)
            text.value = str(time_)
            page.update()

    # クリックイベント
    def stop_button(e):
        time_ = 0
        text.value = str(time_)
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
                flet.IconButton(flet.icons.PLAY_CIRCLE_FILL_OUTLINED, icon_size=50, on_click=start_button),
                # flet.IconButton(flet.icons.PLAY_CIRCLE_FILL_OUTLINED, icon_size=50, on_click=stop_button),
            ],
            # 横位置をセンターにする
            alignment=flet.MainAxisAlignment.CENTER,
        ),
    )


flet.app(target=main)
