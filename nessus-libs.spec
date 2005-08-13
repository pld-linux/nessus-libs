Summary:	Nessus libraries
Summary(pl):	Biblioteki Nessus
Name:		nessus-libs
Version:	2.2.5
Release:	1
License:	GPL
Group:		Networking
Vendor:		Nessus Project
Source0:	ftp://ftp.nessus.org/pub/nessus/nessus-%{version}/src/nessus-libraries-%{version}.tar.gz
# Source0-md5:	a26a31ee7d8e82511e4ba3954ab1db24
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-link.patch
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

%description -l pl
Celem projektu "Nessus" jest dostarczenie spo³eczno¶ci internetowej
wolnodostêpnego, potê¿nego, aktualnego i ³atwego w u¿yciu zdalnego
skanera bezpieczeñstwa (tzn. oprogramowania, które zdalnie
przeprowadza audyt podanej sieci i sprawdza, czy ¼li ludzie mog± siê
do niej w³amaæ lub jej nadu¿yæ w jaki¶ sposób).

Ten pakiet zawiera biblioteki Nessusa.

%package devel
Summary:	Nessus libraries development files
Summary(pl):	Pliki dla programistów u¿ywaj±cych Nessusa
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libpcap-devel
Requires:	openssl-devel

%description devel
Header files for developing applications that use Nessus.

%description devel -l pl
Pliki nag³ówkowe konieczne do rozwoju aplikacji u¿ywaj±cych Nessusa.

%package static
Summary:	Nessus static libraries
Summary(pl):	Biblioteki statyczne Nessusa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Nessus static libraries.

%description static -l pl
Biblioteki statyczne Nessusa.

%prep
%setup -q -n nessus-libraries
%patch0 -p1
%patch1 -p1

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
