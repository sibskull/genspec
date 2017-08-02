%define  modulename $module

Name:    python3-module-%modulename
Version: $version
Release: alt1

Summary: $summary
License: $license
Group:   Development/Python3
URL:     $url

Packager: $packager

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev

BuildArch: noarch

Source:  %modulename-%version.tar

%description
$description

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
$stamp-alt1
$lastchange
