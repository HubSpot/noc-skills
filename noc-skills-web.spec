%define hubspot_base /usr/share/hubspot
%define version 0.1

Name:      noc-skills-web
Summary:   The Web portion of the HubSpot NOC Skills test
Version:   %{version}
Release:   1
License:   GPL
Vendor:    HubSpot
Packager:  %packer
Group:     Misc
Source0:   %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-build
URL:       https://github.com/HubSpot/noc-skills
BuildArch: noarch
Requires:    Django14, python-gunicorn, python-setuptools, python-requests

%description
A simple test of skills recommended or necessary for a successful
NOC Engineer

%prep
%setup -q -n NocSkillsWeb

%build

%install
install -d -m 755 ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsWeb
install -d -m 755 ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsWeb/NocSkillsWeb
install -d -m 755 ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsWeb/NocSkillsWeb/templates
install -d -m 755 ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsWeb/NocSkillsWeb/static
install -d -m 755 ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsWeb/logs
install -d -m 755 ${RPM_BUILD_ROOT}/etc
install -d -m 755 ${RPM_BUILD_ROOT}/etc/gunicorn
install -d -m 755 ${RPM_BUILD_ROOT}/etc/init.d


install -m 755 %{_builddir}/NocSkillsWeb/manage.py ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsWeb/manage.py
install -m 644 %{_builddir}/NocSkillsWeb/NocSkillsWeb/*.py ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsWeb/NocSkillsWeb/
install -m 644 %{_builddir}/NocSkillsWeb/NocSkillsWeb/templates/* ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsWeb/NocSkillsWeb/templates/ || true
install -m 644 %{_builddir}/NocSkillsWeb/NocSkillsWeb/static/* ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsWeb/NocSkillsWeb/static/ || true
install -m 644 %{_builddir}/NocSkillsWeb/resources/NocSkillsWeb.init.sh ${RPM_BUILD_ROOT}/etc/init.d/NocSkillsWeb
install -m 644 %{_builddir}/NocSkillsWeb/resources/gunicorn.conf ${RPM_BUILD_ROOT}/etc/gunicorn/gunicorn.conf

%post
/sbin/chkconfig --add NocSkillsWeb
/sbin/chkconfig NocSkillsWeb off

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
/usr/share/hubspot/NocSkillsWeb/*
%attr(755,root,root) /etc/init.d/NocSkillsWeb
/etc/gunicorn/gunicorn.conf