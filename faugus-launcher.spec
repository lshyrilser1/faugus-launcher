Name:           faugus-launcher
Version:        2.3.0
Release:        1
Summary:        Lightweight launcher for Windows games via UMU-Launcher
Group:          Games
License:        MIT
URL:            https://github.com/Faugus/faugus-launcher
Source0:        https://github.com/Faugus/faugus-launcher/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildSystem:    meson

BuildRequires:  gettext
BuildRequires:  gtk-update-icon-cache
BuildRequires:  meson

#Requires:  python-gobject
#Requires:  python%{pyver}dist(requests)
#Requires:  python%{pyver}dist(icoextract)
#Requires:  python%{pyver}dist(pillow)
#Requires:  python%{pyver}dist(filelock)
Requires:  python%{pyver}dist(vdf)
#Requires:  python%{pyver}dist(psutil)
Requires:  typelib(Adw)
#Requires:  umu-launcher
#Requires:  imagemagick
#Requires:  typelib(Gtk) = 4.0
#Requires:  typelib(AyatanaAppIndicator3)

%description
A simple and lightweight app for running Windows games using UMU-Launcher

%prep
%autosetup -n %{name}-%{version} -p1
sed -i '1{/^#!/d}' faugus/launcher.py

%install -a
chmod 0644 %{buildroot}%{python3_sitelib}/faugus/backup.py \
           %{buildroot}%{python3_sitelib}/faugus/proton_downloader.py
chmod 0644 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/*.svg
ln -sf io.github.Faugus.faugus-launcher.svg \
       %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/faugus-launcher.svg

%files
%license LICENSE
%{_bindir}/faugus-launcher
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_iconsdir}/hicolor/scalable/actions/*.svg
%{_datadir}/faugus-launcher/*
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/*.mo
%lang(bg) %{_datadir}/locale/bg/LC_MESSAGES/*.mo
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/*.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/*.mo
%lang(fa) %{_datadir}/locale/fa/LC_MESSAGES/*.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/*.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/*.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/*.mo
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/*.mo
%lang(ka) %{_datadir}/locale/ka/LC_MESSAGES/*.mo
%lang(nb) %{_datadir}/locale/nb/LC_MESSAGES/*.mo
%lang(ne) %{_datadir}/locale/ne/LC_MESSAGES/*.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/*.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/*.mo
%lang(ps) %{_datadir}/locale/ps/LC_MESSAGES/*.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/*.mo
%lang(ro) %{_datadir}/locale/ro/LC_MESSAGES/*.mo
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/*.mo
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/*.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/*.mo
%lang(ta) %{_datadir}/locale/ta/LC_MESSAGES/*.mo
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/*.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/*.mo
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/*.mo
%{_datadir}/metainfo/*.xml
%{py_sitedir}/faugus
