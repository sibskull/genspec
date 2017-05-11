%define gname github2spec

Name:     genspec
Version:  1.1.1
Release:  alt2

Summary:  Script for generation RPM spec file from template
License:  GPLv3+
Group:    System/Configuration/Packaging
URL: 	  http://altlinux.org/genspec
Packager: Andrey Cherepanov <cas@altlinux.org> 

BuildArch: noarch

BuildPrereq: rpm-build-ruby rpm-build-python3

Source:   %name-%version.tar

%description
Script for generation RPM spec file from template.

%prep
%setup

%install
install -Dm755 %name %buildroot%_bindir/%name
install -Dm755 %gname %buildroot%_bindir/%gname
mkdir -p %buildroot%_datadir/spectemplates
cp -av spectemplates/* %buildroot%_datadir/spectemplates/

%files
%_bindir/%name
%_bindir/%gname
%_datadir/spectemplates

%changelog
* Thu May 11 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.1-alt2
- Add rpm-build-ruby rpm-build-python3 to BuildPrereq

* Thu May 11 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.1-alt1
- Fix invocation of ./genspec instead of genspec

* Thu May 11 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.0-alt1
- Create script to get repository data from github and generate spec file

* Tue May 2 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.2-alt1
- Upgrade to python3

* Mon Apr 24 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.1-alt1
- Add interactive mode

* Fri Jan 30 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial publish
