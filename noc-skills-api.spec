%define hubspot_base /usr/share/hubspot
%define version 0.1

Name:      noc-skills-api
Summary:   The API portion of the HubSpot NOC Skills test
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
Requires:  python-pip, java-1.6.0

%description
A simple test of skills recommended or necessary for a successful
NOC Engineer, API portion

%prep
%setup -q -n NocSkillsAPI

%build

%install
install -d -m 755 ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsAPI
install -d -m 755 ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsAPI/bin
install -d -m 755 ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsAPI/logs
install -d -m 755 ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsAPI/conf
install -d -m 755 ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsAPI/lib
install -d -m 755 ${RPM_BUILD_ROOT}/etc
install -d -m 755 ${RPM_BUILD_ROOT}/etc/init.d

install -m 644 %{_builddir}/NocSkillsAPI/target/NocSkillsAPI-%{version}-SNAPSHOT.jar ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsAPI/lib/
install -m 644 %{_builddir}/NocSkillsAPI/resources/noc_skills_api.yml ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsAPI/conf/
install -m 755 %{_builddir}/NocSkillsAPI/resources/NocSkillsAPI.init.sh ${RPM_BUILD_ROOT}/etc/init.d/NocSkillsAPI
install -m 755 %{_builddir}/NocSkillsAPI/resources/dropwizard-init ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsAPI/bin/

%pre
/usr/bin/pip install daemon-runner
if [ $? -ne 0 ]; then
  echo "Unable to install the daemon-runner package from pip"
  exit 1
fi

%post
/sbin/chkconfig --add NocSkillsAPI
/sbin/chkconfig NocSkillsAPI on

%files
%defattr(-,root,root)
/usr/share/hubspot/NocSkillsAPI/lib/*
/usr/share/hubspot/NocSkillsAPI/conf/*
%attr(755,root,root) /usr/share/hubspot/NocSkillsAPI/bin/*
%attr(755,root,root) /etc/init.d/NocSkillsAPI