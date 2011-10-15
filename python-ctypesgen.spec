# TODO: programs shouldn't have ".py" extension
%define 	module	ctypesgen
%define		snap	r69
%define		rel	4
Summary:	A pure-python wrapper generator for ctypes
Summary(pl.UTF-8):	Generator wrapperów dla ctypes napisany w czystym Pythonie
Name:		python-%{module}
Version:	0.0
Release:	0.%{snap}.%{rel}
License:	BSD
Group:		Libraries/Python
# svn export http://ctypesgen.googlecode.com/svn/trunk/ ctypesgen
Source0:	%{module}-%{snap}.tar.bz2
# Source0-md5:	73192491f45126a1681bd1a7553506d1
URL:		http://code.google.com/p/ctypesgen/
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
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
%setup -q -n %{module}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
        --root=$RPM_BUILD_ROOT \
        --optimize=2

# defaultheader.py and preamble.py are templates not modules, so .py files
# are required instead of compiled versions (and py_postclean cannot be used)
# libraryloader.py is used both as module and template, so both forms are required
find $RPM_BUILD_ROOT%{py_sitescriptdir}/ctypesgencore -name '*.py' -a ! -name 'defaultheader.py' -a ! -name 'preamble.py' -a ! -name 'libraryloader.py' -print0 | xargs -0 %{__rm}
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/ctypesgencore/printer/{defaultheader,preamble}.py[co]

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
%dir %{py_sitescriptdir}/ctypesgencore/printer
%{py_sitescriptdir}/ctypesgencore/printer/__init__.py[co]
%{py_sitescriptdir}/ctypesgencore/printer/printer.py[co]
%{py_sitescriptdir}/ctypesgencore/printer/test.py[co]
%{py_sitescriptdir}/ctypesgencore/printer/defaultheader.py
%{py_sitescriptdir}/ctypesgencore/printer/preamble.py
%dir %{py_sitescriptdir}/ctypesgencore/processor
%{py_sitescriptdir}/ctypesgencore/processor/*.py[co]
