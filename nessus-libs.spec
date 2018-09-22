Summary:	Nessus libraries
Summary(pl.UTF-8):	Biblioteki Nessus
Name:		nessus-libs
Version:	2.2.11
Release:	1
License:	GPL
Group:		Networking
Vendor:		Nessus Project
# Source0:	ftp://ftp.nessus.org/pub/nessus/nessus-%{version}/src/nessus-libraries-%{version}.tar.gz
Source0:	nessus-libraries-%{version}.tar.gz
# Source0-md5:	c1180bec3a7f1b78d4d881f9a73e99bc
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-libtool.patch
Patch3:		openssl.patch
URL:		http://www.nessus.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# needed to get /var/lib/nessus instead of /var/nessus
%define		_localstatedir	/var/lib

%description
Libraries for Nessus - a free, powerful, up-to-date and easy to use
remote security scanner.

%description -l pl.UTF-8
Celem projektu "Nessus" jest dostarczenie społeczności internetowej
wolnodostępnego, potężnego, aktualnego i łatwego w użyciu zdalnego
skanera bezpieczeństwa (tzn. oprogramowania, które zdalnie
przeprowadza audyt podanej sieci i sprawdza, czy źli ludzie mogą się
do niej włamać lub jej nadużyć w jakiś sposób).

Ten pakiet zawiera biblioteki Nessusa.

%package devel
Summary:	Nessus libraries development files
Summary(pl.UTF-8):	Pliki dla programistów używających Nessusa
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libpcap-devel
Requires:	openssl-devel

%description devel
Header files for developing applications that use Nessus.

%description devel -l pl.UTF-8
Pliki nagłówkowe konieczne do rozwoju aplikacji używających Nessusa.

%package static
Summary:	Nessus static libraries
Summary(pl.UTF-8):	Biblioteki statyczne Nessusa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Nessus static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Nessusa.

%prep
%setup -q -n nessus-libraries
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--disable-nessuspcap \
	--enable-cipher \
	--enable-openpty \
	--enable-bpf-sharing

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/nessus

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.2
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_localstatedir}/nessus

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nessus-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man1/nessus-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
