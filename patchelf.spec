Name:		patchelf
Version:	0.10
Release:	1	
Summary:	A utility for patching ELF binaries

Group:		Development/C
License:	GPLv3+
URL:		http://nixos.org/patchelf.html
Source0:	http://hydra.nixos.org/build/114505/download/2/%{name}-%{version}.tar.gz
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
%make_build

%install
%make_install

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


%changelog
* Fri Dec 02 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.6-1
+ Revision: 737200
- version update 0.6

* Fri Nov 11 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.5-1
+ Revision: 730182
- imported package patchelf

