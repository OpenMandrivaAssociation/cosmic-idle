%undefine _debugsource_packages
Name:           cosmic-idle
Version:        1.0.0
Release:        0.alpha5.0
Summary:        Idle notify manager for COSMIC
License:        GPL-3.0-only
Group:          Utility/COSMIC
URL:            https://github.com/pop-os/cosmic-idle
Source0:        https://github.com/pop-os/cosmic-idle/archive/epoch-%{version}-alpha.5/%{name}-epoch-%{version}-alpha.5.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.5 -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%{_bindir}/%{name}
