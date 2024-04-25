Name:           hyprpaper
Version:        0.6.0
Release:        1
Summary:        Hyprpaper is a blazing fast wayland wallpaper utility with IPC controls.

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprpaper
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)

%description
Hyprpaper is a blazing fast wallpaper utility for Hyprland with the ability to dynamically change wallpapers through sockets. It will work on all wlroots-based compositors, though.

%prep
%autosetup

%build
rm -rf ./* ./.*
git clone %{url} .
git checkout v%{version}
make protocols
%cmake
%cmake_build

%install
install -m 755 -Dp %{__cmake_builddir}/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
