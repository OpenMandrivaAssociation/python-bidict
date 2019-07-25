%define	module	bidict

Summary:	Bidirectional (one-to-one) mapping data structure for Python
Name:		python-bidict
Version:	0.18.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/8a/18/a3feb46d99a7a73c3078faf1c9b24655eace83bcf696cfecae46288cad8a/bidict-0.18.0.tar.gz
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


%files
%py_sitedir/%{module}*
