Name:       xdg-user-dirs
Summary:    Handles user special directories
Version:    0.17
Release:    1
License:    GPLv2
URL:        http://www.freedesktop.org/wiki/Software/xdg-user-dirs
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  gettext

%description
Contains xdg-user-dirs-update that updates folders in a users
homedirectory based on the defaults configured by the administrator.

%package lang
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
%description lang
Development files for %{name}

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static --disable-documentation
%make_build

%install
rm -rf %{buildroot}
%make_install

rm %{buildroot}/etc/xdg/autostart/xdg-user-dirs.desktop

%find_lang %name

%files -f %name.lang
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/*
%config %{_sysconfdir}/xdg/user-dirs.conf
%config %{_sysconfdir}/xdg/user-dirs.defaults

%files lang
%defattr(-,root,root,-)


