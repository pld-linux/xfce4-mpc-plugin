Summary:	A mpc plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka mpc dla panelu Xfce
Name:		xfce4-mpc-plugin
Version:	0.4.4
Release:	1
License:	BSD-like
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-mpc-plugin/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	1c126ca71d6db1ac6a0cc6720554e7bd
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-mpc-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	exo-devel >= 0.8.0
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libmpd-devel >= 0.12
BuildRequires:	libxfce4ui-devel >= 4.10.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.10.0
BuildRequires:	xfce4-panel-devel >= 4.10.0
Requires:	xfce4-panel >= 4.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A client plugin for the Music Player Daemon.

%description -l pl.UTF-8
Wtyczka klienta Music Player Daemon.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libmpc.so
%{_datadir}/xfce4/panel/plugins/xfce4-mpc-plugin.desktop
