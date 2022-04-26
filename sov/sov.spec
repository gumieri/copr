Name:           sov
Version:        0.61
Release:        1%{?dist}
Summary:        An overlay that shows schemas for all workspaces to make navigation in sway easier

License:        MIT
URL:            https://github.com/milgra/sov
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

# https://www.reddit.com/r/swaywm/comments/ubsw9a/comment/i68zfjz/?utm_source=reddit&utm_medium=web2x&context=3
Patch100:       a.patch

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  ftgl-devel
BuildRequires:  clang
BuildRequires:  meson
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
Recommends:     sway

%description
Sway Overview. An overlay that shows schemas for all workspaces to make navigation in sway easier. Used by SwayOS.

%prep
%autosetup -n %{name}-%{version}

%build
%meson -Dwerror=false --auto-features=auto
%meson_build

%install
%meson_install

%check
%meson_test

%files
%{_bindir}/sov
%{_datadir}/sov/config

%license LICENSE
%doc README.*

%changelog
* Tue Apr 26 2022 Rafael Gumieri <rafael@gumieri.com> - 0.61-1
- RPM release of sov
