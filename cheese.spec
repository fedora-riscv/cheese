Name:           cheese
Version:        2.21.91
Release:        2%{?dist}
Summary:        A webcam application for snapshots and movies

Group:          Amusements/Graphics
License:        GPLv2+
URL:            http://live.gnome.org/Cheese
Source0:        http://download.gnome.org/sources/cheese/2.21/%{name}-%{version}.tar.bz2
Source1:	cheese-bugreport.sh
Patch0:		libexecdir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gtk2-devel >= 2.10.0
BuildRequires: libglade2-devel >= 2.6.0
BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
BuildRequires: gstreamer-devel >= 0.10.15
BuildRequires: gstreamer-plugins-base-devel >= 0.10.12
BuildRequires: gnome-vfs2-devel
BuildRequires: GConf2-devel
BuildRequires: cairo-devel >= 1.2.4
BuildRequires: hal-devel >= 0.5.9
BuildRequires: libgnomeui-devel
BuildRequires: librsvg2-devel >= 2.18.0
BuildRequires: evolution-data-server-devel
BuildRequires: libXxf86vm-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: perl(XML::Parser)
BuildRequires: gnome-doc-utils
BuildRequires: autoconf, automake, libtool, intltool

Requires: gstreamer-plugins-good >= 0.10.6-2
Requires(post): GConf2
Requires(pre): GConf2
Requires(preun): GConf2 

%description
Cheese is a Photobooth-inspired GNOME application for taking pictures and 
videos from a webcam. It also includes fancy graphical effects based on the 
gstreamer-backend.

%prep
%setup -q
%patch0 -p1 -b .libexecdir
cp %{SOURCE1} data

autoreconf

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --delete-original --vendor="" 	\
 	--dir=$RPM_BUILD_ROOT%{_datadir}/applications 	\
	$RPM_BUILD_ROOT%{_datadir}/applications/cheese.desktop

%find_lang %{name} --with-gnome


%clean
rm -rf $RPM_BUILD_ROOT


%pre
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/cheese.schemas > /dev/null || :
fi


%preun
if [ "$1" -gt 0 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/cheese.schemas > /dev/null || :
fi


%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/cheese.schemas > /dev/null || :


%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi



%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/cheese
%{_datadir}/applications/cheese.desktop
%{_datadir}/cheese
%{_datadir}/icons/hicolor/*/apps/cheese.png
%{_datadir}/icons/hicolor/scalable/apps/cheese.svg
%{_sysconfdir}/gconf/schemas/cheese.schemas
%{_libexecdir}/cheese-bugreport.sh

%changelog
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
