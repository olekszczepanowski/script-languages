from kivy.app import App
import os
import script
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.popup import Popup
from script import createLogList, createRawEntriesList, filterLogList, changeRawEntry


class LogBrowser(BoxLayout):
    def __init__(self, **kwargs):
        super(LogBrowser, self).__init__(orientation="vertical", **kwargs)
        self.log_buttons = []
        self.logs = []
        Window.size = (1300, 600)

        path_container = GridLayout(cols=2)
        path_container.padding = [15, 15, 15, 15]
        self.path_input = TextInput(text="SSHTEST.log", width=500)

        path_button = Button(text="Open")
        path_button.bind(on_press=lambda instance: self.load_logs())
        path_container.add_widget(self.path_input)
        path_container.add_widget(path_button)

        self.add_widget(path_container)

        date_container = GridLayout(cols=4)
        date_container.padding = [15, 15, 15, 15]
        self.date_from = TextInput(text="date from (YYYY-MM-DD)")
        self.date_to = TextInput(text="date to (YYYY-MM-DD)")
        reset_button = Button(text="Reset")
        filter_button = Button(text="Filter")
        filter_button.bind(on_press=lambda instance: self.filter_logs())
        date_container.add_widget(self.date_from)
        date_container.add_widget(self.date_to)
        date_container.add_widget(reset_button)
        date_container.add_widget(filter_button)

        self.add_widget(date_container)

        self.logs_scrollview = ScrollView(height="500px")
        self.logs_scrollview.do_scroll_y = True
        self.logs_container = BoxLayout(orientation="vertical", size_hint_y=None)  # Set size_hint_y to None
        self.logs_scrollview.add_widget(self.logs_container)

        self.selected_button = None

        self.add_widget(self.logs_scrollview)

        details_container = GridLayout(cols=2, rows=4, height=250)
        details_container.add_widget(Label(text='date'))
        self.date = Label(text='None')
        details_container.add_widget(self.date)

        details_container.add_widget(Label(text='hostname'))
        self.hostname = Label(text='None')
        details_container.add_widget(self.hostname)

        details_container.add_widget(Label(text='PID number'))
        self.pid = Label(text='None')
        details_container.add_widget(self.pid)

        details_container.add_widget(Label(text='description'))
        self.description = Label(text='None')
        details_container.add_widget(self.description)

        self.add_widget(details_container)

        nav_container = GridLayout(cols=2)
        self.next_button = Button(text="Next")
        self.next_button.bind(on_press=lambda instance: self.next_log())
        self.prev_button = Button(text="prev")
        self.prev_button.bind(on_press=lambda instance: self.prev_log())
        self.current_log_index = 0
        nav_container.add_widget(self.next_button)
        nav_container.add_widget(self.prev_button)
        self.add_widget(nav_container)

    # def create_logs_buttons(self, path):
    #     if os.path.exists(path):  # Sprawdzamy, czy ścieżka istnieje
    #         self.logs = createLogList(path)
    #         raw_entries = createRawEntriesList(self.logs)
    #         print(raw_entries)
    #         for entry in raw_entries:
    #             button = Button(text=entry, size_hint_y=None, height=40)
    #             button.bind(on_press=self)
    #             self.logs_container.add_widget(button)
    #             self.log_buttons.append(button)
    #     else:
    #         popup = Popup(title='Error', content=Label(text='Invalid path'), size_hint=(None, None), size=(400, 200))
    #         popup.open()

    def update_logs_display(self, logs):
        self.logs_container.clear_widgets()
        self.log_buttons = []

        for index, log_entry in enumerate(logs):
            self.create_logs_buttons(log_entry, index)

            self.next_button.disabled = True
            self.prev_button.disabled = True

    def load_logs(self):
        path = self.path_input.text
        try:
            self.logs = createLogList(path)
            print("Type of self.logs:", type(self.logs))
            print("Length of self.logs:", len(self.logs))
            print(self.logs.logsList)
            self.update_logs_display(self.logs)
        except FileNotFoundError as e:
            self.show_popup(str(e))

    def filter_logs(self):
        try:
            startDate = self.date_from.text
            endDate = self.date_to.text
            self.logs = filterLogList(self.logs, startDate, endDate)
        except ValueError as e:
            self.show_popup(str(e))

    def show_popup(self, message):
        popup = Popup(title='Error',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

    def displayLogInformation(self):
        log = self.logs[self.current_log_index]
        self.updateLogDetails(log)

    def update_log_details(self, log):
        self.date.text = str(log.date.date())
        self.hostname.text = str(log.hostname)
        self.pid.text = str(log.pidNumber)
        self.description.text = str(log.description)

    def create_logs_buttons(self, log_entry, index):
        btn_text = changeRawEntry(log_entry.getRawEntry())
        btn = Button(text=btn_text, size_hint_y=None, height=40)
        btn.bind(on_press=lambda instance: self.log_button_clicked(instance, log_entry, index))
        self.logs_container.add_widget(btn)
        self.log_buttons.append(btn)

    def log_button_clicked(self, instance, log, index):
        if self.selected_button:
            self.selected_button.background_color = [1, 1, 1, 1]

        instance.background_color = [0.5, 0.5, 1, 1]

        self.selected_button = instance
        self.current_log_index = index

        self.update_log_details(log)
        self.prev_button.disabled = self.current_log_index == 0
        self.next_button.disabled = self.current_log_index == len(self.logs) - 1

    def prev_log(self):
        if self.current_log_index > 0:
            self.current_log_index -= 1
            selected_button = self.log_buttons[self.current_log_index]
            log_entry = self.logs.logsList[self.current_log_index]
            self.log_button_clicked(selected_button, log_entry, self.current_log_index)

    def next_log(self):
        if self.current_log_index < len(self.logs) - 1:
            self.current_log_index += 1
            selected_button = self.log_buttons[self.current_log_index]
            log_entry = self.logs.logsList[self.current_log_index]
            self.log_button_clicked(selected_button, log_entry, self.current_log_index)

    def display_logs(self):
        log = self.logs[self.current_log_index]
        self.updateLogDetails(log)


class MyApp(App):
    def build(self):
        self.title = "LogBrowser"
        return LogBrowser()


if __name__ == "__main__":
    MyApp().run()
