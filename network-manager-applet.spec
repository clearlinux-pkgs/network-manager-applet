#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v2
# autospec commit: 250a666
#
Name     : network-manager-applet
Version  : 1.34.0
Release  : 43
URL      : https://download.gnome.org/sources/network-manager-applet/1.34/network-manager-applet-1.34.0.tar.xz
Source0  : https://download.gnome.org/sources/network-manager-applet/1.34/network-manager-applet-1.34.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: network-manager-applet-bin = %{version}-%{release}
Requires: network-manager-applet-data = %{version}-%{release}
Requires: network-manager-applet-license = %{version}-%{release}
Requires: network-manager-applet-locales = %{version}-%{release}
Requires: network-manager-applet-man = %{version}-%{release}
Requires: NetworkManager
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gmodule-export-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(jansson)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(libnma)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(mm-glib)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description


%package bin
Summary: bin components for the network-manager-applet package.
Group: Binaries
Requires: network-manager-applet-data = %{version}-%{release}
Requires: network-manager-applet-license = %{version}-%{release}

%description bin
bin components for the network-manager-applet package.


%package data
Summary: data components for the network-manager-applet package.
Group: Data

%description data
data components for the network-manager-applet package.


%package license
Summary: license components for the network-manager-applet package.
Group: Default

%description license
license components for the network-manager-applet package.


%package locales
Summary: locales components for the network-manager-applet package.
Group: Default

%description locales
locales components for the network-manager-applet package.


%package man
Summary: man components for the network-manager-applet package.
Group: Default

%description man
man components for the network-manager-applet package.


%prep
%setup -q -n network-manager-applet-1.34.0
cd %{_builddir}/network-manager-applet-1.34.0
pushd ..
cp -a network-manager-applet-1.34.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697839263
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static --without-team --without-selinux --without-appindicator
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%configure --disable-static --without-team --without-selinux --without-appindicator
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697839263
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/network-manager-applet
cp %{_builddir}/network-manager-applet-%{version}/COPYING %{buildroot}/usr/share/package-licenses/network-manager-applet/4cc77b90af91e615a64ae04893fdffa7939db84c || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang nm-applet
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/nm-applet
/V3/usr/bin/nm-connection-editor
/usr/bin/nm-applet
/usr/bin/nm-connection-editor

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/nm-applet.convert
/usr/share/applications/nm-applet.desktop
/usr/share/applications/nm-connection-editor.desktop
/usr/share/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml
/usr/share/icons/hicolor/16x16/apps/nm-device-wired.png
/usr/share/icons/hicolor/16x16/apps/nm-no-connection.png
/usr/share/icons/hicolor/16x16/apps/nm-vpn-standalone-lock.png
/usr/share/icons/hicolor/22x22/apps/nm-adhoc.png
/usr/share/icons/hicolor/22x22/apps/nm-device-wired-secure.png
/usr/share/icons/hicolor/22x22/apps/nm-device-wired.png
/usr/share/icons/hicolor/22x22/apps/nm-device-wwan.png
/usr/share/icons/hicolor/22x22/apps/nm-insecure-warn.png
/usr/share/icons/hicolor/22x22/apps/nm-mb-roam.png
/usr/share/icons/hicolor/22x22/apps/nm-no-connection.png
/usr/share/icons/hicolor/22x22/apps/nm-secure-lock.png
/usr/share/icons/hicolor/22x22/apps/nm-signal-00-secure.png
/usr/share/icons/hicolor/22x22/apps/nm-signal-00.png
/usr/share/icons/hicolor/22x22/apps/nm-signal-100-secure.png
/usr/share/icons/hicolor/22x22/apps/nm-signal-100.png
/usr/share/icons/hicolor/22x22/apps/nm-signal-25-secure.png
/usr/share/icons/hicolor/22x22/apps/nm-signal-25.png
/usr/share/icons/hicolor/22x22/apps/nm-signal-50-secure.png
/usr/share/icons/hicolor/22x22/apps/nm-signal-50.png
/usr/share/icons/hicolor/22x22/apps/nm-signal-75-secure.png
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
/usr/share/icons/hicolor/scalable/apps/nm-device-wired-secure-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-device-wired-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-device-wired.svg
/usr/share/icons/hicolor/scalable/apps/nm-device-wwan-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-no-connection-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-no-connection.svg
/usr/share/icons/hicolor/scalable/apps/nm-signal-00-secure-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-signal-00-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-signal-100-secure-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-signal-100-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-signal-25-secure-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-signal-25-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-signal-50-secure-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-signal-50-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-signal-75-secure-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-signal-75-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-active-lock-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-connecting01-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-connecting02-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-connecting03-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-connecting04-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-connecting05-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-connecting06-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-connecting07-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-connecting08-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-connecting09-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-connecting10-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-connecting11-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-connecting12-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-connecting13-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-connecting14-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/nm-vpn-standalone-lock-symbolic.svg
/usr/share/metainfo/nm-connection-editor.appdata.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/network-manager-applet/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/nm-applet.1
/usr/share/man/man1/nm-connection-editor.1

%files locales -f nm-applet.lang
%defattr(-,root,root,-)

