%include	/usr/lib/rpm/macros.php
%define		_class		Stream
%define		_subclass	Var
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - allows stream based access to any variable
Summary(pl.UTF-8):	%{_pearname} - oparty na strumieniu dostęp do dowolnej zmiennej
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b852891189314ad94517be8c8d77c231
URL:		http://pear.php.net/package/Stream_Var/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.3.2
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_pearname} can be registered as a stream with stream_register_wrapper
and allows stream based access to any variable in any scope. Arrays are
treated as directories, so it`s possible to replace temporary
directories and files in your applications with variables.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
%{_pearname} może być zarejestrowany jako strumień za pomocą funkcji
stream_register_wrapper i pozwala na oparty na strumieniu dostęp do
dowolnej zmiennej. Tablice są trakowane jako katalogi, więc możliwe jest
zastąpienie tymczasowych plików oraz katalogów w aplikacjach zmiennymi.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# don't care for tests
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
