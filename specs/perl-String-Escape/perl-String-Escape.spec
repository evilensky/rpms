# $Id$

# Authority: dries
# Upstream: Matthew Simon Cavalletto <simonm$cavalletto,org>

%define real_name String-Escape
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Registry of string functions, including backslash escapes
Name: perl-String-Escape
Version: 2002.001
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Escape/

Source: http://www.cpan.org/modules/by-module/String/String-Escape-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module provides a flexible calling interface to some
frequently-performed string conversion functions, including applying
and expanding standard C/Unix-style backslash escapes like \n and \t,
wrapping
and removing double-quotes, and truncating to fit within a desired length.

The escape() function provides for dynamic selection of operations by
using a package hash variable to map escape specification strings to the
functions which implement them. The lookup imposes a bit of a performance
penalty, but allows for some useful late-binding behaviour. Compound
specifications (ex. 'quoted uppercase') are expanded to a list of
functions to be applied in order. Other modules may also register their
functions here for later general use.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/String/Escape.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2002.001-1.2
- Rebuild for Fedora Core 5.

* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 2002.001-1
- Initial package.
