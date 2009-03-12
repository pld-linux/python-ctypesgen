
%define 	module	ctypesgen
%define		snap	r68
Summary:	A pure-python wrapper generator for ctypes
Name:		python-%{module}
Version:	0.0
Release:	0.%{snap}.1
License:	BSD
Group:		Libraries/Python
Source0:	%{module}-%{snap}.tar.bz2
# Source0-md5:	5deda4849c2677beb054ec1b59aba5a9
URL:		http://code.google.com/p/ctypesgen/
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project automatically generates ctypes wrappers for header files
written in C.

%prep
%setup -q -n %{module}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
        --root=$RPM_BUILD_ROOT \
        --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.egg-info
%dir %{py_sitescriptdir}/ctypesgencore
%{py_sitescriptdir}/ctypesgencore/*.py[co]
%dir %{py_sitescriptdir}/ctypesgencore/parser
%{py_sitescriptdir}/ctypesgencore/parser/*.py[co]
%dir %{py_sitescriptdir}/ctypesgencore/printer
%{py_sitescriptdir}/ctypesgencore/printer/*.py[co]
%dir %{py_sitescriptdir}/ctypesgencore/processor
%{py_sitescriptdir}/ctypesgencore/processor/*.py[co]
%attr(755,root,root) %{_bindir}/ctypesgen.py
