# TODO: programs shouldn't have ".py" extension
%define 	module	ctypesgen
%define		snap	20150512
%define		gitref	3d2d9803339503d2988382aa861b47a6a4872c32
%define		rel	1
Summary:	A pure-python wrapper generator for ctypes
Summary(pl.UTF-8):	Generator wrapperów dla ctypes napisany w czystym Pythonie
Name:		python-%{module}
Version:	0.0
Release:	1.%{snap}.%{rel}
License:	BSD
Group:		Libraries/Python
Source0:	https://github.com/davidjamesca/ctypesgen/archive/%{gitref}/%{module}-%{snap}.tar.gz
# Source0-md5:	abbc70e2fb7c5391ade6b56bd503c6ed
URL:		https://github.com/davidjamesca/ctypesgen
BuildRequires:	python >= 1:2.3
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project automatically generates ctypes wrappers for header files
written in C.

%description -l pl.UTF-8
Ten program automatycznie generuje wrappery ctypes dla plików
nagłówkowych w C.

%prep
%setup -q -n %{module}-%{gitref}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

# defaultheader.py and preamble.py are templates not modules, so .py files
# are required instead of compiled versions
# libraryloader.py is used both as module and template, so both forms are required
%py_postclean -x defaultheader.py,preamble.py,libraryloader.py
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/ctypesgencore/printer_python/{defaultheader,preamble}.py[co]

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE todo.txt
%attr(755,root,root) %{_bindir}/ctypesgen.py
%{py_sitescriptdir}/ctypesgen-0.0-py*.egg-info
%dir %{py_sitescriptdir}/ctypesgencore
%{py_sitescriptdir}/ctypesgencore/*.py[co]
%{py_sitescriptdir}/ctypesgencore/libraryloader.py
%dir %{py_sitescriptdir}/ctypesgencore/parser
%{py_sitescriptdir}/ctypesgencore/parser/*.py[co]
%dir %{py_sitescriptdir}/ctypesgencore/printer_json
%{py_sitescriptdir}/ctypesgencore/printer_json/*.py[co]
%dir %{py_sitescriptdir}/ctypesgencore/printer_python
%{py_sitescriptdir}/ctypesgencore/printer_python/__init__.py[co]
%{py_sitescriptdir}/ctypesgencore/printer_python/printer.py[co]
%{py_sitescriptdir}/ctypesgencore/printer_python/test.py[co]
%{py_sitescriptdir}/ctypesgencore/printer_python/defaultheader.py
%{py_sitescriptdir}/ctypesgencore/printer_python/preamble.py
%dir %{py_sitescriptdir}/ctypesgencore/processor
%{py_sitescriptdir}/ctypesgencore/processor/*.py[co]
