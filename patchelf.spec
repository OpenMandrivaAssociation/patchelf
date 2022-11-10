# (tpg) 2022-06-13 fix ld.lld: error: undefined symbol: __stack_chk_fail
%global optflags %{optflags} -fno-stack-protector
%global build_ldflags %{build_ldflags} -z nostart-stop-gc

Summary:	A utility for patching ELF binaries
Name:		patchelf
Version:	0.17.0
Release:	1
License:	GPLv3+
Group:		Development/Tools
Url:		http://nixos.org/patchelf.html
Source0:	https://github.com/NixOS/patchelf/releases/download/%{version}/patchelf-%{version}.tar.bz2
BuildRequires:	pkgconfig(libacl)
BuildRequires:	pkgconfig(libattr)

%description
PatchELF is a simple utility for modifying an existing ELF executable
or library. It can change the dynamic loader ("ELF interpreter")
of an executable and change the RPATH of an executable or library.

%files
%doc COPYING
%{_bindir}/patchelf
%doc %{_mandir}/man1/patchelf.1*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

# package ships elf.h - delete to use glibc-headers one
rm src/elf.h

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

# the docs get put in a funny place, so delete and include in the
# standard way in the docs section below
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%check
make check || cat tests/test-suite.log ||:
