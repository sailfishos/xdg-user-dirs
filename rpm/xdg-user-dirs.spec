Name:       xdg-user-dirs
Summary:    Handles user special directories
Version:    0.20
Release:    1
License:    GPLv2
URL:        https://github.com/sailfishos/xdg-user-dirs
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  gettext
BuildRequires:  meson

%description
Contains xdg-user-dirs-update that updates folders in a users
homedirectory based on the defaults configured by the administrator.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%meson -Ddocs=false
%meson_build

%install
%meson_install

rm %{buildroot}/etc/xdg/autostart/xdg-user-dirs.desktop
rm %{buildroot}/%{_prefix}/lib/systemd/user/xdg-user-dirs.service

%find_lang %name

%files -f %name.lang
%license COPYING
%{_bindir}/*
%config %{_sysconfdir}/xdg/user-dirs.conf
%config %{_sysconfdir}/xdg/user-dirs.defaults
