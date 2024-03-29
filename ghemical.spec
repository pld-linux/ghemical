Summary:	Ghemical - The MM and QM calculations frontend
Summary(pl.UTF-8):	Ghemical - frontend do obliczeń MM oraz QM
Name:		ghemical
Version:	3.0.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://www.bioinformatics.org/ghemical/download/current/%{name}-%{version}.tar.gz
# Source0-md5:	becf98626f0eba73f7f042bc92aa60ac
Source1:	%{name}.desktop
Source2:	%{name}.xpm
URL:		http://www.bioinformatics.org/ghemical/ghemical/index.html
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	freeglut-devel
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	gtkglext-devel >= 1.0.5
BuildRequires:	libglade2-devel >= 2.4.0
BuildRequires:	libghemical-devel >= 3.0.0
BuildRequires:	liboglappth-devel >= 1.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	openbabel-devel >= 2.0.0
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.6.0
Requires:	gtk+2 >= 2:2.6.0
Requires:	gtkglext >= 1.0.5
Requires:	libglade2 >= 2.4.0
Requires:	libghemical >= 3.0.0
Requires:	liboglappth >= 1.0.0
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

%description -l pl.UTF-8
Ghemical to pakiet oprogramowania obliczeniowego z zakresu chemii
wypuszczony na licencji GNU GPL, napisany w C++. Ma graficzny
interfejs użytkownika (w rzeczywistości - kilka). Obsługuje zarówno
modele mechaniki kwantowej (semi-empiryzcne oraz ab initio) jak i
modele mechaniki molekularnej (jest eksperymentalne pole siły w stylu
Tripos 5.2 dla cząstek organicznych). Dołączone jest także narzędzie
do uproszczonych modeli białek. Dostępne są optymalizacja geometrii,
dynamika molekularna oraz duży zestaw narzędzi do wizualizacji.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-openbabel \
	--enable-threads \
	--enable-gtk

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
%attr(755,root,root) %{_bindir}/ghemical
%{_datadir}/%{name}
%{_pixmapsdir}/ghemical.xpm
%{_desktopdir}/ghemical.desktop
