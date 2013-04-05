Name:		killbots
Version:	4.10.2
Release:	1
Epoch:		1
Summary:	KDE port of the classic BSD console game robots
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/killbots/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
Killbots is a simple game of evading killer robots.

Who created the robots and why they have been programmed to destroy, no one
knows. All that is known is that the robots are numerous and their sole
objective is to destroy you. Fortunately for you, their creator has focused on
quantity rather than quality and as a result the robots are severely lacking
in intelligence. Your superior wit and a fancy teleportation device are your
only weapons against the never-ending stream of mindless automatons.

%files
%{_kde_bindir}/killbots
%{_kde_applicationsdir}/killbots.desktop
%{_kde_appsdir}/killbots
%{_kde_datadir}/config.kcfg/killbots.kcfg
%{_kde_docdir}/*/*/killbots
%{_kde_iconsdir}/hicolor/*/apps/killbots.*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4

%install
%makeinstall_std -C build


%changelog
* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

