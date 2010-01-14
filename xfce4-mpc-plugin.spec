Summary:	A mpc plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka mpc dla panelu Xfce
Name:		xfce4-mpc-plugin
Version:	0.3.3
Release:	4
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-mpc-plugin/%{name}-%{version}.tar.gz
# Source0-md5:	b4f7f67589f34f77973a51dd5069712d
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-mpc-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libmpd-devel >= 0.12
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
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

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-mpc-plugin
%{_datadir}/xfce4/panel-plugins/xfce4-mpc-plugin.desktop
