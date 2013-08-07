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
Requires:  noc-skills-mongo-10gen-repo, mongo-10gen, mongo-10gen-server
BuildArch: noarch

%description
The Mongo database portion of the Noc Skills Test

%package 10gen-repo
Summary: The 10gen repo file so that we can install their package
Group: Misc
%description 10gen-repo
Package that ensures that the 10gen repo file is installed

%prep
%setup -q -n NocSkillsMongo

%build

%install
install -d -m 755 ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsMongo
install -d -m 755 ${RPM_BUILD_ROOT}/etc/yum.repos.d/
install -m 644 %{_builddir}/NocSkillsMongo/resources/initial-data.json ${RPM_BUILD_ROOT}/usr/share/hubspot/NocSkillsMongo/
install -m 644 %{_builddir}/NocSkillsMongo/resources/10gen.repo ${RPM_BUILD_ROOT}/etc/yum.repos.d/

%post
echo "Running post-install for "
/sbin/chkconfig --add mongod
/sbin/chkconfig mongod on
/etc/init.d/mongod start
sleep 150 # give mongo a chance to start up, even on a micro instance.  Usually takes about 120 seconds, so pad
mongoimport --db nocskills --collection Reason < /usr/share/hubspot/NocSkillsMongo/initial-data.json


%files
%defattr(-,root,root)
/usr/share/hubspot/NocSkillsMongo/initial-data.json

%files 10gen-repo
%defattr(-,root,root)
/etc/yum.repos.d/10gen.repo
