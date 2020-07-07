%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		killbots
Version:	20.04.3
Release:	1
Epoch:		1
Summary:	KDE port of the classic BSD console game robots
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/killbots/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Crash)

%description
Killbots is a simple game of evading killer robots.

Who created the robots and why they have been programmed to destroy, no one
knows. All that is known is that the robots are numerous and their sole
objective is to destroy you. Fortunately for you, their creator has focused on
quantity rather than quality and as a result the robots are severely lacking
in intelligence. Your superior wit and a fancy teleportation device are your
only weapons against the never-ending stream of mindless automatons.

%files -f %{name}.lang
%{_bindir}/killbots
%{_datadir}/applications/org.kde.killbots.desktop
%{_datadir}/config.kcfg/killbots.kcfg
%{_iconsdir}/hicolor/*/apps/killbots.*
%{_datadir}/killbots
%{_datadir}/metainfo/org.kde.killbots.appdata.xml
%{_datadir}/qlogging-categories5/killbots.categories

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --with-html
