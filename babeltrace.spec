%define devname %mklibname -d babeltrace

Summary:	An open source trace format converter
Name:		babeltrace
Version:	1.5.1
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		http://diamon.org/babeltrace
Source0:	http://www.efficios.com/files/babeltrace/babeltrace-%{version}.tar.bz2
Patch0:		babeltrace-1.5.1-fix-linkage.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libdw)
BuildRequires:	pkgconfig(libelf)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(popt)
BuildRequires:	swig

%libpackage babeltrace 1
%libpackage babeltrace-lttng-live 1
%libpackage babeltrace-dummy 1
%libpackage babeltrace-ctf 1
%libpackage babeltrace-ctf-metadata 1
%libpackage babeltrace-ctf-text 1

%description
An open source trace format converter

%package -n %{devname}
Summary:	Development files for the babeltrace trace format converter
Group:		Development/Other
Requires:	%mklibname babeltrace 1
Requires:	%mklibname babeltrace-lttng-live 1
Requires:	%mklibname babeltrace-dummy 1
Requires:	%mklibname babeltrace-ctf 1
Requires:	%mklibname babeltrace-ctf-metadata 1
Requires:	%mklibname babeltrace-ctf-text 1

%description -n %{devname}
Development files for the babeltrace trace format converter

%package -n python-%{name}
Summary:	Python bindings to the babeltrace trace format converter
Group:		Development/Python

%description -n python-%{name}
Python bindings to the babeltrace trace format converter

%prep
%setup -q
%apply_patches
%configure --enable-python-bindings

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/babeltrace
%{_bindir}/babeltrace-log

%files -n %{devname}
%{_includedir}/babeltrace
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/*
%doc %{_docdir}/%{name}/*

%files -n python-%{name}
%{py_sitedir}/__pycache__
%{py_sitedir}/_babeltrace.so*
%{py_sitedir}/babeltrace.py
