Summary:	Notes plugin for the Xfce panel
Name:		xfce4-notes-plugin
Version:	1.6.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-notes-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-notes-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	xfce4-dev-tools
BuildRequires:	intltool
Obsoletes:	xfce-notes-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
xfce4-notes-plugin is a notes panel plugin for the Xfce Desktop Environment.
It provides a simple system for managing sticky notes on your desktop.

%prep
%setup -q

%build
./autogen.sh

%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_bindir}/xfce4-popup-notes
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
