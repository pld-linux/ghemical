# TODO:
# - use external openbabel (?)
# - use external miniMOPAC (? included is modified, I think...)
# - src/target3/open.o  - don't use tempnam

Summary:	Ghemical - The MM and QM calculations frontend
Summary(pl):	Ghemical - Frontend do obliczeñ MM oraz QM
Name:		ghemical
Version:	0.82
Release:	1
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://www.uku.fi/~thassine/ghemical/download/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-includes.patch
URL:		http://www.uku.fi/~thassine/ghemical/
BuildRequires:	autoconf
Buildrequires:	python-numpy-devel
BuildRequires:	gcc-g77
BuildRequires:	glut-devel
BuildRequires:	gtkglarea-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_pkgdir		%{_datadir}/%{name}/%{version}

%description
Ghemical is a computational chemistry software package released under
the GNU GPL. It is written in C++. It has a graphical user interface
(in fact, a couple of them), and it supports both quantum-mechanics
(semi-empirical and ab initio) models and molecular mechanics models
(there is an experimental Tripos 5.2-like force field for organic
molecules). Also a tool for reduced protein models is included.
Geometry optimization, molecular dynamics and a large set of
visualization tools are currently available.

%description -l pl
Ghemical to pakiet oprogramowania obliczeniowego z zakresu chemii
wypuszczony na licencji GNU GPL, napisany w C++. Ma graficzny
interfejs u¿ytkownika (w rzeczywisto¶ci - kilka). Obs³uguje zarówno
modele mechaniki kwantowej (semi-empiryzcne oraz ab initio) jak i
modele mechaniki molekularnej (jest eksperymentalne pole si³y w stylu
Tripos 5.2 dla cz±stek organicznych). Do³±czone jest tak¿e narzêdzie
do uproszczonych modeli bia³ek. Dostêpne s± optymalizacja geometrii,
dynamika molekularna oraz du¿y zestaw narzêdzi do wizualizacji.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure 
#	--enable-mpqc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Scientific}
install -d $RPM_BUILD_ROOT%{_datadir}/{gnome/help/%{name}/C,pixmaps}
install -d $RPM_BUILD_ROOT%{_pkgdir}/parameters/{builder,mm2param,mm1param/{stable,unstable}}

install bin/%{name}	$RPM_BUILD_ROOT%{_bindir}
install bin/user-docs/*	$RPM_BUILD_ROOT%{_datadir}/gnome/help/%{name}/C
install bin/parameters/builder/*.txt		$RPM_BUILD_ROOT%{_pkgdir}/parameters/builder
install bin/parameters/mm1param/stable/*.txt	$RPM_BUILD_ROOT%{_pkgdir}/parameters/mm1param/stable
install bin/parameters/mm1param/unstable/*.txt	$RPM_BUILD_ROOT%{_pkgdir}/parameters/mm1param/unstable
install bin/parameters/mm2param/*.txt		$RPM_BUILD_ROOT%{_pkgdir}/parameters/mm2param
install openbabel/*.txt				$RPM_BUILD_ROOT%{_pkgdir}
install %{SOURCE1}				$RPM_BUILD_ROOT%{_applnkdir}/Scientific
install %{SOURCE2}				$RPM_BUILD_ROOT%{_datadir}/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGLIST CHANGES PROJECT bin/examples/*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/gnome/help/%{name}
%{_datadir}/gnome/help/%{name}/C/*
%dir %{_pkgdir}
%{_pkgdir}/*
%{_datadir}/pixmaps/*.xpm
%{_applnkdir}/Scientific/*.desktop
