Summary:	Ghemical - The MM and QM calculations frontend.
Summary(pl):	Ghemical - Frontend do obliczeñ MM oraz QM.
Name:		ghemical
Version:	0.82
Release:	0.1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://www.uku.fi/~thassine/ghemical/download/%{name}-%{version}.tgz
Icon:		%{name}.xpm
URL:		http://www.uku.fi/~thassine/ghemical/
BuildRequires:	autoconf
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

%description -l pl
Chemical

%prep
%setup -q

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_datadir}/{pixmaps/hicolor/32x32/mimetypes,mimelnk/application,mime-info}
#install -d $RPM_BUILD_ROOT%{_applnkdir}/Scientific

%{__make} install DESTDIR=$RPM_BUILD_ROOT

#install kde/mimelnk/application/x-chemtool.desktop	$RPM_BUILD_ROOT%{_datadir}/mimelnk/application
#install kde/icons/hicolor/32x32/mimetypes/chemtool.png	$RPM_BUILD_ROOT%{_datadir}/pixmaps/hicolor/32x32/mimetypes
#install gnome/mime-types/* 			$RPM_BUILD_ROOT%{_datadir}/mime-info
#install gnome/gnome-application-chemtool.png	$RPM_BUILD_ROOT%{_datadir}/pixmaps
#install %{SOURCE1}				$RPM_BUILD_ROOT%{_applnkdir}/Scientific
#install %{name}.xpm				$RPM_BUILD_ROOT%{_datadir}/pixmaps

gzip -9nf ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz examples/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mimelnk/application/*
%{_datadir}/pixmaps/hicolor/32x32/mimetypes/*.png
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/*.xpm
%{_applnkdir}/Scientific/*.desktop
