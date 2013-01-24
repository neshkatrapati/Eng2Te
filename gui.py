#!/usr/bin/python
from gi.repository import Gtk
from classes import *

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Eng2Te")

       
        self.abtd = Gtk.AboutDialog()
        self.abtd.set_name("About Eng2Te")
        self.abtd.set_title("About Eng2Te")
        self.abtd.set_authors(["Ganesh Katrapati"])
        self.abtd.set_program_name("Eng2Te")

        self.abtd.set_license(open("COPYING").read())

        self.vbox = Gtk.VBox(spacing=6)
        self.add(self.vbox)
        self.hbox = Gtk.HBox(spacing=16)
        self.misc = Gtk.HBox(spacing=1)
        self.welcome = Gtk.Label("Welcome to Eng2Te!!")
        image = Gtk.Image()
        image.set_from_stock(Gtk.STOCK_ABOUT,Gtk.IconSize.BUTTON)
        self.about = Gtk.Button()
        self.about.set_label("?")
        self.about.set_size_request(10,10)
        self.welcome.set_size_request(490,10)
        self.misc.add(self.welcome)
        self.misc.add(self.about)
        self.vbox.add(self.misc)
        self.vbox.add(self.hbox)
        scrolled_window = Gtk.ScrolledWindow()
        self.text = Gtk.TextView()
        scrolled_window.add_with_viewport(self.text)
        self.vbox.add(scrolled_window)
        label = Gtk.Label("Query:")
        self.entry = Gtk.Entry()
        self.button = Gtk.Button(label="Search")
        self.button.connect("clicked", self.on_button_clicked)
        self.about.connect("clicked", self.on_about_button_clicked)
        self.hbox.add(label)
        self.hbox.add(self.entry)
        self.hbox.add(self.button)
        
        scrolled_window.set_size_request(500, 400)
        self.hbox.set_size_request(500, 30)
        self.entry.set_size_request(300,20)
        self.dic = Dictionary("resources/eng2te.csv")
    
    def on_about_button_clicked(self, widget):
        self.abtd.show()
    def on_button_clicked(self, widget):
        self.text.get_buffer().set_text("")
        text = self.entry.get_text()
        if text != None and text != "":
            results,exact = self.dic.getValue(text)
            
            if results == None or len(results) < 1:
                self.text.get_buffer().set_text("\tNo Results Found!!!")
                return None

            if exact:
                self.display_helper(results)
            else:
                for result in results:
                    self.display_helper(result,False)

    def display_helper(self,results,exact = True):
        t = ""
        t += " "+results["key"]+ "~"+results["pos"]+"\n\n"
        i = 1
        for value in results["values"]:
            t += "\t"+str(i)+". "+str(value)+"\n"
            i += 1
        if exact == False:
            ts = self.text.get_buffer().get_text(self.text.get_buffer().get_start_iter() , self.text.get_buffer().get_end_iter(),True)
            t = ts+"\n"+t

        self.text.get_buffer().set_text(t)


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
