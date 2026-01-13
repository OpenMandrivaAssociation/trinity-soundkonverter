%bcond clang 1
%bcond dvb 1
%bcond lame 1
%bcond xcb 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg soundkonverter
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.3.8
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Audio converter frontend for Trinity
Group:		Application/Multimedia
URL:		http://potracegui.sourceforge.net

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/multimedia/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:	  cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}
BuildOption:    -DWITH_DVB=%{?!with_dvb:OFF}%{?with_dvb:ON}
BuildOption:    -DWITH_LAME=%{?!with_lame:OFF}%{?with_lame:ON}
BuildOption:    -DWITH_XCB=%{?!with_xcb:OFF}%{?with_xcb:ON}
BuildOption:    -DBUILD_ALL=ON

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

%{?with_lame:BuildRequires:  pkgconfig(lame)}
%{?with_dvb:BuildRequires:  pkgconfig(libdvbv5)}
%{?with_xcb:BuildRequires:  pkgconfig(xcb)}

# TAGLIB support
BuildRequires:	pkgconfig(taglib)

# CDDA support
BuildRequires:  pkgconfig(libcdio_cdda)
BuildRequires:  cdda-devel

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
soundKonverter is a frontend to various audio converters.

The key features are:
 - Audio conversion
 - Replay Gain calculation
 - CD ripping

soundKonverter supports reading and writing tags for many formats, so the tags
are preserved when converting files.

It comes with an Amarok script.

See 'soundkonverter-amarok' package for more informations.

See README.Debian for more informations on supported formats.


%package amarok
Summary:		audio converter frontend for Trinity (Amarok script)
Group:			Application/Multimedia
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-amarok

%description amarok
Amarok script for soundKonverter. It allows you to easily transcode files when
transferring them to your media device.

See the 'trinity-soundkonverter' package for more information.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{tde_prefix}/bin/soundkonverter
%{tde_prefix}/share/applications/tde/soundkonverter.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/audiocd_extract_with_soundkonverter.desktop
%{tde_prefix}/share/apps/soundkonverter
%exclude %{tde_prefix}/share/apps/soundkonverter/amarokscript/
%{tde_prefix}/share/doc/tde/HTML/en/soundkonverter/
%{tde_prefix}/share/icons/hicolor/*/apps/soundkonverter*.png
%{tde_prefix}/share/mimelnk/application/x-la.soundkonverter.desktop
%{tde_prefix}/share/mimelnk/application/x-ofc.soundkonverter.desktop
%{tde_prefix}/share/mimelnk/application/x-ofr.soundkonverter.desktop
%{tde_prefix}/share/mimelnk/application/x-ofs.soundkonverter.desktop
%{tde_prefix}/share/mimelnk/application/x-shorten.soundkonverter.desktop
%{tde_prefix}/share/mimelnk/audio/amr.soundkonverter.desktop
%{tde_prefix}/share/mimelnk/audio/x-ape.soundkonverter.desktop
%{tde_prefix}/share/mimelnk/audio/x-bonk.soundkonverter.desktop
%{tde_prefix}/share/mimelnk/audio/x-pac.soundkonverter.desktop
%{tde_prefix}/share/mimelnk/audio/x-tta.soundkonverter.desktop
%{tde_prefix}/share/mimelnk/audio/x-wavpack-correction.soundkonverter.desktop
%{tde_prefix}/share/mimelnk/audio/x-wavpack.soundkonverter.desktop
%{tde_prefix}/share/mimelnk/video/x-flv.soundkonverter.desktop

%files amarok
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/soundkonverter/amarokscript/

