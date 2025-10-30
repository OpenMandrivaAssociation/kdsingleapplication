%define major   1
%define libname %mklibname kdsingleapplication
%define develname %mklibname kdsingleapplication -d

Name:           kdsingleapplication
Version:        1.2.0
Release:        1
Summary:        KDAB's helper class for single-instance policy applications Qt6
Group:          System/Libraries/Qt
License:        MIT
URL:            https://github.com/KDAB/KDSingleApplication
Source0:        https://github.com/KDAB/KDSingleApplication/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)

%description
KDSingleApplication is a helper class for single-instance policy applications written by KDAB.

%package -n %{libname}
Summary:        Helper class for single-instance policy applications
Group:          System/Libraries

%description -n %{libname}
KDSingleApplication is a helper class for single-instance
policy applications.

%package -n %{develname}
Summary:        Development files for qt6 based libkdsingleapplication
Group:          Development/KDE and Qt
Requires:       %{libname} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}

%description -n %{develname}
Development files for libkdsingleapplication

%prep
%autosetup -p1 -n KDSingleApplication-%{version}

%build
%cmake \
        -DKDSingleApplication_QT6:BOOL=ON \
        -DCMAKE_BUILD_TYPE=Release

%make_build

%install
%make_install -C build

%files -n %{libname}
%license LICENSES/*
%doc README.md
%{_libdir}/libkdsingleapplication-qt6.so.%{major}*

%files -n %{develname}
%doc %{_datadir}/doc/KDSingleApplication-qt6/
%{_libdir}/libkdsingleapplication-qt6.so
%{_libdir}/cmake/KDSingleApplication-qt6/
%{_prefix}/mkspecs/modules/qt_KDSingleApplication.pri
%{_includedir}/kdsingleapplication-qt6/
