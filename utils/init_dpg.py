import dearpygui.dearpygui as dpg
from functools import wraps


def init_dpg(func):
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        dpg.create_context()
        dpg.create_viewport(title='Voltmeter', width=800, height=600)
        dpg.setup_dearpygui()
        dpg.show_viewport()

        func(*args, **kwargs)

        dpg.destroy_context()

    return wrapper
