#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : network-manager-applet
Version  : 1.4.6
Release  : 1
URL      : http://ftp.acc.umu.se/pub/gnome/sources/network-manager-applet/1.4/network-manager-applet-1.4.6.tar.xz
Source0  : http://ftp.acc.umu.se/pub/gnome/sources/network-manager-applet/1.4/network-manager-applet-1.4.6.tar.xz
Summary  : NetworkManager UI utilities (libnm-glib version)
Group    : Development/Tools
License  : GPL-2.0
Requires: network-manager-applet-bin
Requires: network-manager-applet-lib
Requires: network-manager-applet-data
Requires: network-manager-applet-doc
Requires: network-manager-applet-locales
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libsecret-unstable)
BuildRequires : pkgconfig(libxml-2.0)

%description


%package bin
Summary: bin components for the network-manager-applet package.
Group: Binaries
Requires: network-manager-applet-data

%description bin
bin components for the network-manager-applet package.


%package data
Summary: data components for the network-manager-applet package.
Group: Data

%description data
data components for the network-manager-applet package.


%package dev
Summary: dev components for the network-manager-applet package.
Group: Development
Requires: network-manager-applet-lib
Requires: network-manager-applet-bin
Requires: network-manager-applet-data
Provides: network-manager-applet-devel

%description dev
dev components for the network-manager-applet package.


%package doc
Summary: doc components for the network-manager-applet package.
Group: Documentation

%description doc
doc components for the network-manager-applet package.


%package lib
Summary: lib components for the network-manager-applet package.
Group: Libraries
Requires: network-manager-applet-data

%description lib
lib components for the network-manager-applet package.


%package locales
Summary: locales components for the network-manager-applet package.
Group: Default

%description locales
locales components for the network-manager-applet package.


%prep
%setup -q -n network-manager-applet-1.4.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493394535
%configure --disable-static --without-wwan --without-team
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1493394535
rm -rf %{buildroot}
%make_install
%find_lang nm-applet

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nm-applet
/usr/bin/nm-connection-editor

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/NMA-1.0.typelib
/usr/lib64/girepository-1.0/NMGtk-1.0.typelib
/usr/share/GConf/gsettings/nm-applet.convert
/usr/share/appdata/nm-connection-editor.appdata.xml
/usr/share/applications/nm-applet.desktop
/usr/share/applications/nm-connection-editor.desktop
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml
/usr/share/icons/hicolor/16x16/apps/nm-device-wired.png
/usr/share/icons/hicolor/16x16/apps/nm-no-connection.png
/usr/share/icons/hicolor/16x16/apps/nm-vpn-standalone-lock.png
/usr/share/icons/hicolor/22x22/apps/nm-adhoc.png
/usr/share/icons/hicolor/22x22/apps/nm-device-wired.png
/usr/share/icons/hicolor/22x22/apps/nm-device-wwan.png
/usr/share/icons/hicolor/22x22/apps/nm-mb-roam.png
/usr/share/icons/hicolor/22x22/apps/nm-no-connection.png
/usr/share/icons/hicolor/22x22/apps/nm-secure-lock.png
/usr/share/icons/hicolor/22x22/apps/nm-signal-00.png
/usr/share/icons/hicolor/22x22/apps/nm-signal-100.png
/usr/share/icons/hicolor/22x22/apps/nm-signal-25.png
/usr/share/icons/hicolor/22x22/apps/nm-signal-50.png
/usr/share/icons/hicolor/22x22/apps/nm-signal-75.png
/usr/share/icons/hicolor/22x22/apps/nm-stage01-connecting01.png
/usr/share/icons/hicolor/22x22/apps/nm-stage01-connecting02.png
/usr/share/icons/hicolor/22x22/apps/nm-stage01-connecting03.png
/usr/share/icons/hicolor/22x22/apps/nm-stage01-connecting04.png
/usr/share/icons/hicolor/22x22/apps/nm-stage01-connecting05.png
/usr/share/icons/hicolor/22x22/apps/nm-stage01-connecting06.png
/usr/share/icons/hicolor/22x22/apps/nm-stage01-connecting07.png
/usr/share/icons/hicolor/22x22/apps/nm-stage01-connecting08.png
/usr/share/icons/hicolor/22x22/apps/nm-stage01-connecting09.png
/usr/share/icons/hicolor/22x22/apps/nm-stage01-connecting10.png
/usr/share/icons/hicolor/22x22/apps/nm-stage01-connecting11.png
/usr/share/icons/hicolor/22x22/apps/nm-stage02-connecting01.png
/usr/share/icons/hicolor/22x22/apps/nm-stage02-connecting02.png
/usr/share/icons/hicolor/22x22/apps/nm-stage02-connecting03.png
/usr/share/icons/hicolor/22x22/apps/nm-stage02-connecting04.png
/usr/share/icons/hicolor/22x22/apps/nm-stage02-connecting05.png
/usr/share/icons/hicolor/22x22/apps/nm-stage02-connecting06.png
/usr/share/icons/hicolor/22x22/apps/nm-stage02-connecting07.png
/usr/share/icons/hicolor/22x22/apps/nm-stage02-connecting08.png
/usr/share/icons/hicolor/22x22/apps/nm-stage02-connecting09.png
/usr/share/icons/hicolor/22x22/apps/nm-stage02-connecting10.png
/usr/share/icons/hicolor/22x22/apps/nm-stage02-connecting11.png
/usr/share/icons/hicolor/22x22/apps/nm-stage03-connecting01.png
/usr/share/icons/hicolor/22x22/apps/nm-stage03-connecting02.png
/usr/share/icons/hicolor/22x22/apps/nm-stage03-connecting03.png
/usr/share/icons/hicolor/22x22/apps/nm-stage03-connecting04.png
/usr/share/icons/hicolor/22x22/apps/nm-stage03-connecting05.png
/usr/share/icons/hicolor/22x22/apps/nm-stage03-connecting06.png
/usr/share/icons/hicolor/22x22/apps/nm-stage03-connecting07.png
/usr/share/icons/hicolor/22x22/apps/nm-stage03-connecting08.png
/usr/share/icons/hicolor/22x22/apps/nm-stage03-connecting09.png
/usr/share/icons/hicolor/22x22/apps/nm-stage03-connecting10.png
/usr/share/icons/hicolor/22x22/apps/nm-stage03-connecting11.png
/usr/share/icons/hicolor/22x22/apps/nm-tech-3g.png
/usr/share/icons/hicolor/22x22/apps/nm-tech-cdma-1x.png
/usr/share/icons/hicolor/22x22/apps/nm-tech-edge.png
/usr/share/icons/hicolor/22x22/apps/nm-tech-evdo.png
/usr/share/icons/hicolor/22x22/apps/nm-tech-gprs.png
/usr/share/icons/hicolor/22x22/apps/nm-tech-hspa.png
/usr/share/icons/hicolor/22x22/apps/nm-tech-lte.png
/usr/share/icons/hicolor/22x22/apps/nm-tech-umts.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-active-lock.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-connecting01.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-connecting02.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-connecting03.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-connecting04.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-connecting05.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-connecting06.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-connecting07.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-connecting08.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-connecting09.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-connecting10.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-connecting11.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-connecting12.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-connecting13.png
/usr/share/icons/hicolor/22x22/apps/nm-vpn-connecting14.png
/usr/share/icons/hicolor/22x22/apps/nm-wwan-tower.png
/usr/share/icons/hicolor/32x32/apps/nm-device-wired.png
/usr/share/icons/hicolor/32x32/apps/nm-no-connection.png
/usr/share/icons/hicolor/48x48/apps/nm-device-wireless.png
/usr/share/icons/hicolor/scalable/apps/nm-device-wired.svg
/usr/share/icons/hicolor/scalable/apps/nm-no-connection.svg

%files dev
%defattr(-,root,root,-)
/usr/include/libnm-gtk/nm-mobile-providers.h
/usr/include/libnm-gtk/nm-mobile-wizard.h
/usr/include/libnm-gtk/nm-ui-utils.h
/usr/include/libnm-gtk/nm-vpn-password-dialog.h
/usr/include/libnm-gtk/nm-wifi-dialog.h
/usr/include/libnm-gtk/nm-wireless-dialog.h
/usr/include/libnma/nma-mobile-providers.h
/usr/include/libnma/nma-mobile-wizard.h
/usr/include/libnma/nma-ui-utils.h
/usr/include/libnma/nma-vpn-password-dialog.h
/usr/include/libnma/nma-wifi-dialog.h
/usr/lib64/libnm-gtk.so
/usr/lib64/libnma.so
/usr/lib64/pkgconfig/libnm-gtk.pc
/usr/lib64/pkgconfig/libnma.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
/usr/share/gtk-doc/html/libnma/NMAMobileProvidersDatabase.html
/usr/share/gtk-doc/html/libnma/NMAVpnPasswordDialog.html
/usr/share/gtk-doc/html/libnma/NMAWifiDialog.html
/usr/share/gtk-doc/html/libnma/annotation-glossary.html
/usr/share/gtk-doc/html/libnma/api-index-full.html
/usr/share/gtk-doc/html/libnma/api-reference.html
/usr/share/gtk-doc/html/libnma/deprecated-api-index.html
/usr/share/gtk-doc/html/libnma/home.png
/usr/share/gtk-doc/html/libnma/index.html
/usr/share/gtk-doc/html/libnma/left-insensitive.png
/usr/share/gtk-doc/html/libnma/left.png
/usr/share/gtk-doc/html/libnma/libnma-nma-mobile-wizard.html
/usr/share/gtk-doc/html/libnma/libnma-nma-ui-utils.html
/usr/share/gtk-doc/html/libnma/libnma.devhelp2
/usr/share/gtk-doc/html/libnma/object-tree.html
/usr/share/gtk-doc/html/libnma/right-insensitive.png
/usr/share/gtk-doc/html/libnma/right.png
/usr/share/gtk-doc/html/libnma/style.css
/usr/share/gtk-doc/html/libnma/up-insensitive.png
/usr/share/gtk-doc/html/libnma/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnm-gtk.so.0
/usr/lib64/libnm-gtk.so.0.0.0
/usr/lib64/libnma.so.0
/usr/lib64/libnma.so.0.0.0

%files locales -f nm-applet.lang
%defattr(-,root,root,-)

