# $Id$
# Authority: dries
# Upstream: Barbie <barbie$missbarbell,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Phrasebook-Loader-DBI

Summary: Absract your phrases with a DBI driver
Name: perl-Data-Phrasebook-Loader-DBI
Version: 0.16
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Phrasebook-Loader-DBI/

Source: http://www.cpan.org/modules/by-module/Data/Data-Phrasebook-Loader-DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Absract your phrases with a DBI driver.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Data::Phrasebook::Loader::DBI*
%{perl_vendorlib}/Data/Phrasebook/Loader/DBI.pm
%dir %{perl_vendorlib}/Data/Phrasebook/Loader/
%dir %{perl_vendorlib}/Data/Phrasebook/

%changelog
* Wed Sep 28 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.16-1
- Updated to release 0.16.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
