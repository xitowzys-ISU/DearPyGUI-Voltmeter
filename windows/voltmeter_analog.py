import numpy as np
import dearpygui.dearpygui as dpg


def voltmeter_analog() -> None:

    with dpg.font_registry():
        ds_font = dpg.add_font("fonts/DS-DIGI.TTF", 20)

    with dpg.window(label="Voltmeter analog"):

        with dpg.drawlist(width=350, height=190):
            # padding 10
            with dpg.draw_layer():
                dpg.draw_circle((175, 190), 140)

                textV5: int | str = dpg.draw_text(
                    (165, 27), "5V", color=(255, 255, 100), size=20)
                dpg.draw_line((175, 45), (175, 55))
                dpg.bind_item_font(textV5, ds_font)

                textV0 = dpg.draw_text(
                    (5, 170), "0V", color=(255, 255, 100), size=20)
                dpg.draw_line((30, 199), (40, 199))
                dpg.bind_item_font(textV0, ds_font)

                textV10 = dpg.draw_text((319, 169), "10V", color=(
                    255, 255, 100), size=20)
                dpg.draw_line((310, 199), (320, 199))
                dpg.bind_item_font(textV10, ds_font)

                for i in range(0, 181, 5):
                    py = np.cos(np.deg2rad(i)) * 140
                    px = np.sin(np.deg2rad(i)) * 140
                    dpg.draw_circle((175-py, 190-px), 1)

            with dpg.draw_node(tag="main"):
                with dpg.draw_node(tag="arrow"):
                    v = 5
                    v *= 18
                    px = np.cos(np.deg2rad(v)) * 135
                    py = np.sin(np.deg2rad(v)) * 135
                    a = dpg.draw_line((px, py), (0, 0), color=(
                        255, 255, 100), thickness=2, tag="20")

            dpg.draw_circle((350/2, 190), 20,
                            color=(255, 255, 255, 255), fill=[255, 255, 100])
