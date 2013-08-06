%define hubspot_base /usr/share/hubspot
%define version 0.1

Name:      noc-skills-mongo
Summary:   The MongoDB portion of the HubSpot NOC Skills test
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
Requires:  mongodb-server

%description
The Mongo database portion of the Noc Skills Test

%prep
%setup -q -n NocSkillsMongo

%build

%install
install -d -m 755 ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsMongo
install -m 644 %{_builddir}/NocSkillsMongo/resources/initial-data.json ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsMongo/

%pre

%post
/sbin/chkconfig --add mongod
/sbin/chkconfig mongod on
/etc/init.d/mongod start
sleep 5 # give mongo a chance to start up
mongoimport --db nocskills --collection Reason < /usr/share/hubspot/NocSkillsMongo/initial-data.json


%files
%defattr(-,root,root)
/usr/share/hubspot/NocSkillsMongo/initial-data.json
