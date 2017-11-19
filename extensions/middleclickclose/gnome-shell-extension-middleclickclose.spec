%global debug_package %{nil}

Name:          gnome-shell-extension-middleclickclose
Version:       1.1.1
Release:       1%{?dist}
Summary:       Gnome shell extension for closing apps in overview with a middle click

License:       GPL-2.0
URL:           https://github.com/p91paul/middleclickclose
Source0:       https://codeload.github.com/p91paul/middleclickclose/tar.gz/v%{version}#/middleclickclose-%{version}.tar.gz

BuildRequires: glib2

%description
Gnome shell extension for closing apps in overview with a middle click

%prep
%autosetup -n middleclickclose-%{version} 

%build
glib-compile-schemas middleclickclose@paolo.tranquilli.gmail.com/schemas

%install
mkdir -p %{buildroot}%{_datarootdir}/gnome-shell/extensions/
cp -r middleclickclose@paolo.tranquilli.gmail.com %{buildroot}%{_datarootdir}/gnome-shell/extensions/

%files
%license LICENSE
%doc     README.md
%{_datarootdir}/gnome-shell/extensions/middleclickclose@paolo.tranquilli.gmail.com/*

%changelog
* Sun Nov 19 2017 dmytr 1.1.1-1
- New version
* Fri Oct 20 2017 dmytr 1.1-1
- Initial packaging

