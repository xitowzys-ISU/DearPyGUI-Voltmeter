import time

import numpy as np
import dearpygui.dearpygui as dpg

from windows import *
from Serial import Serial
from utils import init_dpg


@init_dpg
def run() -> None:
    serial: Serial = Serial(n=700)

    voltmeter_plot()
    voltmeter_digital()
    voltmeter_analog()

    last_time_read: float = 0
    reset_time: float = 0

    while dpg.is_dearpygui_running():
        serial.time_period = int(dpg.get_value("__input_text"))
        if time.time() - reset_time > serial.time_period:
            reset_time = time.time()

            for i in serial.data:
                if time.time() - i[0] > serial.time_period:
                    serial.data.remove(i)

        if time.time() - last_time_read > 0.02:
            last_time_read = time.time()
            serial.cur_voltage_value = np.round(
                np.random.normal(scale=0.2) + 5, 2)
            serial.data.append((last_time_read, serial.cur_voltage_value))

            serial.update()

            dpg.set_value("__mean_voltage", np.round(
                np.mean(serial.get_y()), 2))

            dpg.set_value("series_tag", [serial.get_x(), serial.get_y()])

            dpg.set_value("__current_voltage", serial.cur_voltage_value)

            dpg.apply_transform(
                "main", dpg.create_translation_matrix([174, 52+140]))

            dpg.apply_transform("arrow", dpg.create_rotation_matrix(
                np.deg2rad(-180 + (serial.cur_voltage_value-5) * 18), [0, 0, 1]))

        dpg.render_dearpygui_frame()


if __name__ == "__main__":
    run()
