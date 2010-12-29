# $Id: lightlang.spec $
# Authority: akdengi
# Upstream: lightlang.org.ru

%define version 0.8.6
%define	rel	7
%define release %mkrel %{rel}

%{?dist: %{expand: %%define %dist 1}}

Summary: Dictionary Shell on Qt4
Summary:ru Словарь на основе Qt4
Name: lightlang
Version:	%{version}
Release:	%{release}
License: GPL
Group: Applications/Office
URL: http://lightlang.org.ru

Packager: Alexander Kazantcev <kazancas@mandriva.ru>
Vendor: EduMandriva <www.edumandriva.ru>
Source: lightlang-%{version}-rev990.tar.bz2
#Patch0: MyWindow.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt4-common >= 4.4.3, python-xlib, python-qt4 >= 4.2.2, python-sip >= 4.2.2, xterm, sox
Requires: qt4-common, python-xlib, python-qt4, sox, lightlang-dict

%description
LightLang is a small and powerfull dictionary shell, writed on qt4 and has a many dictionary (ru-en and en-ru).
%description -l ru
LightLang это маленькая и быстрая словарная оболочка на Qt4 которая содержит в комплекте множество словарей (ru-en и en-ru).

%package devel
Summary:	Devel package for LightLang
Summary(ru): Пакет разработки для Lightlang
Group:		Applications/Office
Requires:	%{name} = %{version}
Requires:	pkgconfig
%description devel
%{summary}

%prep
%setup

%build

%configure --with-audio-player=mplayer
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install
#mkdir -p ${RPM_BUILD_ROOT}/%{_localstatedir}/lib
#mv -v ${RPM_BUILD_ROOT}/%{_datadir}/sl ${RPM_BUILD_ROOT}/%{_localstatedir}/lib/%{name}
#ln -s ../../%{_localstatedir}/lib/%{name} ${RPM_BUILD_ROOT}/%{_datadir}/sl

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/sl
%{_bindir}/xsl
%{_bindir}/llrepo
%{_bindir}/lightlang
%{_libdir}/xsl
%{_libdir}/llrepo
%{_datadir}/applications/xsl.desktop
%{_datadir}/icons/hicolor/256x256/apps/*.png
%{_datadir}/icons/hicolor/128x128/apps/*.png
%{_datadir}/icons/hicolor/64x64/apps/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_datadir}/icons/hicolor/22x22/apps/*.png
%{_datadir}/icons/hicolor/16x16/apps/*.png
%{_datadir}/sl
%{_datadir}/sl
%{_datadir}/xsl
%doc %{_docdir}/lightlang
%doc %{_mandir}/man1/*.lzma
%doc %{_mandir}/ru/man1/*.lzma

%files devel
%{_libdir}/pkgconfig/lightlang.pc

