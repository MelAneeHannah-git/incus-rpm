%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post %{nil}

Name:           cowsql
Version:        1.15.6
Release:        1%{?dist}
Summary:        Distributed SQLite database engine for AlmaLinux 10

License:        MIT
URL:            https://github.com/cowsql/cowsql
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc make autoconf automake libtool chrpath
BuildRequires:  raft-devel >= 0.17.1
BuildRequires:  sqlite-devel libuv-devel

Requires:       raft >= 0.17.1

%description
Distributed SQLite database engine, compiled and verified working on AlmaLinux 10

%package devel
Summary:        Development files for cowsql
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       raft-devel >= 0.17.1

%description devel
Development files for cowsql, matched to working AlmaLinux 10 build

%prep
%autosetup

%build
# Skip rebuild as we're packaging pre-built files

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig

cp -r .libs/* %{buildroot}%{_libdir}/
cp include/cowsql.h %{buildroot}%{_includedir}/
cp -r pkgconfig/* %{buildroot}%{_libdir}/pkgconfig/

# Remove RPATH
chrpath -d %{buildroot}%{_libdir}/libcowsql.so.0.0.1

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libcowsql.so.*

%files devel
%{_includedir}/cowsql.h
%{_libdir}/libcowsql.so
%{_libdir}/libcowsql.a
%{_libdir}/libcowsql.la
%{_libdir}/libcowsql.lai
%{_libdir}/pkgconfig/cowsql.pc

%changelog
* Tue Dec 12 2023 Root User <root@melanee-desk> - 1.15.6-1
- Initial package built for AlmaLinux 10
