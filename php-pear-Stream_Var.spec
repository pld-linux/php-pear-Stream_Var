%include	/usr/lib/rpm/macros.php
%define         _class          Stream
%define         _subclass       Var
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - allows stream based access to any variable
Summary(pl):	%{_pearname} - oparty na strumieniu dostêp do dowolnej zmiennej 
Name:		php-pear-%{_pearname}
Version:	0.2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f7ea10dcac8817c81180afc7c30ce9a8
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_pearname} can be registered as a stream with stream_register_wrapper 
and allows stream based access to any variable in any scope. Arrays are
treated as directories, so it`s possible to replace temporary
directories and files in your applications with variables.

This class has in PEAR status: %{_status}.

%description -l pl
%{_pearname} mo¿e byæ zarejestrowany jako strumieñ za pomoc± funkcji
stream_register_wrapper i pozwala na oparty na strumieniu dostêp do
dowolnej zmiennej. Tablice s± trakowane jako katalogi, wiêc mo¿liwe jest
zast±pienie tymczasowych plików oraz katalogów w aplikacjach zmiennymi.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
