import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class OutputWindow(Gtk.Window):
    def __init__(self):
				
        Gtk.Window.__init__(self, title="Command Output")
        self.set_default_size(600, 400)
        # Create a text view to display the output
        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textview.set_editable(False)
				
        # Add the text view to a scrollable window
        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.add(self.textview)
        self.add(self.scrolled_window)

    def run_command(self, command):
        # Run the command and redirect output to the text buffer
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        while True:
            output = process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                self.textbuffer.insert(self.textbuffer.get_end_iter(), output.decode("utf-8"))
        rc = process.poll()
    def destroy(self):
        if self.process is not None:
            self.process.terminate()
        Gtk.Window.destroy(self)

w = OutputWindow()
w.run_command(sys.argv[1])
w.show_all()
Gtk.main()
