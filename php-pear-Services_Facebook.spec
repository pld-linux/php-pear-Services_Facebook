%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Facebook
%define		_status		alpha
%define		_pearname	Services_Facebook
Summary:	%{_pearname} - PHP interface to Facebook's API
Summary(pl.UTF-8):	%{_pearname} - interfejs PHP do API Facebook
Name:		php-pear-%{_pearname}
Version:	0.2.14
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fb7b77b23e74bde284d287548f40cb51
URL:		http://pear.php.net/package/Services_Facebook/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4.0
Requires:	php-pear-Validate >= 0.0.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interface for accessing Facebook's web services API at
http://api.facebook.com.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Interfejs dostępowy do usług Facebook (http://api.facebook.com/).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Services_Facebook/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Facebook
%{php_pear_dir}/Services/Facebook.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_Facebook
