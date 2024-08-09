# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_without check
%global debug_package %{nil}

%global crate itoa

Name:           rust-itoa
Version:        1.0.11
Release:        1
Summary:        Fast integer primitive to string conversion
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/itoa
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust >= 1.36

%global _description %{expand:
Fast integer primitive to string conversion.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(itoa) = 1.0.11
Requires:       cargo
Requires:       rust >= 1.36

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(itoa/default) = 1.0.11
Requires:       cargo
Requires:       crate(itoa) = 1.0.11

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no-panic-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(itoa/no-panic) = 1.0.11
Requires:       (crate(no-panic/default) >= 0.1.0 with crate(no-panic/default) < 0.2.0~)
Requires:       cargo
Requires:       crate(itoa) = 1.0.11

%description -n %{name}+no-panic-devel %{_description}

This package contains library source intended for building other packages which
use the "no-panic" feature of the "%{crate}" crate.

%files       -n %{name}+no-panic-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
