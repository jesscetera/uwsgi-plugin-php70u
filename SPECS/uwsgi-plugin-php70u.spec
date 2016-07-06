# IUS spec file for uwsgi-plugin-php70u
#
# This package is intended to work with uwsgi from EPEL and php70u from IUS.
# It should remain at the same version as the EPEL uwsgi package to ensure
# compatibility.

%global php php70u

Name: uwsgi-plugin-%{php}
Version: 2.0.12
Release: 1.ius%{?dist}
Summary: uWSGI - Plugin for PHP support
Group: System Environment/Daemons
License: GPLv2 with exceptions
URL: https://github.com/unbit/uwsgi
BuildRequires: uwsgi-devel = %{version}
BuildRequires: libxml2-devel
BuildRequires: %{php}-devel, %{php}-embedded
BuildRequires: libuuid-devel
BuildRequires: pcre-devel
BuildRequires: libedit-devel
BuildRequires: openssl-devel
BuildRequires: libcap-devel
BuildRequires: zlib-devel
Requires: uwsgi-plugin-common

%{?filter_provides_in: %filter_provides_in %{_libdir}/uwsgi/.*\.so$}
%{?filter_setup}


%description
This package contains the PHP plugin for uWSGI.  Designed to work with the
uwsgi packages in EPEL, but built against %{php} from IUS.


%prep
%setup -q -c -T


%build
export CFLAGS="%{optflags} -Wno-unused-but-set-variable"
uwsgi --build-plugin "%{_usrsrc}/uwsgi/%{version}/plugins/php %{php}"


%install
install -D -p -m 0755 %{php}_plugin.so %{buildroot}%{_libdir}/uwsgi/%{php}_plugin.so


%files
%{_libdir}/uwsgi/%{php}_plugin.so


%changelog
* Wed Jul 06 2016 Carl George <carl.george@rackspace.com> - 2.0.12-1.ius
- Initial package
