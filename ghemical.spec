Summary:	Ghemical - The MM and QM calculations frontend
Summary(pl):	Ghemical - frontend do obliczeñ MM oraz QM
Name:		ghemical
Version:	2.01
Release:	1
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://www.uku.fi/~thassine/projects/download/%{name}-%{version}.tar.gz
# Source0-md5:	7a160160c80f213b43485613a5ca2d75
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-link.patch
URL:		http://www.uku.fi/~thassine/projects/ghemical/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	gtkglext-devel >= 1.0.5
BuildRequires:	libglade2-devel >= 2.4.0
BuildRequires:	libghemical-devel >= 2.00
BuildRequires:	libstdc++-devel
BuildRequires:	openbabel-devel >= 2.0.0
BuildRequires:	pkgconfig
Requires:	openbabel >= 2.0.0
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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-openbabel

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO examples
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_pixmapsdir}/*.xpm
%{_desktopdir}/*.desktop
