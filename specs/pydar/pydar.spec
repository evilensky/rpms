# $Id: $

# Authority: dries

# Far from finished, not to be released :)

Summary: far from finished attempt of a buildserver in python
Name: pydar
Version: 0.001
Release: 1
License: GPL
Group: Development/Tools
URL: NoUrlYet

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: pydar-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: mach
Requires: mach, coreutils
Requires: mach = 0.4.3

%description
Not finished, not to be released!

%prep
%setup -n pydar

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
# cat /usr/bin/mach | grep -v builtin > %{buildroot}/%{_datadir}/pydar/pydar/mach.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_sysconfdir}/rc.d/init.d/pydar-buildserver-master
%{_sysconfdir}/rc.d/init.d/pydar-buildserver-slave
%{_bindir}/dar-remote
%{_bindir}/dar-speccheck
%{_datadir}/pydar/*.py
%{_datadir}/pydar/pydar/*.py

%changelog
* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 0.001-1
- Initial package
