# TODO:
# - use external miniMOPAC (? included is modified, I think...)
# - src/target3/open.o  - don't use tempnam
# - use external openbabel

Summary:	Ghemical - The MM and QM calculations frontend
Summary(pl):	Ghemical - Frontend do obliczeñ MM oraz QM
Name:		ghemical
Version:	0.90
Release:	1
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://www.uku.fi/~thassine/ghemical/download/%{name}-%{version}.tgz
# Source0-md5:	a469e583af31c89146397f81aa88289c
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-c++.patch
URL:		http://www.uku.fi/~thassine/ghemical/
BuildRequires:	autoconf
BuildRequires:	gcc-g77
BuildRequires:	glut-devel
BuildRequires:	gtkglarea-devel
BuildRequires:	gtk+-devel
BuildRequires:	libglade-gnome-devel
BuildRequires:	openbabel-devel
Buildrequires:	python-numpy-devel
Requires:	openbabel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch1 -p1

%build
%{__autoconf}
%configure
#	--enable-mpqc

# ENABLE_NLS and PACKAGE is workaround for g++ 3.3 and gnome 1.x headers conflict
%{__make} \
	CFLAGS="%{rpmcflags} -I/usr/include/python2.2/Numeric" \
	CXXFLAGS="%{rpmcflags} -fno-exceptions %{!?debug:-DNO_DEBUG} -I/usr/X11R6/include -I/usr/include/python2.2/Numeric -DDATADIR=\\\"%{_datadir}/openbabel/\\\" -DENABLE_NLS -DPACKAGE=\\\"ghemical\\\""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Scientific/Chemistry,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Chemistry
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGLIST CHANGES PROJECT bin/examples/*
%attr(755,root,root) %{_bindir}/*
%{_pkgdir}
%{_pixmapsdir}/*.xpm
%{_applnkdir}/Scientific/Chemistry/*.desktop
