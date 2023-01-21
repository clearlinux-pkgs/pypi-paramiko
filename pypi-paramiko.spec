#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9C29BC560041E930 (jeff@bitprophet.org)
#
Name     : pypi-paramiko
Version  : 3.0.0
Release  : 18
URL      : https://files.pythonhosted.org/packages/3b/6b/554c00e5e68cd573bda345322a4e895e22686e94c7fa51848cd0e0442a71/paramiko-3.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/3b/6b/554c00e5e68cd573bda345322a4e895e22686e94c7fa51848cd0e0442a71/paramiko-3.0.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/3b/6b/554c00e5e68cd573bda345322a4e895e22686e94c7fa51848cd0e0442a71/paramiko-3.0.0.tar.gz.asc
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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

%description python3
python3 components for the pypi-paramiko package.


%prep
%setup -q -n paramiko-3.0.0
cd %{_builddir}/paramiko-3.0.0
pushd ..
cp -a paramiko-3.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1674259449
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-paramiko
cp %{_builddir}/paramiko-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-paramiko/b12c713656a9b98b6980a52bb068154cfdcbdd99 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
