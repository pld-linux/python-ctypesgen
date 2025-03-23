#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	ctypesgen
Summary:	A pure-python wrapper generator for ctypes
Summary(pl.UTF-8):	Generator wrapperów dla ctypes napisany w czystym Pythonie
Name:		python-%{module}
Version:	1.0.2
Release:	7
License:	BSD
Group:		Libraries/Python
# only wheels on https://pypi.org/simple/ctypesgen so get from github
#Source0Download: https://github.com/davidjamesca/ctypesgen/releases
Source0:	https://github.com/davidjamesca/ctypesgen/archive/ctypesgen-%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	0928ef10a1f0323a82d55d6a0dfac8ff
Patch0:		%{name}-x32.patch
URL:		https://github.com/davidjamesca/ctypesgen
BuildRequires:	python >= 1:2.3
BuildRequires:	python-modules >= 1:2.3
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project automatically generates ctypes wrappers for header files
written in C.

%description -l pl.UTF-8
Ten program automatycznie generuje wrappery ctypes dla plików
nagłówkowych w C.

%prep
%setup -q -n %{module}-%{module}-%{version}
%patch -P 0 -p1

%build
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest -v -x --showlocals ctypesgen/test/testsuite.py
%endif

find ctypesgen -name '*.py[co]' | xargs %{__rm}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

# defaultheader.py and preamble.py are templates not modules, so .py files
# are required instead of compiled versions
# libraryloader.py is used both as module and template, so both forms are required
%py_postclean -x defaultheader.py,preamble/2_5.py,preamble/2_7.py,preable/3_2.py,libraryloader.py
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/ctypesgen/printer_python/defaultheader.py[co]
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/ctypesgen/printer_python/preamble/[23]_*.py[co]
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/ctypesgen/test

%{__mv} $RPM_BUILD_ROOT%{_bindir}/ctypesgen{,-2}

find ctypesgen -name '*.py[co]' | xargs %{__rm}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md todo.txt
%attr(755,root,root) %{_bindir}/ctypesgen-2
%{py_sitescriptdir}/ctypesgen
%{py_sitescriptdir}/ctypesgen-0.0.0-py*.egg-info
