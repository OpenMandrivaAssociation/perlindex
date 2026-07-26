%define upstream_name    perlindex
Name:		%{upstream_name}
Version:	1.606
Release:	2

Summary:	English language stemming
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/perlindex
Source0:	https://cpan.metacpan.org/authors/id/U/UL/ULPFR/perlindex-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This routine applies the Porter Stemming Algorithm to its parameters,
returning the stemmed words. It is derived from the C program "stemmer.c"
as found in freewais and elsewhere, which contains these notes:

   Purpose:    Implementation of the Porter stemming algorithm documented 
               in: Porter, M.F., "An Algorithm For Suffix Stripping," 
               Program 14 (3), July 1980, pp. 130-137.
   Provenance: Written by B. Frakes and C. Cox, 1986.

I have re-interpreted areas that use Frakes and Cox's "WordSize" function.
My version may misbehave on short words starting with "y", but I can't
think of any examples.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

# %check
# %make test

%install
%makeinstall_std

%files
%doc ChangeLog META.yml README
%{_bindir}/*
%{_mandir}/man?/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.605.0-2mdv2011.0
+ Revision: 658675
- update file list
- rebuild for updated spec-helper

* Tue May 18 2010 Jérôme Quelin <jquelin@mandriva.org> 1.605.0-1mdv2011.0
+ Revision: 545246
- import perlindex


* Tue May 18 2010 cpan2dist 1.605-1mdv
- initial mdv release, generated with cpan2dist
