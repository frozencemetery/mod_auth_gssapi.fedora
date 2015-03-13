Name:           mod_auth_gssapi
Version:        1.1.0
Release:        1%{?dist}
Summary:        A GSSAPI Authentication module for Apache

Group:          System Environment/Daemons
License:        MIT
URL:            https://github.com/modauthgssapi/mod_auth_gssapi
Source0:        https://github.com/modauthgssapi/%{name}/releases/download/v%{version}/%name-%{version}.tar.gz

BuildRequires:  httpd-devel, krb5-devel, openssl-devel, autoconf, automake, libtool
Requires:       httpd-mmn = %{_httpd_mmn}
Requires:       krb5-libs >= 1.11.5

%description
The mod_auth_gssapi module is an authentication service that implements the
SPNEGO based HTTP Authentication protocol defined in RFC4559.

%prep
%setup -q


%build
export APXS=%{_httpd_apxs}
autoreconf -fi
%configure
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_httpd_moddir}
install -m 755 src/.libs/%{name}.so %{buildroot}%{_httpd_moddir}

# Apache configuration for the module
echo "LoadModule auth_gssapi_module modules/mod_auth_gssapi.so" > 10-auth_gssapi.conf
mkdir -p %{buildroot}%{_httpd_modconfdir}
install -m 644 10-auth_gssapi.conf %{buildroot}%{_httpd_modconfdir}

%files
%doc
%defattr(-,root,root)
%doc README COPYING
%config(noreplace) %{_httpd_modconfdir}/10-auth_gssapi.conf
%{_httpd_moddir}/mod_auth_gssapi.so

%changelog
* Thu Mar 12 2015 Simo Sorce <simo@redhat.com> 1.1.0-1
- New minor release 1.1.0
- New feature: Basic Auth support
- Improvements: Better crypto for sesison cookies

* Sat Nov  8 2014 Simo Sorce <simo@redhat.com> 1.0.4-1
- Patch release 1.0.4
- logging initialization fixes
- build fixes

* Wed Aug 27 2014 Simo Sorce <simo@redhat.com> 1.0.2-1
- Adds documntation to README
- fixes bad bug that crippled configuration

* Thu Aug 14 2014 Simo Sorce <simo@redhat.com> 1.0.1-1
- Patch release 1.0.1

* Mon Aug  4 2014 Simo Sorce <simo@redhat.com> 1.0.0-1
- First release
