# TODO:
# - use external openbabel (?)
# - use external miniMOPAC (? included is modified, I think...)
# - src/target3/open.o  - don't use tempnam

Summary:	Ghemical - The MM and QM calculations frontend.
Summary(pl):	Ghemical - Frontend do obliczeñ MM oraz QM.
Name:		ghemical
Version:	0.82
Release:	0.5
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://www.uku.fi/~thassine/ghemical/download/%{name}-%{version}.tgz
Icon:		%{name}.xpm
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

# well... who will translate this? :)
#%description -l pl

%prep
%setup -q
%patch0 -p1

%build
autoconf
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
#install %{SOURCE1}				$RPM_BUILD_ROOT%{_applnkdir}/Scientific
#install %{ICON}		%{_datadir}/pixmaps/

gzip -9nf AUTHORS BUGLIST CHANGES PROJECT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz bin/examples/*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/gnome/help/%{name}
%{_datadir}/gnome/help/%{name}/C/*
%dir %{_pkgdir}
%{_pkgdir}/*
#%{_datadir}/pixmaps/*.xpm
#%{_applnkdir}/Scientific/*.desktop
