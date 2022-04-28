%global nvim_packer_dir %{_datadir}/nvim/site/pack/packer/start/packer.nvim/

Name:           nvim-packer
Version:        0.0.0.20220428
Release:        1%{?dist}
Summary:        use-package inspired plugin/package management for Neovim.

License:        MIT
URL:            https://github.com/wbthomason/packer.nvim
Source0:        %{url}/archive/master.tar.gz

BuildRequires:  git
Requires:       neovim


%description
%{summary}
Packer is built on native packages. You may wish to read :h packages before continuing

%prep
%autosetup -n %{name}-master

%install
mkdir -p %{nvim_packer_dir}
find doc lua -type f -exec install -Dm 644 "{}" "${nvim_packer_dir}/{}" \;


%check
%make_test

%files
%{nvim_packer_dir}
%license LICENSE
%doc README.*

%changelog
* Thu Apr 28 2022 Rafael Gumieri <rafael@gumieri.com> - 1.0-1
- RPM release of nvim-packer
