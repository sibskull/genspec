Name:    $module
Version: $version
Release: alt1

Summary: $summary
License: $license
Group:   Other
URL:     $url

Packager: $packager

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev

BuildArch: noarch

Source:  %name-%version.tar

%description
$description

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
$stamp-alt1
$lastchange
