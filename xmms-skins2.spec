Summary:	Skins from Internet
Summary(pl):	Skórki z Internetu
Name:		xmms-skins2
Version:	1.0
Release:	1
License:	Free
Group:		X11/Applications/Multimedia
Source0:	%{name}.tar.gz
Requires:	bzip2
Requires:	tar
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%define		_prefix		/usr/X11R6
%define		skinsdir	%{_prefix}/share/xmms/Skins

%description
Additional skins for XMMS found in Internet. They were carefuly
selected, so you won't find here monstrosities made in 5 minutes.

%description -l pl
Dodatkowe skórki dla XMMS-a znalezione w Internecie. Zosta³y uwa¿nie
wybrane, tote¿ nie znajdzie siê tu potworków zrobionych w piêæ minut.

%prep
%setup -q -n xmms-skins2

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{skinsdir}

install *.bz2 $RPM_BUILD_ROOT%{skinsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz
%{skinsdir}/*
