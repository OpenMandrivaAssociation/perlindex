%define upstream_name    perlindex
%define upstream_version 1.605

Name:       %{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    English language stemming
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/perlindex
/usr/share/man/man1/perlindex.1.lzma

