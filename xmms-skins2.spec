Summary:	Skins from Internet
Summary(pl.UTF-8):	Skórki z Internetu
Name:		xmms-skins2
Version:	1.0
Release:	7
License:	Free
Group:		X11/Applications/Multimedia
Source0:	http://ep09.pld-linux.org/~havner/%{name}.tar.bz2
# Source0-md5:	ba72b5ef8c32503a37b3a8658f0601eb
BuildRequires:	rpmbuild(macros) >= 1.125
# xmms-config script is used to get xmms paths
BuildRequires:	xmms-libs
Requires:	bzip2
Requires:	tar
Requires:	xmms
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xmms-skin

%define		_skindir	%{xmms_datadir}/Skins

%description
Additional skins for XMMS found in Internet. They were carefully
selected, so you won't find here monstrosities made in 5 minutes.
This package contains following skins:
- 2K
- Advanced
- BlackDawn
- BlueSteel
- Camel
- CrystalBastard
- Digitool
- ElectroPC
- Escalate
- ForcedToBe
- Kinwashi-Auriga
- Mercury
- Merregnon
- Plastik
- Relic
- Topaz
- WinampX

%description -l pl.UTF-8
Dodatkowe skórki dla XMMS-a znalezione w Internecie. Zostały uważnie
wybrane, toteż nie znajdzie się tu potworków zrobionych w pięć minut.
Ten pakiet zawiera następujące skórki:
- 2K
- Advanced
- BlackDawn
- BlueSteel
- Camel
- CrystalBastard
- Digitool
- ElectroPC
- Escalate
- ForcedToBe
- Kinwashi-Auriga
- Mercury
- Merregnon
- Plastik
- Relic
- Topaz
- WinampX

%package -n xmms-skin-2K
Summary:	2K skin
Summary(pl.UTF-8):	Skórka 2K
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-2K
2K skin.

%description -n xmms-skin-2K -l pl.UTF-8
Skórka 2K.

%package -n xmms-skin-Advanced
Summary:	Advanced skin
Summary(pl.UTF-8):	Skórka Advanced
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Advanced
Advanced skin.

%description -n xmms-skin-Advanced -l pl.UTF-8
Skórka Advanced.

%package -n xmms-skin-BlackDawn
Summary:	BlackDawn skin
Summary(pl.UTF-8):	Skórka BlackDawn
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-BlackDawn
BlackDawn skin.

%description -n xmms-skin-BlackDawn -l pl.UTF-8
Skórka BlackDawn.

%package -n xmms-skin-BlueSteel
Summary:	BlueSteel skin
Summary(pl.UTF-8):	Skórka BlueSteel
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-BlueSteel
BlueSteel skin.

%description -n xmms-skin-BlueSteel -l pl.UTF-8
Skórka BlueSteel.

%package -n xmms-skin-Camel
Summary:	Camel skin
Summary(pl.UTF-8):	Skórka Camel
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Camel
Camel skin.

%description -n xmms-skin-Camel -l pl.UTF-8
Skórka Camel.

%package -n xmms-skin-CrystalBastard
Summary:	CrystalBastard skin
Summary(pl.UTF-8):	Skórka CrystalBastard
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-CrystalBastard
CrystalBastard skin.

%description -n xmms-skin-CrystalBastard -l pl.UTF-8
Skórka CrystalBastard.

%package -n xmms-skin-Digitool
Summary:	Digitool skin
Summary(pl.UTF-8):	Skórka Digitool
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Digitool
Digitool skin.

%description -n xmms-skin-Digitool -l pl.UTF-8
Skórka Digitool.

%package -n xmms-skin-ElectroPC
Summary:	ElectroPC skin
Summary(pl.UTF-8):	Skórka ElectroPC
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-ElectroPC
ElectroPC skin.

%description -n xmms-skin-ElectroPC -l pl.UTF-8
Skórka ElectroPC.

%package -n xmms-skin-Escalate
Summary:	Escalate skin
Summary(pl.UTF-8):	Skórka Escalate
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Escalate
Escalate skin.

%description -n xmms-skin-Escalate -l pl.UTF-8
Skórka Escalate.

%package -n xmms-skin-ForcedToBe
Summary:	ForcedToBe skin
Summary(pl.UTF-8):	Skórka ForcedToBe
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-ForcedToBe
ForcedToBe skin.

%description -n xmms-skin-ForcedToBe -l pl.UTF-8
Skórka ForcedToBe.

%package -n xmms-skin-Kinwashi-Auriga
Summary:	Kinwashi-Auriga skin
Summary(pl.UTF-8):	Skórka Kinwashi-Auriga
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Kinwashi-Auriga
Kinwashi-Auriga skin.

%description -n xmms-skin-Kinwashi-Auriga -l pl.UTF-8
Skórka Kinwashi-Auriga.

%package -n xmms-skin-Mercury
Summary:	Mercury skin
Summary(pl.UTF-8):	Skórka Mercury
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Mercury
Mercury skin.

%description -n xmms-skin-Mercury -l pl.UTF-8
Skórka Mercury.

%package -n xmms-skin-Merregnon
Summary:	Merregnon skin
Summary(pl.UTF-8):	Skórka Merregnon
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Merregnon
Merregnon skin.

%description -n xmms-skin-Merregnon -l pl.UTF-8
Skórka Merregnon.

%package -n xmms-skin-Plastik
Summary:	Plastik skin
Summary(pl.UTF-8):	Skórka Plastik
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Plastik
Plastik skin.

%description -n xmms-skin-Plastik -l pl.UTF-8
Skórka Plastik.

%package -n xmms-skin-Relic
Summary:	Relic skin
Summary(pl.UTF-8):	Skórka Relic
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Relic
Relic skin.

%description -n xmms-skin-Relic -l pl.UTF-8
Skórka Relic.

%package -n xmms-skin-Topaz
Summary:	Topaz skin
Summary(pl.UTF-8):	Skórka Topaz
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Topaz
Topaz skin.

%description -n xmms-skin-Topaz -l pl.UTF-8
Skórka Topaz.

%package -n xmms-skin-WinampX
Summary:	WinampX skin
Summary(pl.UTF-8):	Skórka WinampX
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-WinampX
WinampX skin.

%description -n xmms-skin-WinampX -l pl.UTF-8
Skórka WinampX.

%prep
%setup -q -n xmms-skins2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_skindir}

install *.bz2 $RPM_BUILD_ROOT%{_skindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_skindir}/*

%files -n xmms-skin-2K
%defattr(644,root,root,755)
%doc doc/2K.txt.gz
%{_skindir}/2K.tar.bz2

%files -n xmms-skin-Advanced
%defattr(644,root,root,755)
%doc doc/Advanced.txt.gz
%{_skindir}/Advanced.tar.bz2

%files -n xmms-skin-BlackDawn
%defattr(644,root,root,755)
%doc doc/BlackDawn.txt.gz
%{_skindir}/BlackDawn.tar.bz2

%files -n xmms-skin-BlueSteel
%defattr(644,root,root,755)
%{_skindir}/BlueSteel.tar.bz2

%files -n xmms-skin-Camel
%defattr(644,root,root,755)
%doc doc/Camel.txt.gz
%{_skindir}/Camel.tar.bz2

%files -n xmms-skin-CrystalBastard
%defattr(644,root,root,755)
%doc doc/CrystalBastard.txt.gz
%{_skindir}/CrystalBastard.tar.bz2

%files -n xmms-skin-Digitool
%defattr(644,root,root,755)
%doc doc/Digitool.txt.gz
%{_skindir}/Digitool.tar.bz2

%files -n xmms-skin-ElectroPC
%defattr(644,root,root,755)
%doc doc/ElectroPC.txt.gz
%{_skindir}/ElectroPC.tar.bz2

%files -n xmms-skin-Escalate
%defattr(644,root,root,755)
%doc doc/Escalate.txt.gz
%{_skindir}/Escalate.tar.bz2

%files -n xmms-skin-ForcedToBe
%defattr(644,root,root,755)
%doc doc/ForcedToBe.txt.gz
%{_skindir}/ForcedToBe.tar.bz2

%files -n xmms-skin-Kinwashi-Auriga
%defattr(644,root,root,755)
%{_skindir}/Kinwashi-Auriga.tar.bz2

%files -n xmms-skin-Mercury
%defattr(644,root,root,755)
%{_skindir}/Mercury.tar.bz2

%files -n xmms-skin-Merregnon
%defattr(644,root,root,755)
%doc doc/Merregnon.txt.gz
%{_skindir}/Merregnon.tar.bz2

%files -n xmms-skin-Plastik
%defattr(644,root,root,755)
%doc doc/Plastik.txt.gz
%{_skindir}/Plastik.tar.bz2

%files -n xmms-skin-Relic
%defattr(644,root,root,755)
%doc doc/Relic.txt.gz
%{_skindir}/Relic.tar.bz2

%files -n xmms-skin-Topaz
%defattr(644,root,root,755)
%doc doc/Topaz.txt.gz
%{_skindir}/Topaz.tar.bz2

%files -n xmms-skin-WinampX
%defattr(644,root,root,755)
%doc doc/WinampX.txt.gz
%{_skindir}/WinampX.tar.bz2
