import dearpygui.dearpygui as dpg


def voltmeter_plot() -> None:
    with dpg.window(label="Voltmeter plot"):

        with dpg.table(header_row=False, resizable=True, policy=dpg.mvTable_SizingStretchProp,
                       borders_outerH=True, borders_innerV=True, borders_outerV=True):
            dpg.add_table_column()

            with dpg.table_row():

                with dpg.plot(label="Voltage plot", height=400, width=400):

                    dpg.add_plot_legend()

                    dpg.add_plot_axis(dpg.mvXAxis, label="x")
                    dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")

                    dpg.add_line_series(
                        [.0], [.0], parent="y_axis", tag="series_tag")
