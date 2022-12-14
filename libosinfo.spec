# -*- rpm-spec -*-

Summary: A library for managing OS information for virtualization
Name: libosinfo
Version: 1.8.0
Release: 1%{?dist}
License: LGPLv2+
Source: https://releases.pagure.org/%{name}/%{name}-%{version}.tar.xz
URL: https://libosinfo.org/
BuildRequires: meson
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: glib2-devel
BuildRequires: libxml2-devel >= 2.6.0
BuildRequires: libxslt-devel >= 1.0.0
BuildRequires: libsoup-devel
BuildRequires: vala
BuildRequires: /usr/bin/pod2man
BuildRequires: hwdata
BuildRequires: gobject-introspection-devel
BuildRequires: osinfo-db
Requires: hwdata
Requires: osinfo-db
Requires: osinfo-db-tools

%description
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

%package devel
Summary: Libraries, includes, etc. to compile with the libosinfo library
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: glib2-devel
# -vala subpackage removed in F30
Obsoletes: libosinfo-vala < 1.3.0-3
Provides: libosinfo-vala = %{version}-%{release}

%description devel
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

Libraries, includes, etc. to compile with the libosinfo library

%prep
%setup -q

%build
%meson \
    -Denable-gtk-doc=true \
    -Denable-tests=true \
    -Denable-introspection=enabled \
    -Denable-vala=enabled

%install
%meson_install

%find_lang %{name}

%check
%meson_test

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING.LIB NEWS README
%{_bindir}/osinfo-detect
%{_bindir}/osinfo-query
%{_bindir}/osinfo-install-script
%{_mandir}/man1/osinfo-detect.1*
%{_mandir}/man1/osinfo-query.1*
%{_mandir}/man1/osinfo-install-script.1*
%{_libdir}/%{name}-1.0.so.*
%{_libdir}/girepository-1.0/Libosinfo-1.0.typelib

%files devel
%{_libdir}/%{name}-1.0.so
%dir %{_includedir}/%{name}-1.0/
%dir %{_includedir}/%{name}-1.0/osinfo/
%{_includedir}/%{name}-1.0/osinfo/*.h
%{_libdir}/pkgconfig/%{name}-1.0.pc
%{_datadir}/gir-1.0/Libosinfo-1.0.gir
%{_datadir}/gtk-doc/html/Libosinfo

%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libosinfo-1.0.deps
%{_datadir}/vala/vapi/libosinfo-1.0.vapi

%changelog
