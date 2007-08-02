# $Id$

# Authority: dries
# Upstream: Steven McDougall <swmcd$world,std,com>

%define real_name Set-IntSpan
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Manages sets of integers
Name: perl-Set-IntSpan
Version: 1.11
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Set-IntSpan/

Source: http://www.cpan.org/modules/by-module/Set/Set-IntSpan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Set::IntSpan manages sets of integers.  It is optimized for sets that
have long runs of consecutive integers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Set/IntSpan.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.09-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Updated to release 1.09.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.
