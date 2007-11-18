Summary:	Notes plugin for the Xfce panel
Name:		xfce-notes-plugin
Version:	1.4.1
Release:	%mkrel 2
Epoch:		1
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-notes-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-notes-plugin/xfce4-notes-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.3.90.2
BuildRequires:	xfce-panel-devel >= 4.3.90.2
BuildRequires:	libxfcegui4-devel >= 4.3.90.2
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Notes panel plugin for the Xfce Desktop Environment. It provides a
simple system for managing sticky notes on your desktop.

%prep
%setup -qn xfce4-notes-plugin-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang xfce4-notes-plugin

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f xfce4-notes-plugin.lang
%defattr(-,root,root)
%doc README ChangeLog COPYING AUTHORS INSTALL NEWS
%{_bindir}/xfce4-popup-notes
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg