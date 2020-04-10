# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================

from Functions import base_dir, os


def GUI(self, Gtk, GdkPixbuf, Gdk, th):

    self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
    self.add(self.vbox)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    # =======================================================
    #                       App Notifications
    # =======================================================

    self.notification_revealer = Gtk.Revealer()
    self.notification_revealer.set_reveal_child(False)

    self.notification_label = Gtk.Label()

    pb_panel = GdkPixbuf.Pixbuf().new_from_file(base_dir + '/images/panel.png')
    panel = Gtk.Image().new_from_pixbuf(pb_panel)

    overlayFrame = Gtk.Overlay()
    overlayFrame.add(panel)
    overlayFrame.add_overlay(self.notification_label)

    self.notification_revealer.add(overlayFrame)

    hbox1.pack_start(self.notification_revealer, True, False, 0)

    # ==========================================================
    #                       LOCATIONS
    # ==========================================================
    lbl = Gtk.Label("Enter Location")
    self.loc.set_size_request(280, 0)
    btnbrowse = Gtk.Button(label="...")
    btnsearch = Gtk.Button(label="Load")

    btnsearch.connect("clicked", self.on_load_clicked, self.fb)
    btnbrowse.connect("clicked", self.on_browse_clicked)

    btnsearch.set_size_request(130, 0)
    hbox6.pack_start(lbl, False, False, 10)
    hbox6.pack_start(self.loc, False, False, 0)
    hbox6.pack_start(btnbrowse, False, False, 5)
    hbox6.pack_end(btnsearch, False, False, 0)

    # ==========================================================
    #                       BUTTON
    # ==========================================================
    self.btnset = Gtk.Button(label="Apply Image")
    self.btnset.connect("clicked", self.on_apply_clicked)
    hbox2.pack_end(self.btnset, False, False, 0)

    # ==========================================================
    #                       PATREON
    # ==========================================================

    pE2 = Gtk.EventBox()
    pE3 = Gtk.EventBox()

    pbp2 = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/patreon.png'), 28, 28)
    pimage2 = Gtk.Image().new_from_pixbuf(pbp2)

    pbp3 = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/paypal.png'), 28, 28)
    pimage3 = Gtk.Image().new_from_pixbuf(pbp3)

    pE2.add(pimage2)
    pE3.add(pimage3)

    pE2.connect("button_press_event", self.on_social_clicked,
                "https://www.patreon.com/hefftor")

    pE3.connect("button_press_event", self.on_social_clicked,
                "https://streamlabs.com/bradheffernan1")

    pE2.set_property("has-tooltip", True)
    pE3.set_property("has-tooltip", True)

    pE2.connect("query-tooltip", self.tooltip_callback,
                "Support Brad on Patreon")
    pE3.connect("query-tooltip", self.tooltip_callback,
                "Buy Brad a coffee")

    hbox2.pack_start(pE2, False, False, 0)  # Patreon
    hbox2.pack_start(pE3, False, False, 0)  # Patreon

    # ==========================================================
    #                       STATUS
    # ==========================================================
    
    hbox5.pack_start(self.status, True, False, 0)

    # ==========================================================
    #                       RESOLUTION
    # ==========================================================
    self.res = Gtk.Entry()
    self.res.set_text("1920x1080")
    self.res.set_width_chars(True)
    self.res.set_size_request(100, 0)
    label = Gtk.Label("Resolution")
    hbox4.pack_start(label, False, False, 0)
    hbox4.pack_start(self.res, False, False, 0)

    hbox2.pack_start(hbox4, True, False, 0)

    # ==========================================================
    #                       RESOLUTION
    # ==========================================================
    self.blur = Gtk.Entry()
    self.blur.set_text("1.0")
    self.blur.set_max_length(4)
    self.blur.set_width_chars(True)
    self.blur.set_size_request(67, 0)
    label = Gtk.Label("Blur intensity")

    hbox7.pack_start(label, False, False, 0)
    hbox7.pack_start(self.blur, False, False, 0)

    hbox2.pack_start(hbox7, True, False, 0)

    # ==========================================================
    #                       PACK TO WINDOW
    # ==========================================================

    self.vbox.pack_start(hbox1, False, False, 0)
    self.vbox.pack_start(hbox6, False, False, 0)
    self.vbox.pack_start(self.hbox3, True, True, 0)
    self.vbox.pack_start(hbox5, False, False, 0)
    self.vbox.pack_end(hbox2, False, False, 0)  # Patreon
