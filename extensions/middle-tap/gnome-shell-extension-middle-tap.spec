%global debug_package %{nil}

Name:          gnome-shell-extension-middle-tap
Version:       0.1
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

Requires:      glib2
Requires:      mutter
Requires:      libinput

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
%{_libdir}/girepository-1.0/MiddleTap-1.0.typelib
%{_datarootdir}/gir-1.0/MiddleTap-1.0.gir
%{_datarootdir}/gnome-shell/extensions/MiddleTap@dmytr.github.io/*

%changelog
* Sat Nov 25 2017 dmytr 0.1-1
- Initial packaging
