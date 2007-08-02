# $Id$
# Authority: dries
# Upstream: Dave Cardwell <dcardwell$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Provider-DBIC

Summary: Load templates using DBIx::Class
Name: perl-Template-Provider-DBIC
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Provider-DBIC/

Source: http://search.cpan.org//CPAN/authors/id/D/DC/DCARDWELL/Template-Provider-DBIC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Load templates using DBIx::Class.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/Template::Provider::DBIC*
%{perl_vendorlib}/Template/Provider/DBIC.pm
%dir %{perl_vendorlib}/Template/Provider/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
