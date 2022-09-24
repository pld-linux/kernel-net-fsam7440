#
# Conditional build:
%bcond_with	verbose		# verbose build (V=1)
#
%define		modname	fsam7440
%define		_rel	0.1
Summary:	Linux kernel module for Wireless switch on AMILO M 7440
Summary(pl.UTF-8):	Moduł jądra Linuksa dla przełączników bezprzewodowych w AMILO M 7440
Name:		kernel%{_alt_kernel}-net-%{modname}
Version:	0.4
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL v2
Group:		Base/Kernel
Source0:	https://downloads.sourceforge.net/fsam7440/fsam7440-%{version}.tar.bz2
# Source0-md5:	d7567212acb5aca03b7926bbfcf67721
URL:		http://fsam7440.sourceforge.net/
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.14}
BuildRequires:	rpmbuild(macros) >= 1.308
BuildRequires:	sed >= 4.0
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod
Requires:	module-init-tools >= 3.2.2-2
Obsoletes:	kernel%{_alt_kernel}-smp-net-%{modname} < 0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description -n kernel%{_alt_kernel}-net-%{modname}
Linux kernel module to change wireless radio status on Fujitsu-Siemens
AMILO M 7440 laptop.

%description -n kernel%{_alt_kernel}-net-%{modname} -l pl.UTF-8
Moduł jądra Linuksa do zmiany stanu radia bezprzewodowego w laptopach
Fujitsu-Siemens AMILO M 7440.

%prep
%setup -q -n %{modname}-%{version}

%{__sed} -i -e 's,linux/autoconf\.h,generated/autoconf.h,' fsam7440.c

%build
%build_kernel_modules -m fsam7440

%install
rm -rf $RPM_BUILD_ROOT

%install_kernel_modules -m fsam7440 -d misc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n kernel%{_alt_kernel}-net-%{modname}
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-net-%{modname}
%depmod %{_kernel_ver}

%files -n kernel%{_alt_kernel}-net-%{modname}
%defattr(644,root,root,755)
%doc README AUTHORS
%doc %lang(es) README-ES
/lib/modules/%{_kernel_ver}/misc/fsam7440*.ko*
