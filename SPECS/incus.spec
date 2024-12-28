%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post %{nil}

Name:           incus
Version:        6.8.0
Release:        1%{?dist}
Summary:        Container and Virtual Machine Manager

License:        ASL 2.0
URL:            https://github.com/lxc/incus
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  raft-devel >= 0.17.1
BuildRequires:  cowsql-devel >= 1.15.6

Requires:       raft >= 0.17.1
Requires:       cowsql >= 1.15.6
Requires:       lvm2
Requires:       sqlite
Requires:       libuv

%description
Container and virtual machine manager built with our verified dependencies

%prep
%autosetup

%build
# Skip rebuild as we're packaging pre-built files

%install
# Install binaries
mkdir -p %{buildroot}%{_bindir}
cp -a bin/* %{buildroot}%{_bindir}/

# Install systemd service
mkdir -p %{buildroot}%{_unitdir}
cp systemd/incus.service %{buildroot}%{_unitdir}/

# Create directories
mkdir -p %{buildroot}%{_sharedstatedir}/incus

%post
%systemd_post incus.service

%preun
%systemd_preun incus.service

%postun
%systemd_postun_with_restart incus.service

%files
%{_bindir}/incus*
%{_unitdir}/incus.service
%dir %{_sharedstatedir}/incus

%changelog
* Tue Dec 12 2023 Root User <root@melanee-desk> - 6.8.0-1
- Initial package built for AlmaLinux 10
