# TODO:
# - use external openbabel (?)
# - use external miniMOPAC (? included is modified, I think...)

Summary:	Ghemical - The MM and QM calculations frontend.
Summary(pl):	Ghemical - Frontend do obliczeñ MM oraz QM.
Name:		ghemical
Version:	0.82
Release:	0.4
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://www.uku.fi/~thassine/ghemical/download/%{name}-%{version}.tgz
Icon:		%{name}.xpm
Patch0:		%{name}-miniMOPAC_fix.patch
URL:		http://www.uku.fi/~thassine/ghemical/
BuildRequires:	autoconf
Buildrequires:	python-numpy-devel
BuildRequires:	gcc-g77
BuildRequires:	gtkglarea-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
install -d $RPM_BUILD_ROOT%{%{_bindir},%{_applnkdir}/Scientific}

#install %{SOURCE1}				$RPM_BUILD_ROOT%{_applnkdir}/Scientific

gzip -9nf ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz bin/examples/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pixmaps/*.xpm
%{_applnkdir}/Scientific/*.desktop
