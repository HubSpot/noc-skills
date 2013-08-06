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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-build
URL:       https://github.com/HubSpot/noc-skills
BuildArch: noarch
Requires:  mongodb-server

%description
The Mongo database portion of the Noc Skills Test

%prep

%build

%install

%pre

%post

%files

