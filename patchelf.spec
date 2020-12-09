Summary:	A utility for patching ELF binaries
Name:		patchelf
Version:	0.12
Release:	1
License:	GPLv3+
Group:		Development/Tools
Url:		http://nixos.org/patchelf.html
Source0:	https://github.com/NixOS/patchelf/archive/%{version}.tar.gz
BuildRequires:	acl-devel
BuildRequires:	attr-devel

%description
PatchELF is a simple utility for modifying an existing ELF executable
or library. It can change the dynamic loader ("ELF interpreter")
of an executable and change the RPATH of an executable or library.

%files
%doc COPYING
%{_bindir}/patchelf
%{_mandir}/man1/patchelf.1*

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
make check
