%define	module	bidict
%define name	python-%{module}
%define version 0.1.1
%define	rel	1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release	%{rel}
%endif

Summary:	Bidirectional (one-to-one) mapping data structure for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://bitbucket.org/jab/bidict/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel, python-setuptools

%description
bidict provides a bidirectional mapping data structure and related
utilities (namedbidict, inverted) to naturally model one-to-one
relations in Python. To keep the learning curve low, it introduces no
new functions to the dict API you're already familiar with. It owes
its simplicity to Python's slice syntax, which provides a handy and
natural way of expressing the inverse mapping in a bidict.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%py_sitedir/%{module}*
