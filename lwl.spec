Summary:	Log Writer Library
Summary(pl):	Biblioteka zapisu do logów
Name:		lwl
Version:	0.9
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://freesoftware.fsf.org/download/lwl/%{name}-%{version}.tar.gz
URL:		http://www.freesoftware.fsf.org/lwl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log Writer Library (LWL) is a portable library for C programmers. It
provides functions to log messages to files from programs such as
daemons. The format of logged messages is highly and easily
customizable.

%description -l pl
Biblioteka zapisu do logów (Log Writer Library - LWL) jest przeno¶n±
bibliotek± dla programistów pisz±cych w C. Dostacza funkcje
pozwalaj±ce logowaæ do plików przez programy, czy demony. Format
logowanych wiadomo¶ci jest bardzo ³atwy do zmienienia, a jednocze¶nie
bardzo elastyczny.

%package devel
Summary:	Header files and development documentation for Log Writer Library
Summary(pl):	Pliki nag³ówkowe i dokumentacja do biblioteki zapisu do logów
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for Log Writer Library.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do biblioteki zapisu do logów.

%package static
Summary:	Static Log Writer Library
Summary(pl):	Statyczna biblioteka zapisu do logów
Group:		Development/Libraries

%description static
Static Log Writer Library. Log Writer Library (LWL) is a portable
library for C programmers. It provides functions to log messages to
files from programs such as daemons. The format of logged messages is
highly and easily customizable.

%description static -l pl
Statyczna biblioteka zapisu do logów. Biblioteka zapisu do logów (Log
Writer Library - LWL) jest przeno¶n± bibliotek± dla programistów
pisz±cych w C. Dostacza funkcje pozwalaj±ce logowaæ do plików przez
programy, czy demony. Format logowanych wiadomo¶ci jest bardzo ³atwy
do zmienienia, a jednocze¶nie bardzo elastyczny.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc src/example.c doc/ref/html/{*.html,*.gif}
%attr(755,root,root) %{_libdir}/*.so.?
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/*.h

%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.a
