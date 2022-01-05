Name:           swaylock
Version:        1.0
Release:        1%{?dist}
Summary:        Graphical logout/suspend/reboot/shutdown dialog for Wayland

License:        MIT
URL:            https://github.com/loserMcloser/waylogout
Source0:        %{url}/archive/master.tar.gz

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  clang
BuildRequires:  meson
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  cairo-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  scdoc
Requires:       libxkbcommon
Requires:       wayland
Requires:       cairo
Requires:       gdk-pixbuf2
Recommends:     sway
Recommends:     fontawesome-fonts

%description
Waylogout is graphical logout/suspend/reboot/shutdown dialog for Wayland. It is inspired by oblogout and based on code from swaylock-effects.

%prep
%autosetup

%build
%meson -Dwerror=false --auto-features=auto
%meson_build

%install
%meson_install

%check
%meson_test

%files
%{_bindir}/waylogout
%{_datadir}/completions/bash/waylogout
%{_datadir}/completions/fish/waylogout.fish
%{_datadir}/completions/zsh/_waylogout

%{_mandir}/man1/waylogout.1.gz

%license LICENSE
%doc README.*

%changelog
* wed Jan 5 2022 Rafael Gumieri <rafael@gumieri.com> - 1.0-1
- RPM release of waylogout