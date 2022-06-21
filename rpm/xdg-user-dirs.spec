Name:       xdg-user-dirs
Summary:    Handles user special directories
Version:    0.16
Release:    1
Group:      User Interface/Desktops
License:    GPLv2
URL:        https://github.com/sailfishos/xdg-user-dirs
Source0:    %{name}-%{version}.tar.gz
Patch0:     use-fuzzy.patch
Patch1:     meego-use-fuzzy-translations.patch
BuildRequires:  gettext

%description
Contains xdg-user-dirs-update that updates folders in a users
homedirectory based on the defaults configured by the administrator.

%package lang
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
%description lang
Development files for %{name}

%prep
%setup -q -n %{name}-%{version}/%{name}

# use-fuzzy.patch
%patch0 -p1
# meego-use-fuzzy-translations.patch
%patch1 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static --disable-documentation
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

rm %{buildroot}/etc/xdg/autostart/xdg-user-dirs.desktop

%find_lang %name

%files -f %name.lang
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/*
%config %{_sysconfdir}/xdg/user-dirs.conf
%config %{_sysconfdir}/xdg/user-dirs.defaults

%files lang
%defattr(-,root,root,-)


