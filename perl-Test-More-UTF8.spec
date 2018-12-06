#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-More-UTF8
Version  : 0.05
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/M/MO/MONS/Test-More-UTF8-0.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MO/MONS/Test-More-UTF8-0.05.tar.gz
Summary  : 'Enhancing Test::More for UTF8-based projects'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
NAME
Test::More::UTF8 - Enhancing Test::More for UTF8-based projects
SYNOPSIS
use Test::More;
use Test::More::UTF8;

%package dev
Summary: dev components for the perl-Test-More-UTF8 package.
Group: Development
Provides: perl-Test-More-UTF8-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-More-UTF8 package.


%prep
%setup -q -n Test-More-UTF8-0.05

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Test/More/UTF8.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::More::UTF8.3
