#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Session-Wrapper
Summary:	Apache::Session::Wrapper - A simple wrapper around Apache::Session
Summary(pl):	Apache::Session::Wrapper - prosty wrapper na Apache::Session
Name:		perl-Apache-Session-Wrapper
Version:	0.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3da1330b76d1305bde3bbfee7e82ae17
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Apache-Session >= 1.6
BuildRequires:	perl-Class-Container
BuildRequires:	perl-Exception-Class
BuildRequires:	perl-Params-Validate >= 0.7
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a simple wrapper around Apache::Session which provides
some methods to simplify getting and setting the session id.

%description -l pl
Ten moduł jest prostym wrapperem na Apache::Session dostarczającym
metody upraszczające uzyskiwanie i ustawianie identyfikatorów sesji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Apache/*/*.pm
%{_mandir}/man3/*
