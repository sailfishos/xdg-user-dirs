Name:		xdg-user-dirs
Version:	0.12
Release:	2
Summary:	Handles user special directories

Group:		User Interface/Desktops
License:	GPL
URL:		http://www.freedesktop.org/wiki/Software/xdg-user-dirs
Source0:	http://user-dirs.freedesktop.org/releases/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gettext

Patch0:		xdg-user-dirs-desktop-moblin.patch
# use fuzzy translations (for Downloads)
# https://bugzilla.redhat.com/show_bug.cgi?id=532399
Patch1:		use-fuzzy.patch
# fix a typo in README
Patch2:		typo.patch
Patch3:         meego-use-fuzzy-translations.patch
Patch4:         meego-bmc1989-new-picture-names-for-meego-sample-media.patch


%description
Contains xdg-user-dirs-update that updates folders in a users
homedirectory based on the defaults configured by the administrator.

%prep
%setup -q

%patch0 -p1 -b .desktop-moblin
%patch1 -p1 -b .use-fuzzy
%patch2 -p1 -b .typo
%patch3 -p1 -b .meego-use-fuzzy-translations
%patch4 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc NEWS AUTHORS README ChangeLog COPYING
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.conf
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.defaults
