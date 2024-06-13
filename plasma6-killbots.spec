#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		plasma6-killbots
Version:	24.05.1
Release:	%{?git:0.%{git}.}1
Summary:	KDE port of the classic BSD console game robots
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/killbots/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/killbots/-/archive/%{gitbranch}/killbots-%{gitbranchd}.tar.bz2#/killbots-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/killbots-%{version}.tar.xz
%endif
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Crash)

%description
Killbots is a simple game of evading killer robots.

Who created the robots and why they have been programmed to destroy, no one
knows. All that is known is that the robots are numerous and their sole
objective is to destroy you. Fortunately for you, their creator has focused on
quantity rather than quality and as a result the robots are severely lacking
in intelligence. Your superior wit and a fancy teleportation device are your
only weapons against the never-ending stream of mindless automatons.

%files -f killbots.lang
%{_bindir}/killbots
%{_datadir}/applications/org.kde.killbots.desktop
%{_datadir}/config.kcfg/killbots.kcfg
%{_iconsdir}/hicolor/*/apps/killbots.*
%{_datadir}/killbots
%{_datadir}/metainfo/org.kde.killbots.appdata.xml
%{_datadir}/qlogging-categories6/killbots.categories

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n killbots-%{?git:%{gitbranchd}}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build
%find_lang killbots --with-html
