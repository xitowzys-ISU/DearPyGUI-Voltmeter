import dearpygui.dearpygui as dpg


def voltmeter_digital():

    with dpg.font_registry():
        ds_font = dpg.add_font("fonts/DS-DIGI.TTF", 20)

    with dpg.window(label="Voltmeter digital"):

        with dpg.table(header_row=False, resizable=True, policy=dpg.mvTable_SizingStretchProp,
                       borders_outerH=True, borders_innerV=True, borders_outerV=True):

            for i in range(2):
                dpg.add_table_column()

            with dpg.table_row():
                dpg.add_text("Current voltage")
                cur_voltage = dpg.add_text(
                    "", indent=5, tag="__current_voltage", color=[0, 255, 0, 255])

            with dpg.table_row():
                dpg.add_text("Input aggregation time")
                input_text = dpg.add_input_text(
                    default_value=2, indent=5, decimal=True, no_spaces=False, tag="__input_text")

            with dpg.table_row():
                dpg.add_text("Average voltage")
                mean_voltage = dpg.add_text(
                    "", indent=5, tag="__mean_voltage", color=[0, 255, 0, 255])

    dpg.bind_item_font(cur_voltage, ds_font)
    dpg.bind_item_font(mean_voltage, ds_font)
    dpg.bind_item_font(input_text, ds_font)
