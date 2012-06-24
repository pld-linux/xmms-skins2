Summary:	Skins from Internet
Summary(pl):	Sk�rki z Internetu
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

%description -l pl
Dodatkowe sk�rki dla XMMS-a znalezione w Internecie. Zosta�y uwa�nie
wybrane, tote� nie znajdzie si� tu potwork�w zrobionych w pi�� minut.
Ten pakiet zawiera nast�puj�ce sk�rki:
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
Summary(pl):	Sk�rka 2K
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-2K
2K skin.

%description -n xmms-skin-2K -l pl
Sk�rka 2K.

%package -n xmms-skin-Advanced
Summary:	Advanced skin
Summary(pl):	Sk�rka Advanced
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Advanced
Advanced skin.

%description -n xmms-skin-Advanced -l pl
Sk�rka Advanced.

%package -n xmms-skin-BlackDawn
Summary:	BlackDawn skin
Summary(pl):	Sk�rka BlackDawn
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-BlackDawn
BlackDawn skin.

%description -n xmms-skin-BlackDawn -l pl
Sk�rka BlackDawn.

%package -n xmms-skin-BlueSteel
Summary:	BlueSteel skin
Summary(pl):	Sk�rka BlueSteel
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-BlueSteel
BlueSteel skin.

%description -n xmms-skin-BlueSteel -l pl
Sk�rka BlueSteel.

%package -n xmms-skin-Camel
Summary:	Camel skin
Summary(pl):	Sk�rka Camel
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Camel
Camel skin.

%description -n xmms-skin-Camel -l pl
Sk�rka Camel.

%package -n xmms-skin-CrystalBastard
Summary:	CrystalBastard skin
Summary(pl):	Sk�rka CrystalBastard
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-CrystalBastard
CrystalBastard skin.

%description -n xmms-skin-CrystalBastard -l pl
Sk�rka CrystalBastard.

%package -n xmms-skin-Digitool
Summary:	Digitool skin
Summary(pl):	Sk�rka Digitool
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Digitool
Digitool skin.

%description -n xmms-skin-Digitool -l pl
Sk�rka Digitool.

%package -n xmms-skin-ElectroPC
Summary:	ElectroPC skin
Summary(pl):	Sk�rka ElectroPC
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-ElectroPC
ElectroPC skin.

%description -n xmms-skin-ElectroPC -l pl
Sk�rka ElectroPC.

%package -n xmms-skin-Escalate
Summary:	Escalate skin
Summary(pl):	Sk�rka Escalate
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Escalate
Escalate skin.

%description -n xmms-skin-Escalate -l pl
Sk�rka Escalate.

%package -n xmms-skin-ForcedToBe
Summary:	ForcedToBe skin
Summary(pl):	Sk�rka ForcedToBe
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-ForcedToBe
ForcedToBe skin.

%description -n xmms-skin-ForcedToBe -l pl
Sk�rka ForcedToBe.

%package -n xmms-skin-Kinwashi-Auriga
Summary:	Kinwashi-Auriga skin
Summary(pl):	Sk�rka Kinwashi-Auriga
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Kinwashi-Auriga
Kinwashi-Auriga skin.

%description -n xmms-skin-Kinwashi-Auriga -l pl
Sk�rka Kinwashi-Auriga.

%package -n xmms-skin-Mercury
Summary:	Mercury skin
Summary(pl):	Sk�rka Mercury
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Mercury
Mercury skin.

%description -n xmms-skin-Mercury -l pl
Sk�rka Mercury.

%package -n xmms-skin-Merregnon
Summary:	Merregnon skin
Summary(pl):	Sk�rka Merregnon
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Merregnon
Merregnon skin.

%description -n xmms-skin-Merregnon -l pl
Sk�rka Merregnon.

%package -n xmms-skin-Plastik
Summary:	Plastik skin
Summary(pl):	Sk�rka Plastik
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Plastik
Plastik skin.

%description -n xmms-skin-Plastik -l pl
Sk�rka Plastik.

%package -n xmms-skin-Relic
Summary:	Relic skin
Summary(pl):	Sk�rka Relic
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Relic
Relic skin.

%description -n xmms-skin-Relic -l pl
Sk�rka Relic.

%package -n xmms-skin-Topaz
Summary:	Topaz skin
Summary(pl):	Sk�rka Topaz
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-Topaz
Topaz skin.

%description -n xmms-skin-Topaz -l pl
Sk�rka Topaz.

%package -n xmms-skin-WinampX
Summary:	WinampX skin
Summary(pl):	Sk�rka WinampX
Group:		X11/Applications/Multimedia
Requires:	xmms
Provides:	xmms-skin
Obsoletes:	xmms-skins2

%description -n xmms-skin-WinampX
WinampX skin.

%description -n xmms-skin-WinampX -l pl
Sk�rka WinampX.

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
