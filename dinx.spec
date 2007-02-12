%define		sysver	%(echo `uname -r`)
Summary:	DinX is not X
Summary(pl.UTF-8):	DinX to nie X
Name:		dinx
Version:	0.2.2
Release:	2
License:	MPL/GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/dinx/%{name}-%{version}.tar.gz
# Source0-md5:	79386af387fd05b9af9407939d4629c1
URL:		http://dinx.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# NOT FHS-compliant
# TODO: missing dirs (after making it FHS-compliant)
%define		_prefix		/usr/DinX
%define		_modulesdir	/lib/modules/%{sysver}
%define		_sysincludedir	/usr/include

%description
DinX is an experimental windowing system. DinX is designed to be
simple, lightweight, and fast. It should be suitable for running
multiple windowed programs on a small system, like a Linux handheld.

%description -l pl.UTF-8
DinX jest eksperymentalnym systemem okienkowym. Ma być prosty, lekki i
szybki. Powinien być odpowiedni do uruchamiania wielu aplikacji
okienkowych na małym systemie.

%package devel
Summary:	DinX devel
Summary(pl.UTF-8):	DinX dla programistów
Group:		Development/Libraries

%description devel
Header files for DinX libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe do bibliotek DinX.

%package kernel-%{sysver}-modules
Summary:	DinX kernel modules
Summary(pl.UTF-8):	DinX - moduły jądra
Group:		Base/Kernel

%description kernel-%{sysver}-modules
Kernel modules for DinX.

%description kernel-%{sysver}-modules -l pl.UTF-8
Moduły jądra dla DinX.

%prep
%setup -q

%build
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/dev
install -d $RPM_BUILD_ROOT%{_modulesdir}/misc
install -d $RPM_BUILD_ROOT%{_includedir}/{dinx,linux}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

(cd $RPM_BUILD_ROOT; cd usr/include; install -d {dinx,linux}; \
ln -sf ../../DinX/include/linux/dinx.h linux/dinx.h;\
ln -sf ../../DinX/include/dinx/access.h dinx/access.h; \
ln -sf ../../DinX/include/dinx/messages.h dinx/messages.h)

install modules/dinx*.o $RPM_BUILD_ROOT%{_modulesdir}/misc

cd $RPM_BUILD_ROOT/dev
echo "Making DinX devices.."
mknod dinxwin0 c 60 0
mknod dinxwin1 c 60 1
mknod dinxwin2 c 60 2
mknod dinxwin3 c 60 3
mknod dinxwin4 c 60 4
mknod dinxwin5 c 60 5
mknod dinxwin6 c 60 6
mknod dinxwin7 c 60 7
mknod dinxwin8 c 60 8
mknod dinxwin9 c 60 9
mknod dinxwin10 c 60 10
mknod dinxwin11 c 60 11
mknod dinxwin12 c 60 12
mknod dinxwin13 c 60 13
mknod dinxwin14 c 60 14
mknod dinxwin15 c 60 15
ln -sf dinxwin0 dinxwin

echo "Making DinX Server devices.."
mknod dinxsvr0 c 60 0
mknod dinxsvr1 c 60 1
mknod dinxsvr2 c 60 2
mknod dinxsvr3 c 60 3
mknod dinxsvr4 c 60 4
mknod dinxsvr5 c 60 5
mknod dinxsvr6 c 60 6
mknod dinxsvr7 c 60 7
mknod dinxsvr8 c 60 8
mknod dinxsvr9 c 60 9
mknod dinxsvr10 c 60 10
mknod dinxsvr11 c 60 11
mknod dinxsvr12 c 60 12
mknod dinxsvr13 c 60 13
mknod dinxsvr14 c 60 14
mknod dinxsvr15 c 60 15
ln -sf dinxsvr0 dinxsvr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*
%attr(755,root,root) %{_bindir}/dinxd
%attr(666,root,root) /dev/dinx*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libdinx.a
%{_sysincludedir}/linux/dinx.h
%{_sysincludedir}/dinx/*.h
%{_includedir}/linux/dinx.h
%{_includedir}/dinx/*.h

%files kernel-%{sysver}-modules
%defattr(644,root,root,755)
%{_modulesdir}/misc/*.o
