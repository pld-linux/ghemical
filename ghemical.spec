# TODO:
# - use external miniMOPAC (? included is modified, I think...)
# - src/target3/open.o  - don't use tempnam
# - use external openbabel

Summary:	Ghemical - The MM and QM calculations frontend
Summary(pl):	Ghemical - frontend do obliczeñ MM oraz QM
Name:		ghemical
Version:	1.01
Release:	1
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://www.uku.fi/~thassine/ghemical/download/%{name}-%{version}.tgz
# Source0-md5:	41f7b6ce38b4a1be9a9cf00d7d068b4a
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.uku.fi/~thassine/ghemical/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	f2c
BuildRequires:	glut-devel
BuildRequires:	gtkglarea1-devel
BuildRequires:	gtk+-devel
BuildRequires:	libglade-gnome-devel
BuildRequires:	openbabel-devel
BuildRequires:	python-numpy-devel
Requires:	openbabel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure
#	--enable-mpqc

# ENABLE_NLS and PACKAGE is workaround for g++ 3.3 and GNOME 1.x headers conflict
%{__make} \
	CFLAGS="%{rpmcflags} -I/usr/include/python2.4/Numeric" \
	CXXFLAGS="%{rpmcflags} -fno-exceptions %{!?debug:-DNO_DEBUG} -I/usr/X11R6/include -I/usr/include/python2.4/Numeric -DDATADIR=\\\"%{_datadir}/openbabel/\\\" -DENABLE_NLS -DPACKAGE=\\\"ghemical\\\""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGLIST CHANGES PROJECT bin/examples/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_pixmapsdir}/*.xpm
%{_desktopdir}/*.desktop
