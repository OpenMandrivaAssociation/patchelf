Name:		patchelf
Version:	0.5
Release:	1	
Summary:	A utility for patching ELF binaries

Group:		Development/C
License:	GPLv3+
URL:		http://nixos.org/patchelf.html
Source0:	http://hydra.nixos.org/build/114505/download/2/%{name}-%{version}.tar.bz2
Source1:	patchelf.1

%description
PatchELF is a simple utility for modifying existing ELF executables
and libraries.  It can change the dynamic loader ("ELF interpreter")
of executables and change the RPATH of executables and libraries.

%prep
%setup -q

# package ships elf.h - delete to use glibc-headers one
rm src/elf.h

%build
%configure
%make

%install
%makeinstall_std

# the docs get put in a funny place, so delete and include in the
# standard way in the docs section below
rm -rf %{buildroot}/usr/share/doc/%{name}

# install the man page
mkdir -p %{buildroot}/%{_mandir}/man1
install --mode=0644 %{SOURCE1} %{buildroot}/%{_mandir}/man1


%files
%{_bindir}/patchelf
%{_mandir}/man1/patchelf.1*
%doc README COPYING
