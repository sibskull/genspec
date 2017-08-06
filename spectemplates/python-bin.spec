Name:    $module
Version: $version
Release: alt1

Summary: $summary
License: $license
Group:   Other
URL:     $url

Packager: $packager

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

Source:  %name-%version.tar

%description
$description

%prep
%setup -n %name-%version

%build
%python_build

%install
%python_install

%files
%_bindir/%name
%python_sitelibdir/%name/
%python_sitelibdir/*.egg-info

%changelog
$stamp-alt1
$lastchange
