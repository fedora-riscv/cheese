Name:           cheese
Version:        0.3.0
Release:        1%{?dist}
Summary:        A webcam application for snapshots and movies

Group:          Amusements/Graphics
License:        GPLv2+
URL:            http://live.gnome.org/Cheese
Source0:        http://download.gnome.org/sources/cheese/0.3/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gtk2-devel >= 2.10.0
BuildRequires: libglade2-devel >= 2.0.0
BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
BuildRequires: gstreamer-devel >= 0.10.12
BuildRequires: gstreamer-plugins-base-devel >= 0.10.12
BuildRequires: gnome-vfs2-devel
BuildRequires: GConf2-devel
BuildRequires: cairo-devel
BuildRequires: hal-devel
BuildRequires: libgnomeui-devel
BuildRequires: evolution-data-server-devel
BuildRequires: libXxf86vm-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext

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

%changelog
* Mon Dec 24 2007  Matthias Clasen  <mclasen@redhat.com> 0.3.0-1
- Update to 0.3.0

* Fri Sep  7 2007  Matthias Clasen  <mclasen@redhat.com> 0.2.4-2
- package review feedback

* Thu Sep  6 2007  Matthias Clasen  <mclasen@redhat.com> 0.2.4-1
- Initial packages
