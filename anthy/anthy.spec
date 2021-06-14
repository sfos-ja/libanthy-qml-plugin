Name: anthy
Version: 9100h
Release: 2%{?dist}
Summary: Japanese kana-to-kanji conversion engine
License: LGPLv2
Source0: http://dl.sourceforge.jp/%{name}/37536/%{name}-%{version}.tar.gz
#Source: %{name}-%{version}.tar.gz
URL: http://sourceforge.jp/projects/anthy/

%description
Japanese kana-to-kanji conversion engine

%define debug_package %{nil}

%prep
%setup -q

%build
%configure
export LD_LIBRARY_PATH="`pwd`/src-main/.libs:`pwd`/src-worddic/.libs:${LD_LIBRARY_PATH}"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
/etc/anthy-conf
/usr/bin/anthy-agent
/usr/bin/anthy-dic-tool
/usr/bin/anthy-morphological-analyzer
/usr/include/anthy/anthy.h
/usr/include/anthy/dicutil.h
/usr/include/anthy/input.h
%{_libdir}/libanthy.a
%{_libdir}/libanthy.la
%{_libdir}/libanthy.so
%{_libdir}/libanthy.so.0
%{_libdir}/libanthy.so.0.1.0
%{_libdir}/libanthydic.a
%{_libdir}/libanthydic.la
%{_libdir}/libanthydic.so
%{_libdir}/libanthydic.so.0
%{_libdir}/libanthydic.so.0.1.0
%{_libdir}/libanthyinput.a
%{_libdir}/libanthyinput.la
%{_libdir}/libanthyinput.so
%{_libdir}/libanthyinput.so.0
%{_libdir}/libanthyinput.so.0.0.0
%{_libdir}/pkgconfig/anthy.pc
/usr/share/anthy/anthy.dic
/usr/share/anthy/dic-tool-usage.txt
/usr/share/anthy/typetab
/usr/share/anthy/zipcode.t
