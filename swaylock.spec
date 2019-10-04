#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swaylock
Version  : 1.4
Release  : 2
URL      : https://github.com/swaywm/swaylock/archive/1.4.tar.gz
Source0  : https://github.com/swaywm/swaylock/archive/1.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: swaylock-bin = %{version}-%{release}
Requires: swaylock-data = %{version}-%{release}
Requires: swaylock-man = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-meson
BuildRequires : libxkbcommon-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : scdoc

%description
# swaylock
swaylock is a screen locking utility for Wayland compositors. It is compatible
with any Wayland compositor which implements the following Wayland protocols:

%package bin
Summary: bin components for the swaylock package.
Group: Binaries
Requires: swaylock-data = %{version}-%{release}

%description bin
bin components for the swaylock package.


%package data
Summary: data components for the swaylock package.
Group: Data

%description data
data components for the swaylock package.


%package man
Summary: man components for the swaylock package.
Group: Default

%description man
man components for the swaylock package.


%prep
%setup -q -n swaylock-1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570221536
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/swaylock

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/swaylock
/usr/share/fish/completions/swaylock.fish
/usr/share/zsh/site-functions/_swaylock

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/swaylock.1
