%define upstream_name    Padre-Plugin-HTML
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	L<Padre> and HTML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Lint)
BuildRequires:	perl(HTML::Tidy)
BuildRequires:	perl(Padre)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(WebService::Validator::HTML::W3C)
BuildRequires:	perl(XML::XPath)
BuildRequires:	perl(Module::Build::Compat)

BuildArch:	noarch

%description
HTML plugin for Padre

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 653611
- rebuild for updated spec-helper

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 573858
- skip test (padre plugin tests fail)
- update to 0.10

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 444021
- import perl-Padre-Plugin-HTML


* Thu Sep 17 2009 cpan2dist 0.09-1mdv
- initial mdv release, generated with cpan2dist
