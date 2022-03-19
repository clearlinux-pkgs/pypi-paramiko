#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9C29BC560041E930 (jeff@bitprophet.org)
#
Name     : pypi-paramiko
Version  : 2.10.3
Release  : 4
URL      : https://files.pythonhosted.org/packages/d4/93/1a1eb7f214e6774099d56153db9e612f93cb8ffcdfd2eca243fcd5bb3a78/paramiko-2.10.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/d4/93/1a1eb7f214e6774099d56153db9e612f93cb8ffcdfd2eca243fcd5bb3a78/paramiko-2.10.3.tar.gz
Source1  : https://files.pythonhosted.org/packages/d4/93/1a1eb7f214e6774099d56153db9e612f93cb8ffcdfd2eca243fcd5bb3a78/paramiko-2.10.3.tar.gz.asc
Summary  : SSH2 protocol library
Group    : Development/Tools
License  : LGPL-2.1
Requires: pypi-paramiko-license = %{version}-%{release}
Requires: pypi-paramiko-python = %{version}-%{release}
Requires: pypi-paramiko-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(bcrypt)
BuildRequires : pypi(cryptography)
BuildRequires : pypi(pynacl)
BuildRequires : pypi(six)

%description
|version| |python| |license| |ci| |coverage|
.. |version| image:: https://img.shields.io/pypi/v/paramiko
:target: https://pypi.org/project/paramiko/
:alt: PyPI - Package Version
.. |python| image:: https://img.shields.io/pypi/pyversions/paramiko
:target: https://pypi.org/project/paramiko/
:alt: PyPI - Python Version
.. |license| image:: https://img.shields.io/pypi/l/paramiko
:target: https://github.com/paramiko/paramiko/blob/main/LICENSE
:alt: PyPI - License
.. |ci| image:: https://img.shields.io/circleci/build/github/paramiko/paramiko/main
:target: https://app.circleci.com/pipelines/github/paramiko/paramiko
:alt: CircleCI
.. |coverage| image:: https://img.shields.io/codecov/c/gh/paramiko/paramiko
:target: https://app.codecov.io/gh/paramiko/paramiko
:alt: Codecov

%package license
Summary: license components for the pypi-paramiko package.
Group: Default

%description license
license components for the pypi-paramiko package.


%package python
Summary: python components for the pypi-paramiko package.
Group: Default
Requires: pypi-paramiko-python3 = %{version}-%{release}

%description python
python components for the pypi-paramiko package.


%package python3
Summary: python3 components for the pypi-paramiko package.
Group: Default
Requires: python3-core
Provides: pypi(paramiko)
Requires: pypi(bcrypt)
Requires: pypi(cryptography)
Requires: pypi(pynacl)
Requires: pypi(six)

%description python3
python3 components for the pypi-paramiko package.


%prep
%setup -q -n paramiko-2.10.3
cd %{_builddir}/paramiko-2.10.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647712853
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-paramiko
cp %{_builddir}/paramiko-2.10.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-paramiko/b12c713656a9b98b6980a52bb068154cfdcbdd99
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-paramiko/b12c713656a9b98b6980a52bb068154cfdcbdd99

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
