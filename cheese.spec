Name:           cheese
Epoch:          2
Version:        3.8.2
Release:        4%{?dist}
Summary:        Application for taking pictures and movies from a webcam

Group:          Amusements/Graphics
License:        GPLv2+
URL:            http://projects.gnome.org/cheese/
#VCS: git:git://git.gnome.org/cheese
Source0:        http://download.gnome.org/sources/cheese/3.8/%{name}-%{version}.tar.xz

# HdG: since I hit a couple of issues in cheese, and cheese needed some loving
# in general I ended up doing a whole lot of *bugfix* patches for cheese,
# fixing various performance / device compatibility issues, but also things
# like needing to press some buttons twice before they work, etc.
# See here for a bug for tracking the upstreaming of this patchset:
# https://bugzilla.gnome.org/show_bug.cgi?id=702264
Patch1:         0001-cheese-camera-Add-a-capsfilter-to-our-video-source-b.patch
Patch2:         0002-cheese-camera-remove-extranous-csp_post_balance-vide.patch
Patch3:         0003-cheese-camera-Set-image-and-video-capture-caps.patch
Patch4:         0004-cheese-camera-Fix-the-no-video-after-switching-resol.patch
Patch5:         0005-cheese-camera-2-minor-error-handling-cleanups.patch
Patch6:         0006-cheese-camera-Fix-video-source-memleak-when-switchin.patch
Patch7:         0007-cheese-camera-Remove-unused-enum.patch
Patch8:         0008-cheese-camera-device-Fix-compiler-warning.patch
Patch9:         0009-cheese-camera-device-Fix-memleak-in-get_best_format.patch
Patch10:        0010-cheese-camera-device-Keep-track-of-highest-available.patch
Patch11:        0011-cheese-camera-device-Add-cheese_camera_device_find_f.patch
Patch12:        0012-cheese-camera-device-limit-caps-to-the-maximum-frame.patch
Patch13:        0013-cheese-camera-device-get_caps_for_format-simplify-th.patch
Patch14:        0014-cheese-camera-device-Make-get_best_format-smarter.patch
Patch15:        0015-cheese-camera-device-Plug-some-memory-leaks.patch
Patch16:        0016-cheese-camera-Drop-unused-preview_caps.patch
Patch17:        0017-cheese-camera-Do-not-add-videoconvert-elements-aroun.patch
Patch18:        0018-cheese-camera-Check-for-the-current-effect-being-the.patch
Patch19:        0019-cheese-camera-Don-t-block-the-main-valve-while-recor.patch
Patch20:        0020-cheese-camera-Downscale-image-for-effects-preview-pi.patch
Patch21:        0021-cheese-window-Fix-de-activation-of-effects-button.patch
Patch22:        0022-cheese-window-Make-mode-toggle-and-effects-button-in.patch
Patch23:        0023-libcheese-Add-_init_with_args-init-function-variants.patch
Patch24:        0024-cheese-Use-cheese_gtk_init_with_args.patch
Patch25:        0025-cheese-Remove-last-remnants-of-the-old-menu-code.patch
Patch26:        0026-cheese-Protect-set_wide_mode-set_fullscreen-against-.patch
Patch27:        0027-cheese-Get-rid-of-special-set_startup_foo-functions.patch
Patch28:        0028-cheese-Fix-the-need-to-press-F11-twice-after-startin.patch
Patch29:        0029-cheese-Make-widemode-controllable-from-the-app-menu.patch
Patch30:        0030-cheese-Move-reading-of-widemode-setting-to-cheese-ma.patch
Patch31:        0031-cheese-Fix-reading-of-fullscreen-setting-from-config.patch
Patch32:        0032-cheese-Don-t-show-thumbnails-when-toggling-widemode-.patch
Patch33:        0033-cheese-Fix-updating-of-device-selection-combo-sensit.patch
Patch34:        0034-cheese-Fix-assert-failures-when-taking-a-photo.patch
Patch35:        0035-cheese-flash-Fix-the-flash-no-longer-being-white.patch
Patch36:        0036-cheese-camera-Set-the-effects-valve-to-closed-when-c.patch
Patch37:        0037-cheese-Move-disabling-of-shoot-button-to-cheese-wind.patch
Patch38:        0038-cheese-Use-shoot-action-for-webcam-button.patch
Patch39:        0039-cheese-window-Add-cancel_running_action-method.patch
Patch40:        0040-cheese-window-Fix-toggle_camera_actions_sensitivitie.patch
Patch41:        0041-cheese-window-Add-show_error-method.patch
Patch42:        0042-cheese-preferences-Add-camera_changed-method.patch
Patch43:        0043-cheese_camera_get_camera_devices-Allow-calling-befor.patch
Patch44:        0044-cheese-Move-camera_setup-to-cheese-preferences.patch
Patch45:        0045-cheese-Properly-deal-with-going-from-0-1-devices.patch
Patch46:        0046-cheese-Avoid-unnecessary-calls-to-switch_camera_devi.patch
Patch47:        0047-on_camera_update_num_camera_devices-Remove-unnecessa.patch
Patch48:        0048-cheese-preferences-Simplify-remove_camera_device.patch
Patch49:        0049-cheese-preferences-Cleanly-handle-going-from-1-0-dev.patch
Patch50:        0050-cheese-Don-t-allow-changing-the-camera-and-or-its-re.patch
Patch51:        0051-cheese-Leave-shoot-button-disabled-when-the-effects-.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=678447
# Patch2: 0002-Setup-vp8enc-in-a-way-suitable-for-realtime-encoding.patch

BuildRequires: gtk3-devel >= 3.0.0
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-bad-free-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: cairo-devel >= 1.4.0
BuildRequires: librsvg2-devel >= 2.18.0
BuildRequires: evolution-data-server-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXtst-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: libgudev1-devel
BuildRequires: libcanberra-devel
BuildRequires: clutter-devel
BuildRequires: clutter-gtk-devel
BuildRequires: clutter-gst2-devel
BuildRequires: libmx-devel
BuildRequires: vala-devel
BuildRequires: pkgconfig(gee-1.0)
BuildRequires: gnome-video-effects
BuildRequires: gnome-desktop3-devel
BuildRequires: chrpath
BuildRequires: itstool
# 3.8.2 tarball misses man page
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: /usr/bin/convert

Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: gstreamer1-plugins-good
Requires: gstreamer1-plugins-bad-free
Requires: gnome-video-effects

%description
Cheese is a Photobooth-inspired GNOME application for taking pictures and
videos from a webcam. It can also apply fancy graphical effects.

%package libs
Summary:        Webcam display and capture widgets
Group:          System Environment/Libraries
License:        GPLv2+

%description libs
This package contains libraries needed for applications that
want to display a webcam in their interface.

%package libs-devel
Summary:        Development files for %{name}-libs
Group:          Development/Libraries
License:        GPLv2+
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description libs-devel
This package contains the libraries and header files that are needed
for writing applications that require a webcam display widget.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1


%build
%configure --disable-static --enable-man
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libcheese.{a,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/libcheese-gtk.{a,la}

desktop-file-install --delete-original --vendor=""    \
    --dir=$RPM_BUILD_ROOT%{_datadir}/applications     \
    --add-category X-AudioVideoImport                 \
    $RPM_BUILD_ROOT%{_datadir}/applications/cheese.desktop

%find_lang %{name} --with-gnome

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/cheese
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libcheese-gtk.so.*

# hack to conserve space on the live image
convert $RPM_BUILD_ROOT%{_datadir}/help/C/cheese/figures/effects.png -resize 850x320 effects.png
mv effects.png $RPM_BUILD_ROOT%{_datadir}/help/C/cheese/figures/effects.png

%post
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :


%postun
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :

%post libs
/sbin/ldconfig
if [ $1 -eq 1 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%postun libs
/sbin/ldconfig
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files
%doc AUTHORS README
%{_bindir}/cheese
%{_datadir}/applications/cheese.desktop
%{_datadir}/cheese
%{_datadir}/icons/hicolor/*/apps/cheese.png
%{_datadir}/icons/hicolor/*/actions/*.png
%{_datadir}/icons/hicolor/scalable/actions/*.svg
%{_mandir}/man1/cheese.1.gz

%files -f %{name}.lang libs
%doc COPYING
%{_libdir}/libcheese.so.*
%{_libdir}/libcheese-gtk.so.*
%{_datadir}/glib-2.0/schemas/org.gnome.Cheese.gschema.xml
%{_libdir}/girepository-1.0/Cheese-3.0.typelib

%files libs-devel
%{_libdir}/libcheese.so
%{_libdir}/libcheese-gtk.so
%{_includedir}/cheese/
%{_datadir}/gtk-doc/
%{_libdir}/pkgconfig/cheese.pc
%{_libdir}/pkgconfig/cheese-gtk.pc
%{_datadir}/gir-1.0/Cheese-3.0.gir

%changelog
* Thu Jun 20 2013 Hans de Goede <hdegoede@redhat.com> - 2:3.8.2-4
- Fix misbehavior when started without a camera
- Don't crash when the (last) camera gets unplugged
- Automatically use a newly plugged camera when going from 0 to 1 cameras
- Misc. other bugfixes

* Mon Jun 17 2013 Hans de Goede <hdegoede@redhat.com> - 2:3.8.2-3
- Add a number of bug-fixes to deal better with high res cams (#873434)
- Fix cheese-introduction.png being in both cheese and cheese-libs (#893756)
- Put the COPYING file in the docs for cheese-libs (#893800)
- Fix the flash when taking a photo being dark grey instead of white (#965813)
- Fix needing to press the effects button twice to select effects after
  selecting an effect for the first time
- Various other bug-fixes

* Tue May 14 2013 Matthias Clasen <mclasen@redhat.com> - 2:3.8.2-2
- Conserve space by shrinking images

* Mon May 13 2013 Matthias Clasen <mclasen@redhat.com> - 2:3.8.2-1
- Update to 3.8.2

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.7.92-2
- Rebuilt for clutter-gtk soname bump

* Wed Mar 20 2013 Richard Hughes <rhughes@redhat.com> - 2:3.7.92-1
- Update to 3.7.92

* Wed Mar  6 2013 Matthias Clasen <mclasen@redhat.com> - 2:3.7.91-1
- Update to 3.7.91

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.7.90-3
- Rebuilt for cogl soname bump

* Wed Feb 20 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.7.90-2
- Rebuilt for libgnome-desktop soname bump

* Tue Feb 19 2013 Richard Hughes <rhughes@redhat.com> - 2:3.7.90-1
- Update to 3.7.90

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2:3.7.4-2
- Rebuild for new cogl

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 2:3.7.4-1
- Update to 3.7.4

* Thu Dec 20 2012 Kalev Lember <kalevlember@gmail.com> - 2:3.7.3-1
- Update to 3.7.3

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 2:3.6.2-1
- Update to 3.6.2

* Wed Oct 17 2012 Kalev Lember <kalevlember@gmail.com> - 2:3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Richard Hughes <hughsient@gmail.com> - 2:3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 2:3.5.92-1
- Update to 3.5.92

* Thu Sep  6 2012 Matthias Clasen <mclasen@redhat.com> - 2:3.5.91-1
- Update to 3.5.91
- Drop upstreamed patches

* Tue Aug 28 2012 Matthias Clasen <mclasen@redhat.com> - 2:3.5.5-2
- Rebuild against new cogl/clutter

* Wed Aug 22 2012 Hans de Goede <hdegoede@redhat.com> - 2:3.5.5-1
- New upstream release 3.5.5
- Fix cheese crashing on tvcards which report they can capture 0x0 as
  minimum resolution (rhbz#850505)

* Tue Aug 21 2012 Brian Pepple <bpepple@fedoraproject.org> - 2:3.5.2-6
- Rebuild for new libcogl.

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Hans de Goede <hdegoede@redhat.com> - 2:3.4.2-3
- Reduce camerabin pipeline creation time (rhbz#797188, gnome#677731)
- Don't add 0 byte sized files to the thumb-view (rhbz#830166, gnome#677735)
- Fix sizing of horizontal thumbnail list (rhbz#829957)
- Optimize encoding parameters (rhbz#572169)

* Wed Jun 13 2012 Owen Taylor <otaylor@redhat.com> - 2:3.5.2-3
- Require matching version of cheese-libs for cheese

* Thu Jun 07 2012 Matthias Clasen <mclasen@redhat.com> - 2:3.5.2-2
- Rebuild against new gnome-desktop

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 2:3.5.2-1
- Update to 3.5.2

* Tue Jun  5 2012 Hans de Goede <hdegoede@redhat.com> - 2:3.5.1-2
- Fix missing images on buttons, also fixes the "Gtk-WARNING **: Attempting to
  add a widget with type GtkImage to a GtkButton ..." warnings (gnome#677543)
- Fix cheese crashing when started on machines with v4l2 radio or vbi devices
  (rhbz#810429, gnome#677544)

* Sun May 06 2012 Kalev Lember <kalevlember@gmail.com> - 2:3.5.1-1
- Update to 3.5.1

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 2:3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 2:3.4.0-1
- Update to 3.4.0

* Wed Mar 14 2012 Brian Pepple <bpepple@fedoraproject.org> - 2:3.3.5-2
- Rebuild for new cogl

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 2:3.3.5-1
- Update to 3.3.5

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 2:3.3.4-1
- Update to 3.3.4

* Mon Jan 16 2012 Matthias Clasen <mclasen@redhat.com> - 2:3.3.3-3
- Add a BuildRequires for itstool

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Matthias Clasen <mclasen@redhat.com> - 2:3.3.3-1
- Update to 3.3.3

* Thu Nov 24 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.3.2-2
- Rebuild against new clutter

* Tue Nov 22 2011 Tomas Bzatek <tbzatek@redhat.com> - 1:3.3.2-1
- Update to 3.3.2

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.3.1-1
- Update to 3.3.1-1

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.1-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.2.1-1
- Update to 3.2.1

* Thu Sep 29 2011 Hans de Goede <hdegoede@redhat.com> - 1:3.2.0-2
- Add Requires: gstreamer-plugins-bad-free for the camerabin element (#717872)

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 1:3.2.0-1
- Update to 3.2.0

* Wed Sep 21 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:3.1.92-2
- Rebuld for new libcogl.
- Use old libgee api.

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.1.92-1
- Update to 3.1.92

* Tue Sep  6 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.1.91.1-1
- Update to 3.1.91.1

* Tue Jul 26 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.0.2-2
- Rebuild

* Mon Jul 25 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.0.2-1
- Update to 3.0.2

* Wed Jun 29 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1:3.0.1-3
- Removed RPATHS (RH #703636)

* Wed Jun 15 2011 Bastien Nocera <bnocera@redhat.com> 3.0.1-2
- Rebuild against newest gnome-desktop3

* Tue Apr 26 2011 Matthias Clasen <mclasen@redhat.com> 1:3.0.1-1
- Update to 3.0.1

* Tue Apr  5 2011 Matthias Clasen <mclasen@redhat.com> 1:3.0.0-2
- Add newer icons from upstream

* Mon Apr  4 2011 Christopher Aillon <caillon@redhat.com> 1:3.0.0-1
- Update to 3.0

* Wed Mar 30 2011 Alexander Larsson <alexl@redhat.com> - 1:2.91.93-3
- Move gsettings schema to cheese-libs, fixes control-center crash (#691667)
- Move typelib to cheese-libs

* Mon Mar 28 2011 Bastien Nocera <bnocera@redhat.com> 2.91.93-2
- Add missing gnome-video-effects dependency

* Fri Mar 25 2011 Bastien Nocera <bnocera@redhat.com> 2.91.93-1
- Update to 2.91.93

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> 1:2.91.92-1
- Update to 2.91.92

* Sat Mar 12 2011 Bastien Nocera <bnocera@redhat.com> 2.91.91.1-1
- Update to 2.91.91.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.91.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Christopher Aillon <caillon@redhat.com> 1:2.91.4-1
- Update to 2.91.4

* Mon Jan 10 2011 Matthias Clasen <mclasen@redhat.com> 1:2.91.3-1
- Update to 2.91.3

* Thu Sep 30 2010 Matthias Clasen <mclasen@redhat.com> 1:2.32.0-1
- Update to 2.32.0

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> 1:2.31.91-1
- Update to 2.31.91

* Mon Aug 23 2010 Matthias Clasen <mclasen@redhat.com> 1:2.31.90-2
- Co-own /usr/share/gtk-doc

* Thu Aug 19 2010 Matthias Clasen <mclasen@redhat.com> 1:2.31.90-1
- Update to 2.31.90

* Wed Aug 11 2010 Matthias Clasen <mclasen@redhat.com> 1:2.31.1-2
- Add an epoch to stay ahead of F14

* Fri Aug  6 2010 Matthias Clasen <mclasen@redhat.com> 2.31.1-1
- Update to 2.31.1

* Tue Apr 27 2010 Matthias Clasen <mclasen@redhat.com> 2.30.1-1
- Update to 2.30.1
- Spec file cleanups

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> 2.30.0-1
- Update to 2.30.0

* Wed Mar 24 2010 Bastien Nocera <bnocera@redhat.com> 2.29.92-4
- Fix possible crasher when countdown reaches zero

* Fri Mar 19 2010 Matthias Clasen <mclasen@redhat.com> 2.29.92-3
- Fix text rendering issues on the effects tab

* Tue Mar 16 2010 Matthias Clasen <mclasen@redhat.com> 2.29.92-2
- Use an existing icon

* Tue Mar 09 2010 Bastien Nocera <bnocera@redhat.com> 2.29.92-1
- Update to 2.29.92

* Tue Feb 09 2010 Bastien Nocera <bnocera@redhat.com> 2.29.90-2
- Fix include path, and missing requires for the pkg-config file

* Tue Feb 09 2010 Bastien Nocera <bnocera@redhat.com> 2.29.90-1
- Update to 2.29.90

* Sun Jan 17 2010 Matthias Clasen  <mclasen@redhat.com> 2.29.5-2
- Rebuild

* Tue Jan 12 2010 Matthias Clasen  <mclasen@redhat.com> 2.29.5-1
- Update to 2.29.5

* Sun Sep 27 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 2.28.0-2
- Update desktop file according to F-12 FedoraStudio feature

* Mon Sep 21 2009 Matthias Clasen  <mclasen@redhat.com> 2.28.0-1
- Update to 2.28.0

* Mon Sep  7 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.92-1
- Update to 2.27.92

* Mon Aug 24 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.91-1
- Update to 2.27.91

* Sat Aug 22 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.90-3
- Update sensitivity of menu items

* Fri Aug 14 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.90-2
- Fix schemas file syntax

* Tue Aug 11 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.90-1
- Update to 2.27.90

* Tue Jul 28 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.5-1
- Update to 2.27.5

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.4-1
- Update to 2.27.4

* Tue Jun 16 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.3-1
- Update to 2.27.3

* Sun May 31 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.2-1
- Update to 2.27.2

* Fri May 15 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.1-1
- Update to 2.27.1

* Mon Mar 16 2009 Matthias Clasen  <mclasen@redhat.com> 2.26.0-1
- Update to 2.26.0

* Mon Mar  2 2009 Matthias Clasen  <mclasen@redhat.com> 2.25.92-1
- Update to 2.25.92

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Matthias Clasen  <mclasen@redhat.com> 2.25.91-1
- Update to 2.25.91

* Tue Feb  3 2009 Matthias Clasen  <mclasen@redhat.com> 2.25.90-1
- Update to 2.25.90

* Tue Jan  6 2009 Matthias Clasen  <mclasen@redhat.com> 2.25.4-1
- Update to 2.25.4

* Wed Dec 17 2008 Matthias Clasen  <mclasen@redhat.com> 2.25.3-1
- Update to 2.25.3

* Wed Dec  3 2008 Matthias Clasen  <mclasen@redhat.com> 2.25.2-1
- Update to 2.25.2

* Fri Nov 21 2008 Matthias Clasen  <mclasen@redhat.com> 2.25.1-4
- Better URL

* Thu Nov 13 2008 Matthias Clasen  <mclasen@redhat.com> 2.25.1-3
- Update to 2.25.1

* Sun Nov  9 2008 Hans de Goede <hdegoede@redhat.com> 2.24.1-2
- Fix cams which only support 1 resolution not working (rh470698, gnome560032)

* Mon Oct 20 2008 Matthias Clasen  <mclasen@redhat.com> 2.24.1-1
- Update to 2.24.1

* Wed Oct  8 2008 Matthias Clasen  <mclasen@redhat.com> 2.24.0-2
- Save space

* Mon Sep 22 2008 Matthias Clasen  <mclasen@redhat.com> 2.24.0-1
- Update to 2.24.0

* Tue Sep  9 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.92-3
- Update to 2.23.92
- Drop upstreamed patches

* Wed Sep  3 2008 Hans de Goede <hdegoede@redhat.com> 2.23.91-2
- Fix use with multiple v4l devices (rh 460956, gnome 546868, gnome 547144)

* Tue Sep  2 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.91-1
- Update to 2.23.91

* Fri Aug 22 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.90-1
- Update to 2.23.90

* Tue Aug  5 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.6-1
- Update to 2.23.6

* Tue Jul 22 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.5-1
- Update to 2.23.5

* Wed Jun 18 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.4-1
- Update to 2.23.4

* Tue Jun  3 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.3-1
- Update to 2.23.3

* Tue May 13 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.2-1
- Update to 2.23.2

* Fri Apr 25 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.1-1
- Update to 2.23.1

* Tue Apr 22 2008 Matthias Clasen  <mclasen@redhat.com> 2.22.1-2
- Fix an invalid free

* Mon Apr  7 2008 Matthias Clasen  <mclasen@redhat.com> 2.22.1-1
- Update to 2.22.1

* Mon Mar 10 2008 Matthias Clasen  <mclasen@redhat.com> 2.22.0-1
- Update to 2.22.0

* Tue Feb 26 2008  Matthias Clasen  <mclasen@redhat.com> 2.21.92-1
- Update to 2.21.92

* Fri Feb 15 2008  Matthias Clasen  <mclasen@redhat.com> 2.21.91-3
- Fix a locking problem that causes the UI to freeze

* Fri Feb  8 2008  Matthias Clasen  <mclasen@redhat.com> 2.21.91-2
- Rebuild for gcc 4.3

* Tue Jan 29 2008  Matthias Clasen  <mclasen@redhat.com> 2.21.91-1
- Update to 2.21.91

* Mon Jan 14 2008  Matthias Clasen  <mclasen@redhat.com> 2.21.5-1
- Update to 2.21.5

* Mon Dec 24 2007  Matthias Clasen  <mclasen@redhat.com> 0.3.0-1
- Update to 0.3.0

* Fri Sep  7 2007  Matthias Clasen  <mclasen@redhat.com> 0.2.4-2
- package review feedback

* Thu Sep  6 2007  Matthias Clasen  <mclasen@redhat.com> 0.2.4-1
- Initial packages
