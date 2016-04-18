%define url_ver %(echo %{version} | cut -c 1-3)
%define _disable_rebuild_configure 1

Summary:	Notes plugin for the Xfce panel
Name:		xfce4-notes-plugin
Version:	1.8.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-notes-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-notes-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		xfce4-notes-plugin-1.8.1-str-fmt.patch
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1)
BuildRequires:	perl(XML::Parser)
BuildRequires:	xfce4-dev-tools
BuildRequires:	intltool
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	pkgconfig(libxfconf-0)
Obsoletes:	xfce-notes-plugin
Requires:	xfce4-panel >= 4.4.2

%description
xfce4-notes-plugin is a notes panel plugin for the Xfce Desktop Environment.
It provides a simple system for managing sticky notes on your desktop.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_sysconfdir}/xdg/autostart/xfce4-notes-autostart.desktop
%{_bindir}/xfce4-notes
%{_bindir}/xfce4-notes-settings
%{_bindir}/xfce4-popup-notes
%{_libdir}/xfce4/panel/plugins/libnotes.so
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_datadir}/applications/xfce4-notes.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/%{name}/gtk-2.0
%{_datadir}/%{name}/pixmaps
