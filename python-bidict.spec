%define	module	bidict

Summary:	Bidirectional (one-to-one) mapping data structure for Python
Name:		python-bidict
Version:	0.24.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/b/bidict/bidict-%{version}.tar.gz
License:	MPL-2.0
Group:		Development/Python
Url:		https://github.com/jab/bidict
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(uv-build)

%description
bidict provides a bidirectional mapping data structure and related
utilities (namedbidict, inverted) to naturally model one-to-one
relations in Python. To keep the learning curve low, it introduces no
new functions to the dict API you're already familiar with. It owes
its simplicity to Python's slice syntax, which provides a handy and
natural way of expressing the inverse mapping in a bidict.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%license LICENSE
%py_sitedir/%{module}*
