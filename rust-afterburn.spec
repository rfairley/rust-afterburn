# Generated by rust2rpm
%bcond_without check

%global crate afterburn
%global cargo_registry ./vendor

Name:           rust-%{crate}
Version:        4.1.0
Release:        1%{?dist}
Summary:        A simple cloud-provider agent

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/afterburn
Source0:        %{crates_source}
Source1:        https://github.com/coreos/afterburn/releases/download/v%{version}/%{crate}-%{version}-vendor.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description \
A simple cloud provider agent

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate}
%{summary}.

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/afterburn
%{_unitdir}/afterburn.service
%{_unitdir}/afterburn-checkin.service
%{_unitdir}/afterburn-firstboot-checkin.service
%{_unitdir}/afterburn-sshkeys@.service

%prep
%autosetup -n %{crate}-%{version_no_tilde} -a 1
set -eu
%{__mkdir} -p .cargo
%{__cat} > .cargo/config << EOF
[build]
rustc = "rustc"
rustdoc = "rustdoc"
rustflags = %{__global_rustflags_toml}

[term]
verbose = true

[source]

[source.local-registry]
directory = "%{cargo_registry}"

[source.crates-io]
registry = "https://crates.io"
replace-with = "local-registry"
EOF
%cargo_prep

%build
%cargo_build

%install
%cargo_install
%{__install} -Dpm0644 -t %{buildroot}%{_unitdir} \
  systemd/afterburn.service
%{__install} -Dpm0644 -t %{buildroot}%{_unitdir} \
  systemd/afterburn-checkin.service
%{__install} -Dpm0644 -t %{buildroot}%{_unitdir} \
  systemd/afterburn-firstboot-checkin.service
# Based on https://github.com/coreos/afterburn/blob/master/Makefile
sed -e 's,@DEFAULT_INSTANCE@,'core',' < \
  systemd/afterburn-sshkeys@.service.in > \
  systemd/afterburn-sshkeys@.service.tmp
mv systemd/afterburn-sshkeys@.service.tmp \
  systemd/afterburn-sshkeys@.service
%{__install} -Dpm0644 -t %{buildroot}%{_unitdir} \
  systemd/afterburn-sshkeys@.service

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Tue Apr 23 2019 root - 4.1.0-1
- Initial package
