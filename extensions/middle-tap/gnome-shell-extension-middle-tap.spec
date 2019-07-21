%global debug_package %{nil}

Name:          gnome-shell-extension-middle-tap
Version:       0.4
Release:       1%{?dist}
Summary:       GNOME Shell extension which makes "tap with two fingers" work as a middle click

License:       MIT
URL:           https://github.com/dmytr/middle-tap
Source0:       https://codeload.github.com/dmytr/middle-tap/tar.gz/v%{version}#/middle-tap-%{version}.tar.gz

BuildRequires: meson
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: mutter-devel
BuildRequires: libinput-devel
BuildRequires: systemd-devel

Requires:      glib2
Requires:      mutter
Requires:      libinput
Requires:      systemd

%description
GNOME Shell extension which makes "tap with two fingers" work as a middle click

%prep
%autosetup -n middle-tap-%{version} 

%build
%meson
%meson_build

%install
%meson_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/libmiddletap.so
%{_libdir}/girepository-1.0/MiddleTap-%{version}.typelib
%{_datarootdir}/gir-1.0/MiddleTap-%{version}.gir
%{_datarootdir}/gnome-shell/extensions/MiddleTap@dmytr.github.io/*

%changelog
* Sun Jul 21 2019 dmytr 0.4-1
- New version with GNOME Shell 3.32.2 (Fedora 30) support
* Tue Nov 27 2018 dmytr 0.3-1
- New version with GNOME Shell 3.30.2 (Fedora 29) support
* Sun May 06 2018 dmytr 0.2-1
- New version with Fedora 28 support
* Sat Nov 25 2017 dmytr 0.1-1
- Initial packaging
