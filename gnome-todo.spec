#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : gnome-todo
Version  : 41.0
Release  : 43
URL      : https://download.gnome.org/sources/gnome-todo/41/gnome-todo-41.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-todo/41/gnome-todo-41.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.1
Requires: gnome-todo-bin = %{version}-%{release}
Requires: gnome-todo-data = %{version}-%{release}
Requires: gnome-todo-license = %{version}-%{release}
Requires: gnome-todo-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : glibc-bin
BuildRequires : gnome-online-accounts-dev
BuildRequires : libpeas-dev
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(libadwaita-1)
BuildRequires : pkgconfig(libecal-2.0)
BuildRequires : pkgconfig(libpeas-1.0)
BuildRequires : pkgconfig(libportal-gtk4)
BuildRequires : sassc
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-build-with-libportal-gtk4.patch

%description
Summary
-------
* To be able to use the latest/adequate version of sass, install sassc
* meson will regenerate the CSS every time you modify the SCSS files.
* Note that meson always builds out-of-tree, so the modified css files will
appear in your builddir.

%package bin
Summary: bin components for the gnome-todo package.
Group: Binaries
Requires: gnome-todo-data = %{version}-%{release}
Requires: gnome-todo-license = %{version}-%{release}

%description bin
bin components for the gnome-todo package.


%package data
Summary: data components for the gnome-todo package.
Group: Data

%description data
data components for the gnome-todo package.


%package dev
Summary: dev components for the gnome-todo package.
Group: Development
Requires: gnome-todo-bin = %{version}-%{release}
Requires: gnome-todo-data = %{version}-%{release}
Provides: gnome-todo-devel = %{version}-%{release}
Requires: gnome-todo = %{version}-%{release}

%description dev
dev components for the gnome-todo package.


%package doc
Summary: doc components for the gnome-todo package.
Group: Documentation

%description doc
doc components for the gnome-todo package.


%package license
Summary: license components for the gnome-todo package.
Group: Default

%description license
license components for the gnome-todo package.


%package locales
Summary: locales components for the gnome-todo package.
Group: Default

%description locales
locales components for the gnome-todo package.


%prep
%setup -q -n gnome-todo-41.0
cd %{_builddir}/gnome-todo-41.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680031552
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-todo
cp %{_builddir}/gnome-todo-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-todo/338650eb7a42dd9bc1f1c6961420f2633b24932d || :
cp %{_builddir}/gnome-todo-%{version}/subprojects/libadwaita/COPYING %{buildroot}/usr/share/package-licenses/gnome-todo/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-todo

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-todo

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Gtd-1.0.typelib
/usr/share/applications/org.gnome.Todo.desktop
/usr/share/dbus-1/services/org.gnome.Todo.service
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.todo.background.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.todo.gschema.xml
/usr/share/icons/hicolor/scalable/apps/org.gnome.Todo.Devel.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.Todo.svg
/usr/share/icons/hicolor/symbolic/actions/builder-view-left-pane-symbolic.svg
/usr/share/icons/hicolor/symbolic/actions/drag-handle-symbolic.svg
/usr/share/icons/hicolor/symbolic/actions/mail-inbox-symbolic.svg
/usr/share/icons/hicolor/symbolic/actions/view-tasks-all-symbolic.svg
/usr/share/icons/hicolor/symbolic/actions/view-tasks-today-symbolic.svg
/usr/share/icons/hicolor/symbolic/actions/view-tasks-unscheduled-symbolic.svg
/usr/share/icons/hicolor/symbolic/actions/view-tasks-week-symbolic.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Todo-symbolic.svg
/usr/share/metainfo/org.gnome.Todo.appdata.xml

%files dev
%defattr(-,root,root,-)
/usr/include/gnome-todo/gnome-todo.h
/usr/include/gnome-todo/gtd-activatable.h
/usr/include/gnome-todo/gtd-animatable.h
/usr/include/gnome-todo/gtd-animation-utils.h
/usr/include/gnome-todo/gtd-bin-layout.h
/usr/include/gnome-todo/gtd-clock.h
/usr/include/gnome-todo/gtd-easing.h
/usr/include/gnome-todo/gtd-interval.h
/usr/include/gnome-todo/gtd-keyframe-transition.h
/usr/include/gnome-todo/gtd-list-model-filter.h
/usr/include/gnome-todo/gtd-list-store.h
/usr/include/gnome-todo/gtd-manager.h
/usr/include/gnome-todo/gtd-max-size-layout.h
/usr/include/gnome-todo/gtd-menu-button.h
/usr/include/gnome-todo/gtd-notification.h
/usr/include/gnome-todo/gtd-object.h
/usr/include/gnome-todo/gtd-omni-area-addin.h
/usr/include/gnome-todo/gtd-omni-area.h
/usr/include/gnome-todo/gtd-panel.h
/usr/include/gnome-todo/gtd-property-transition.h
/usr/include/gnome-todo/gtd-provider-popover.h
/usr/include/gnome-todo/gtd-provider.h
/usr/include/gnome-todo/gtd-star-widget.h
/usr/include/gnome-todo/gtd-task-list-view.h
/usr/include/gnome-todo/gtd-task-list.h
/usr/include/gnome-todo/gtd-task.h
/usr/include/gnome-todo/gtd-timeline.h
/usr/include/gnome-todo/gtd-transition.h
/usr/include/gnome-todo/gtd-types.h
/usr/include/gnome-todo/gtd-utils.h
/usr/include/gnome-todo/gtd-widget.h
/usr/include/gnome-todo/gtd-window.h
/usr/include/gnome-todo/gtd-workspace.h
/usr/lib64/pkgconfig/gnome-todo.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/gnome-todo/add-notes.page
/usr/share/help/C/gnome-todo/archive.page
/usr/share/help/C/gnome-todo/assign-color.page
/usr/share/help/C/gnome-todo/assign-date.page
/usr/share/help/C/gnome-todo/contributing.page
/usr/share/help/C/gnome-todo/create-tasklists.page
/usr/share/help/C/gnome-todo/create-tasks.page
/usr/share/help/C/gnome-todo/delete-tasklist.page
/usr/share/help/C/gnome-todo/execute-task.page
/usr/share/help/C/gnome-todo/figures/org.gnome.Todo.svg
/usr/share/help/C/gnome-todo/give-star.page
/usr/share/help/C/gnome-todo/index.page
/usr/share/help/C/gnome-todo/overview.page
/usr/share/help/C/gnome-todo/rename-tasklist.page
/usr/share/help/C/gnome-todo/rename-tasks.page
/usr/share/help/C/gnome-todo/support.page
/usr/share/help/C/gnome-todo/switch-theme.page
/usr/share/help/C/gnome-todo/workflow.page
/usr/share/help/es/gnome-todo/add-notes.page
/usr/share/help/es/gnome-todo/archive.page
/usr/share/help/es/gnome-todo/assign-color.page
/usr/share/help/es/gnome-todo/assign-date.page
/usr/share/help/es/gnome-todo/contributing.page
/usr/share/help/es/gnome-todo/create-tasklists.page
/usr/share/help/es/gnome-todo/create-tasks.page
/usr/share/help/es/gnome-todo/delete-tasklist.page
/usr/share/help/es/gnome-todo/execute-task.page
/usr/share/help/es/gnome-todo/figures/org.gnome.Todo.svg
/usr/share/help/es/gnome-todo/give-star.page
/usr/share/help/es/gnome-todo/index.page
/usr/share/help/es/gnome-todo/overview.page
/usr/share/help/es/gnome-todo/rename-tasklist.page
/usr/share/help/es/gnome-todo/rename-tasks.page
/usr/share/help/es/gnome-todo/support.page
/usr/share/help/es/gnome-todo/switch-theme.page
/usr/share/help/es/gnome-todo/workflow.page
/usr/share/help/eu/gnome-todo/add-notes.page
/usr/share/help/eu/gnome-todo/archive.page
/usr/share/help/eu/gnome-todo/assign-color.page
/usr/share/help/eu/gnome-todo/assign-date.page
/usr/share/help/eu/gnome-todo/contributing.page
/usr/share/help/eu/gnome-todo/create-tasklists.page
/usr/share/help/eu/gnome-todo/create-tasks.page
/usr/share/help/eu/gnome-todo/delete-tasklist.page
/usr/share/help/eu/gnome-todo/execute-task.page
/usr/share/help/eu/gnome-todo/figures/org.gnome.Todo.svg
/usr/share/help/eu/gnome-todo/give-star.page
/usr/share/help/eu/gnome-todo/index.page
/usr/share/help/eu/gnome-todo/overview.page
/usr/share/help/eu/gnome-todo/rename-tasklist.page
/usr/share/help/eu/gnome-todo/rename-tasks.page
/usr/share/help/eu/gnome-todo/support.page
/usr/share/help/eu/gnome-todo/switch-theme.page
/usr/share/help/eu/gnome-todo/workflow.page
/usr/share/help/ko/gnome-todo/add-notes.page
/usr/share/help/ko/gnome-todo/archive.page
/usr/share/help/ko/gnome-todo/assign-color.page
/usr/share/help/ko/gnome-todo/assign-date.page
/usr/share/help/ko/gnome-todo/contributing.page
/usr/share/help/ko/gnome-todo/create-tasklists.page
/usr/share/help/ko/gnome-todo/create-tasks.page
/usr/share/help/ko/gnome-todo/delete-tasklist.page
/usr/share/help/ko/gnome-todo/execute-task.page
/usr/share/help/ko/gnome-todo/figures/org.gnome.Todo.svg
/usr/share/help/ko/gnome-todo/give-star.page
/usr/share/help/ko/gnome-todo/index.page
/usr/share/help/ko/gnome-todo/overview.page
/usr/share/help/ko/gnome-todo/rename-tasklist.page
/usr/share/help/ko/gnome-todo/rename-tasks.page
/usr/share/help/ko/gnome-todo/support.page
/usr/share/help/ko/gnome-todo/switch-theme.page
/usr/share/help/ko/gnome-todo/workflow.page
/usr/share/help/sv/gnome-todo/add-notes.page
/usr/share/help/sv/gnome-todo/archive.page
/usr/share/help/sv/gnome-todo/assign-color.page
/usr/share/help/sv/gnome-todo/assign-date.page
/usr/share/help/sv/gnome-todo/contributing.page
/usr/share/help/sv/gnome-todo/create-tasklists.page
/usr/share/help/sv/gnome-todo/create-tasks.page
/usr/share/help/sv/gnome-todo/delete-tasklist.page
/usr/share/help/sv/gnome-todo/execute-task.page
/usr/share/help/sv/gnome-todo/figures/org.gnome.Todo.svg
/usr/share/help/sv/gnome-todo/give-star.page
/usr/share/help/sv/gnome-todo/index.page
/usr/share/help/sv/gnome-todo/overview.page
/usr/share/help/sv/gnome-todo/rename-tasklist.page
/usr/share/help/sv/gnome-todo/rename-tasks.page
/usr/share/help/sv/gnome-todo/support.page
/usr/share/help/sv/gnome-todo/switch-theme.page
/usr/share/help/sv/gnome-todo/workflow.page
/usr/share/help/uk/gnome-todo/add-notes.page
/usr/share/help/uk/gnome-todo/archive.page
/usr/share/help/uk/gnome-todo/assign-color.page
/usr/share/help/uk/gnome-todo/assign-date.page
/usr/share/help/uk/gnome-todo/contributing.page
/usr/share/help/uk/gnome-todo/create-tasklists.page
/usr/share/help/uk/gnome-todo/create-tasks.page
/usr/share/help/uk/gnome-todo/delete-tasklist.page
/usr/share/help/uk/gnome-todo/execute-task.page
/usr/share/help/uk/gnome-todo/figures/org.gnome.Todo.svg
/usr/share/help/uk/gnome-todo/give-star.page
/usr/share/help/uk/gnome-todo/index.page
/usr/share/help/uk/gnome-todo/overview.page
/usr/share/help/uk/gnome-todo/rename-tasklist.page
/usr/share/help/uk/gnome-todo/rename-tasks.page
/usr/share/help/uk/gnome-todo/support.page
/usr/share/help/uk/gnome-todo/switch-theme.page
/usr/share/help/uk/gnome-todo/workflow.page

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-todo/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/gnome-todo/338650eb7a42dd9bc1f1c6961420f2633b24932d

%files locales -f gnome-todo.lang
%defattr(-,root,root,-)

