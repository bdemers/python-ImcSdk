%global package_name ImcSdk
%global sum Python SDK for Cisco IMC 

Name:           python-%{package_name}
Version:        0.7.2
Release:        3%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{package_name}
Source0:        https://pypi.python.org/packages/source/I/%{package_name}/%{package_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python3-devel
BuildRequires:  python-sphinx

%description
Python development kit for Cisco IMC

%package -n python2-%{package_name}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{package_name}}

%description -n python2-%{package_name}
Python development kit for Cisco IMC

%prep
%autosetup -n %{package_name}-%{version}

# Kill egg-info in order to generate new SOURCES.txt
rm -rf ImcSdk.egg-info

# TODO: doc build needs a little work: https://github.com/CiscoUcs/ImcSdk/issues/4
rm docs/ImcSdk.rst docs/modules.rst

%build
%{__python2} setup.py build

# generate doc
sphinx-apidoc -o docs/ ImcSdk
# remove sphinx config.py from docs dir
rm docs/conf.py

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

# TODO: fix test execution downstream (https://github.com/CiscoUcs/ImcSdk/pull/3/)
# %check
# %{__python2} setup.py test

%files -n python2-%{package_name}
%{python2_sitelib}/%{package_name}/
%{python2_sitelib}/%{package_name}*.egg-info
%doc README.rst
%doc docs/
%license LICENSE

%changelog
* Tue Jan 12 2016 Brian Demers <brdemers@cisco.com> 0.7.2-3
- removing doc config.py from rpm 
* Mon Jan 11 2016 Brian Demers <brdemers@cisco.com> 0.7.2-2
- Updating to use a python2 package, to allow for future python3 
* Mon Dec 21 2015 Brian Demers <brdemers@cisco.com> 0.7.2-1
- Initial RPM release

