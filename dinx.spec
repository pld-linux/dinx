%define		sysver	%(echo `uname -r`)
Summary:	DinX
Summary(pl):	DinX
Name:		dinx
Version:	0.2.2
Release:	1
License:	GPL
Group:		DinX
######		Unknown group!
Group(pl):	DinX
Source0:	%{name}-%{version}.tar.gz
Patch0:		
#BuildRequires:	
URL:		http://dinx.sourceforge.net/
#Requires:	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/DinX
%define _modulesdir	/lib/modules/%{sysver}
%define	_sysincludedir	/usr/include

%description

%description -l pl

%package devel
Summary:	DinX devel	
Summary(pl):	DinX devel
Group:		DinX
######		Unknown group!
Group(pl):	DinX

%description devel

%description -l pl devel

%package kernel-%{sysver}-modules
Summary:	DinX kernel modules.
Summary(pl):	DinX modu³y j±dra.
Group:		DinX
######		Unknown group!
Group(pl):	DinX

%description kernel-%{sysver}-modules

%description -l pl kernel-%{sysver}-modules

%prep
%setup -q

#%patch

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/dev
install -d $RPM_BUILD_ROOT%{_modulesdir}/misc
install -d $RPM_BUILD_ROOT%{_includedir}/{dinx,linux}
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

(cd $RPM_BUILD_ROOT; cd usr/include; install -d {dinx,linux}; \
ln -s ../../DinX/include/linux/dinx.h linux/dinx.h;\
ln -s ../../DinX/include/dinx/access.h dinx/access.h; \
ln -s ../../DinX/include/dinx/messages.h dinx/messages.h)

install -s modules/dinx*.o $RPM_BUILD_ROOT%{_modulesdir}/misc

gzip -9nf README

cd $RPM_BUILD_ROOT/dev
echo "Makeing DinX devices.."
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
ln -s dinxwin0 dinxwin

echo "Makeing DinX Server devices.."
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
ln -s dinxsvr0 dinxsvr

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%defattr(644,root,root,755)
%doc README.gz doc/*
%attr(755,root,root) %{_bindir}/dinxd
%attr(644,root,root) %{_libdir}/libdinx.a
%attr(666,root,root) /dev/dinx*

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_sysincludedir}/linux/dinx.h
%attr(644,root,root) %{_sysincludedir}/dinx/*.h
%attr(644,root,root) %{_includedir}/linux/dinx.h
%attr(644,root,root) %{_includedir}/dinx/*.h

%files kernel-%{sysver}-modules
%defattr(644,root,root,755)
%attr(644,root,root) %{_modulesdir}/misc/*.o
