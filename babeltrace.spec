%define _disable_ld_no_undefined 1

%define devname %mklibname -d babeltrace

Summary:	An open source trace format converter
Name:		babeltrace
Version:	2.0.0
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		http://diamon.org/babeltrace
Source0:	http://www.efficios.com/files/babeltrace/babeltrace-%{version}.tar.bz2
Patch0:		babeltrace-2.0.0-fix-reserved-keywords.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libdw)
BuildRequires:	pkgconfig(libelf)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	swig

%libpackage babeltrace2 0
%libpackage babeltrace2-ctf-writer 0

%description
An open source trace format converter.

%package -n %{devname}
Summary:	Development files for the babeltrace trace format converter
Group:		Development/Other
Provides:	lib%{name} = %{EVRD}
Requires:	%mklibname babeltrace 1
Requires:	%mklibname babeltrace-lttng-live 1
Requires:	%mklibname babeltrace-dummy 1
Requires:	%mklibname babeltrace-ctf 1
Requires:	%mklibname babeltrace-ctf-metadata 1
Requires:	%mklibname babeltrace-ctf-text 1

%description -n %{devname}
Development files for the babeltrace trace format converter.

%package -n python-%{name}
Summary:	Python bindings to the babeltrace trace format converter
Group:		Development/Python

%description -n python-%{name}
Python bindings to the babeltrace trace format converter.

%prep
%autosetup -p1

%build
# Workaround for failure at link time
#ld.lld: error: undefined hidden symbol: __start___bt_plugin_descriptor_attributes
%define _disable_lto 1
%global optflags %{optflags} -fno-lto -Wl,-z,nostart-stop-gc -Wno-error=unknown-warning-option
%global build_ldflags %{build_ldflags} -z nostart-stop-gc
#export CC=gcc
%configure --enable-python-bindings
%make_build

%install
%make_install

%files
%{_bindir}/babeltrace2
%{_libdir}/babeltrace2
%{_mandir}/man7/babeltrace2-*.7*

%files -n %{devname}
%{_includedir}/babeltrace2
%{_includedir}/babeltrace2-ctf-writer
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_mandir}/man1/*
%doc %{_docdir}/%{name}/*

%files -n python-%{name}
%{py_platsitedir}/*.egg-info
%{py_platsitedir}/bt2
