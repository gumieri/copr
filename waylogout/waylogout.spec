Name:           waylogout
Version:        1.0
Release:        1%{?dist}
Summary:        Graphical logout/suspend/reboot/shutdown dialog for Wayland

License:        MIT
URL:            https://github.com/loserMcloser/waylogout
Source0:        %{url}/archive/mainline.tar.gz

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
%autosetup -n %{name}-mainline

%build
%meson -Dwerror=false --auto-features=auto
%meson_build

%install
%meson_install

%check
%meson_test

%files
%{_bindir}/waylogout
%{_datadir}/bash-completion/completions/waylogout
%{_datadir}/fish/vendor_completions.d/waylogout.fish
%{_datadir}/zsh/site-functions/_waylogout

%{_mandir}/man1/waylogout.1.gz

%license LICENSE
%doc README.*

%changelog
* Wed Jan 05 2022 Rafael Gumieri <rafael@gumieri.com> - 1.0-1
- RPM release of waylogout
