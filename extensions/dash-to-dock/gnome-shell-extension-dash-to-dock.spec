%global debug_package %{nil}

Name:          gnome-shell-extension-dash-to-dock
Version:       63	
Release:       1%{?dist}
Summary:       A dock for the Gnome Shell

License:       GPL-2.0
URL:           https://github.com/micheleg/dash-to-dock
Source0:       https://codeload.github.com/micheleg/dash-to-dock/tar.gz/extensions.gnome.org-v%{version}#/dash-to-dock-%{version}.tar.gz

BuildRequires: glib2
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: zip

%description
A dock for the Gnome Shell. This extension moves the dash out of the overview 
transforming it in a dock for an easier launching of applications and a faster 
switching between windows and desktops.

%prep
%autosetup -n dash-to-dock-extensions.gnome.org-v%{version} 

%build
%make_build

%install
%make_install

%files
%license COPYING
%doc     README.md
%{_datarootdir}/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com/*
%{_datarootdir}/glib-2.0/schemas/org.gnome.shell.extensions.dash-to-dock.gschema.xml
%{_datarootdir}/locale/*/LC_MESSAGES/dashtodock.mo

%changelog
* Sun May 06 2018 dmytr 63-1
- New version
* Fri Oct 20 2017 dmytr 1.1-1
- Initial packaging

