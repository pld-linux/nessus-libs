#FIXME: desc/summary a w szczególności wersje pl ssą

Summary:	Nessus libraries
Summary(pl):	Biblioteki Nessus
Name:		nessus-libs
Version:	1.2.5
Release:	1
License:	GPL
Group:		Networking
Vendor:		Nessus Project
Source0:	ftp://ftp.nessus.org/pub/nessus/nessus-%{version}/src/nessus-libraries-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.nessus.org/
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries for Nessus - a free, powerful, up-to-date and easy to use
remote security scanner.

%description -l pl
Biblioteki dla Nessusa - wolnego, potężnego, aktualnego i łatwego w
użyciu zdalnego skanera zabezpieczeń.

%package devel
Summary:	Nessus libraries development files
Summary(pl):	Pliki dla deweloperów używających Nessusa
Group:		Development/Libraries
Requires:   %{name} = %{version}

%description devel
Header files and libraries for developing applications that use
Nessus.

%description devel -l pl
Pliki nagłówkowe i biblioteki konieczne do rozwoju aplikacji
używających Nessusa.

%package static
Summary:	Nessus static libraries
Summary(pl):	Biblioteki statyczne Nessusa
Group:		Development/Libraries
Requires:   %{name}-devel = %{version}

%description static
Nessus static libraries.

%description static -l pl
Biblioteki statyczne Nessusa.

%prep
%setup -q -n nessus-libraries
%patch0 -p1

%build
aclocal
%{__autoconf}
%configure \
	--disable-nessuspcap \
	--enable-cipher
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
