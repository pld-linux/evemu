Summary:	Linux kernel evdev device emulation
Summary(pl.UTF-8):	Emulacja linuksowych urządzeń evdev
Name:		evemu
Version:	1.0.10
Release:	1
License:	LGPL v3
Group:		Libraries
#Source0Download: https://launchpad.net/evemu/+download
Source0:	https://launchpad.net/evemu/trunk/evemu-%{version}/+download/%{name}-%{version}.tar.xz
# Source0-md5:	34595e1f7872b8440945e8c563e06932
URL:		https://launchpad.net/evemu
BuildRequires:	asciidoc
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tar >= 1:1.22
BuildRequires:	xmlto
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The evemu library and tools are used to describe devices, record data,
create devices and replay data from Linux kernel evdev devices.

%description -l pl.UTF-8
Biblioteka i narzędzia evemu służą do opisywania urządzeń, zapisu
danych, tworzenia urządzeń i odtwarzania danych z urządzeń evdev jądra
Linuksa.

%package devel
Summary:	Header files for evemu library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki evemu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for evemu library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki evemu.

%package static
Summary:	Static evemu library
Summary(pl.UTF-8):	Statyczna biblioteka evemu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static evemu library.

%description static -l pl.UTF-8
Statyczna biblioteka evemu.

%package -n python-evemu
Summary:	Python interface to evemu library
Summary(pl.UTF-8):	Pythonowy interfejs do biblioteki evemu
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-evemu
Python interface to evemu library.

%description -n python-evemu -l pl.UTF-8
Pythonowy interfejs do biblioteki evemu.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/evemu-*
%attr(755,root,root) %{_libdir}/libevemu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libevemu.so.1
%{_mandir}/man1/evemu-*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libevemu.so
%{_includedir}/evemu.h
%{_pkgconfigdir}/evemu.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libevemu.a

%files -n python-evemu
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/evemu
%{py_sitescriptdir}/evemu/*.py[co]
