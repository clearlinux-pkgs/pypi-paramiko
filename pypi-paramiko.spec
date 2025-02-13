#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : pypi-paramiko
Version  : 3.5.1
Release  : 29
URL      : https://files.pythonhosted.org/packages/7d/15/ad6ce226e8138315f2451c2aeea985bf35ee910afb477bae7477dc3a8f3b/paramiko-3.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/7d/15/ad6ce226e8138315f2451c2aeea985bf35ee910afb477bae7477dc3a8f3b/paramiko-3.5.1.tar.gz
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
%setup -q -n paramiko-3.5.1
cd %{_builddir}/paramiko-3.5.1
pushd ..
cp -a paramiko-3.5.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738691480
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 setup.py build

popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-paramiko
cp %{_builddir}/paramiko-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-paramiko/b12c713656a9b98b6980a52bb068154cfdcbdd99 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
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
