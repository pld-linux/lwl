Summary:	Log Writer Library
Summary(pl):	Biblioteka zapisu do logów
Name:		lwl
Version:	1.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://savannah.nongnu.org/download/lwl/%{name}-%{version}.tar.gz
# Source0-md5:	b420d15e4b51b94b119a10079b62d31d
URL:		http://www.nongnu.org/lwl/
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
bibliotek± dla programistów pisz±cych w C. Dostarcza funkcje
pozwalaj±ce logowaæ do plików przez programy, czy demony. Format
logowanych wiadomo¶ci jest bardzo ³atwy do zmienienia, a jednocze¶nie
bardzo elastyczny.

%package devel
Summary:	Header files and development documentation for Log Writer Library
Summary(pl):	Pliki nag³ówkowe i dokumentacja do biblioteki zapisu do logów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for Log Writer Library.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do biblioteki zapisu do logów.

%package static
Summary:	Static Log Writer Library
Summary(pl):	Statyczna biblioteka zapisu do logów
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Log Writer Library.

%description static -l pl
Statyczna biblioteka zapisu do logów.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS THANKS
%attr(755,root,root) %{_libdir}/liblwl.*.*.*

%files devel
%defattr(644,root,root,755)
%doc src/example.c doc/html/{*.html,*.png}
%{_libdir}/*.la
%{_includedir}/*.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.a
