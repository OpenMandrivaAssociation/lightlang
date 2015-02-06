Summary: Dictionary Shell on Qt4
Name: lightlang
Version:	0.8.6
Release:	9
License: GPL
Group: Office
URL: http://lightlang.org.ru

Source: lightlang-%{version}-rev990.tar.bz2
#Patch0: MyWindow.patch

BuildRequires: qt4-common >= 4.4.3, python-xlib, python-qt4 >= 4.2.2, python-sip >= 4.2.2, xterm, sox, mplayer
Requires: qt4-common, python-xlib, python-qt4, sox, lightlang-dict

%description
LightLang is a small and powerfull dictionary shell,
writed on qt4 and has a many dictionary (ru-en and en-ru).

%package devel
Summary:	Devel package for LightLang
#Summary(ru): Пакет разработки для Lightlang
Group:		Office
Requires:	%{name} = %{version}
Requires:	pkgconfig
%description devel
%{summary}

%prep
%setup -q

%build

%configure --with-audio-player=mplayer
make %{?_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} install
#mkdir -p ${RPM_BUILD_ROOT}/%{_localstatedir}/lib
#mv -v ${RPM_BUILD_ROOT}/%{_datadir}/sl ${RPM_BUILD_ROOT}/%{_localstatedir}/lib/%{name}
#ln -s ../../%{_localstatedir}/lib/%{name} ${RPM_BUILD_ROOT}/%{_datadir}/sl

%files
%defattr(-,root, root)
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
%{_datadir}/xsl
%doc %{_docdir}/lightlang
%doc %{_mandir}/man1/*xz
%doc %{_mandir}/ru/man1/*xz

%files devel
%defattr(-,root, root)
%{_libdir}/pkgconfig/lightlang.pc


%changelog
* Thu Dec 30 2010 Александр Казанцев <kazancas@mandriva.org> 0.8.6-7mdv2011.0
+ Revision: 626202
- initial release
- import lightlang


* Thu Aug 5 2010 Alexander Kazancev <kazancas@mandriva.ru>
- build for revision 990

* Sat May 30 2009 Alexander Kazancev <kazancas@mandriva.ru>
- build for SVN538

* Thu Apr 23 2009 root <root@mandriva.com> 0.8.6-2mdk
- rebuild

* Sun Mar 22 2009 Alexandr Kazancev <kazancas@mandriva.ru> - 0.8.6
- New release 0.8.6-rc2

* Sun Oct 26 2008 Alexandr Kazancev <kazancas@mandriva.ru> - 0.8.5
- Build for 2009.0

* Sat Jan 27 2008 Alexandr Kazancev <kazancas@mail.ru> - 0.8.5
- First release
