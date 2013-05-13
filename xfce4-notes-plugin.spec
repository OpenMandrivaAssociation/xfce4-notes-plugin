%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Notes plugin for the Xfce panel
Name:		xfce4-notes-plugin
Version:	1.7.7
Release:	4
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-notes-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-notes-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		xfce4-notes-plugin-1.6.4-format_not_a_string_literal_and_no_format_arguments.patch
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	pkgconfig(libxfcegui4-1.0) >= 4.4.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	xfce4-dev-tools
BuildRequires:	intltool
BuildRequires:	unique-devel
BuildRequires:	xfconf-devel
Obsoletes:	xfce-notes-plugin
Requires:	xfce4-panel >= 4.4.2

%description
xfce4-notes-plugin is a notes panel plugin for the Xfce Desktop Environment.
It provides a simple system for managing sticky notes on your desktop.

%prep
%setup -q
#%patch0 -p1

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
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_datadir}/applications/xfce4-notes.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/%{name}/gtk-2.0
%{_datadir}/%{name}/pixmaps


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 1.7.7-3mdv2012.0
+ Revision: 791558
- Rebuild

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 1.7.7-2
+ Revision: 790086
- Rebuild for xfce 4.10

* Sun Nov 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.7-1mdv2011.0
+ Revision: 594763
- update to new version 1.7.7

* Mon Oct 18 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7.6-2mdv2011.0
+ Revision: 586598
- fix broken patch

* Tue Mar 30 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.6-1mdv2010.1
+ Revision: 529960
- update to new version 1.7.6

* Sun Mar 28 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.3-1mdv2010.1
+ Revision: 528647
- update to new version 1.7.3
- fix file list

* Sun Dec 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.2-1mdv2010.1
+ Revision: 480479
- add buildrequires on unique-devel
- update to new version 1.7.2
- fix file list
- adjust url for SOURCE0

* Mon Sep 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.1-1mdv2010.0
+ Revision: 432907
- update to new version 1.7.1

* Wed Jun 24 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.0-1mdv2010.0
+ Revision: 388892
- update to new version 1.7.0
- fix file list

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.4-2mdv2009.1
+ Revision: 349473
- rebuild for xfce-4.6.0

* Sun Mar 01 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.4-1mdv2009.1
+ Revision: 346604
- update to new version 1.6.4
- add missing buildrequires on thunar-devel
- Patch0: fix building with -Werror=format-strings

* Mon Nov 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.3-1mdv2009.1
+ Revision: 306366
- update to new version 1.6.3

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.2-3mdv2009.1
+ Revision: 295003
- rebuild for new Xfce4.6 beta1

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 1.6.2-2mdv2009.0
+ Revision: 269789
- rebuild early 2009.0 package (before pixel changes)

* Wed May 07 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.2-1mdv2009.0
+ Revision: 202697
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Dec 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.1-1mdv2008.1
+ Revision: 138458
- add missing buildrequires

  + Jérôme Soyer <saispo@mandriva.org>
    - New release 1.6.1

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - better description

* Fri Nov 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.0-1mdv2008.1
+ Revision: 111375
- new version

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.1-3mdv2008.1
+ Revision: 110127
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING, INSTALl and NEWS files
- use upstream name

* Fri May 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.4.1-2mdv2008.0
+ Revision: 31035
- add %%post and %%postun scripts

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.4.1-1mdv2008.0
+ Revision: 30429
- update url
- own missing files
- new version

