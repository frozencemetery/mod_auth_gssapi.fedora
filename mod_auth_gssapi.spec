Name:           mod_auth_gssapi
Version:        1.5.0
Release:        1%{?dist}
Summary:        A GSSAPI Authentication module for Apache

Group:          System Environment/Daemons
License:        MIT
URL:            https://github.com/modauthgssapi/mod_auth_gssapi
Source0:        https://github.com/modauthgssapi/%{name}/releases/download/v%{version}/%name-%{version}.tar.gz

BuildRequires:  httpd-devel, krb5-devel, openssl-devel, autoconf, automake, libtool
BuildRequires:  gssntlmssp-devel
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
* Mon Jan 16 2017 Simo Sorce <simo@redhat.com> - 1.5.0-1
- Last listoff of Space Shuttle Columbia release (1.5.0)

* Mon Nov 14 2016 Joe Orton <jorton@redhat.com> - 1.4.1-2
- rebuild for new OpenSSL

* Mon Aug 15 2016 Robbie Harwood <rharwood@redhat.com> 1.4.1-1
- Mishka & Chizhik fly on a rocket release (1.4.1)
- Fix bogus changelog date

* Fri Jun 17 2016 Simo Sorce <simo@redhat.com> 1.4.0-1
- Lunar Reconnaissance Orbiter (2009) release (1.4.0)

* Mon Feb 22 2016 Simo Sorce <simo@redhat.com> 1.3.2-1
- NEAR Shoemaker launch (1996) release (1.3.2)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep  3 2015 Simo Sorce <simo@redhat.com> 1.3.1-1
- Viking 2 landing (1976) release (1.3.1)

* Tue Jul  7 2015 Simo Sorce <simo@redhat.com> 1.3.0-2
- Fix annoying incorrect behavior with simple configuration where
  GssapiAllowedMech is not used.

* Sat Jul  4 2015 Simo Sorce <simo@redhat.com> 1.3.0-1
- US Independence Day Release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Simo Sorce <simo@redhat.com> 1.2.0-1
- New minor release 1.2.0
- Adds delegation support on Basic Auth
- Response fix, send last auth token on successful auth

* Tue Mar 31 2015 Simo Sorce <simo@redhat.com> 1.1.0-3
- Fix some authentication issues

* Thu Mar 26 2015 Simo Sorce <simo@redhat.com> 1.1.0-2
- Fix saving delegated credentials for SPNs

* Thu Mar 12 2015 Simo Sorce <simo@redhat.com> 1.1.0-1
- New minor release 1.1.0
- New feature: Basic Auth support
- Improvements: Better crypto for sesison cookies

* Sat Nov  8 2014 Simo Sorce <simo@redhat.com> 1.0.4-1
- Patch release 1.0.4
- logging initialization fixes
- additional build fixes

* Sat Oct 11 2014 Simo Sorce <simo@redhat.com> 1.0.3-1
- Patch release 1.0.3
- fixes some build issues on various distros

* Wed Aug 27 2014 Simo Sorce <simo@redhat.com> 1.0.2-1
- Adds documntation to README
- fixes bad bug that crippled configuration

* Thu Aug 14 2014 Simo Sorce <simo@redhat.com> 1.0.1-1
- Patch release 1.0.1

* Mon Aug  4 2014 Simo Sorce <simo@redhat.com> 1.0.0-1
- First release
