# IUS spec file for uwsgi-plugin-php70u
#
# This package is intended to work with uwsgi from EPEL and php70u from IUS.
# It should remain at the same version as the EPEL uwsgi package to ensure
# compatibility.

%global php php70u

Name: uwsgi-plugin-%{php}
Version: 2.0.14
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
Requires: uwsgi-plugin-common = %{version}

%{?filter_provides_in: %filter_provides_in %{_libdir}/uwsgi/.*\.so$}
%{?filter_setup}


%description
This package contains the PHP plugin for uWSGI.  Designed to work with the
uwsgi packages in EPEL, but built against %{php} from IUS.


%prep
%setup -q -c -T
cp -a %{_usrsrc}/uwsgi/%{version}/plugins/php .


%build
export CFLAGS="%{optflags} -Wno-unused-but-set-variable"
uwsgi --build-plugin "php %{php}"


%install
install -D -p -m 0755 %{php}_plugin.so %{buildroot}%{_libdir}/uwsgi/%{php}_plugin.so


%files
%{_libdir}/uwsgi/%{php}_plugin.so


%changelog
* Wed Oct 12 2016 Carl George <carl.george@rackspace.com> - 2.0.14-1.ius
- Rebuild against uwsgi 2.0.14

* Wed Aug 10 2016 Carl George <carl.george@rackspace.com> - 2.0.13.1-1.ius
- Rebuild against uwsgi 2.0.13.1

* Wed Jul 06 2016 Carl George <carl.george@rackspace.com> - 2.0.12-1.ius
- Initial package
