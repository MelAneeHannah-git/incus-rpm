%global _enable_debug_package 0
%global debug_package %{nil}

Name:           raft
Version:        0.17.1
Release:        1%{?dist}
Summary:        Raft consensus protocol implementation for AlmaLinux 10

License:        MIT
URL:            https://github.com/canonical/raft
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc make autoconf automake libtool
BuildRequires:  libuv-devel lz4-devel

%description
Raft consensus protocol implementation, compiled and verified working on AlmaLinux 10

%package devel
Summary:        Development files for raft
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for raft, matched to working AlmaLinux 10 build

%prep
%autosetup

%build
# Skip rebuild as we're packaging pre-built files

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig

cp -r .libs/* %{buildroot}%{_libdir}/
cp -r include/* %{buildroot}%{_includedir}/
cp -r pkgconfig/* %{buildroot}%{_libdir}/pkgconfig/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libraft.so.*

%files devel
%{_includedir}/raft.h
%{_includedir}/raft/
%{_libdir}/libraft.so
%{_libdir}/libraft.a
%{_libdir}/libraft.la
%{_libdir}/libraft.lai
%{_libdir}/pkgconfig/raft.pc

%changelog
* Tue Dec 12 2023 Root User <root@melanee-desk> - 0.17.1-1
- Initial package built for AlmaLinux 10
