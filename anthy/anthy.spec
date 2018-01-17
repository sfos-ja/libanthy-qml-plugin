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
/usr/lib/libanthy.a
/usr/lib/libanthy.la
/usr/lib/libanthy.so
/usr/lib/libanthy.so.0
/usr/lib/libanthy.so.0.1.0
/usr/lib/libanthydic.a
/usr/lib/libanthydic.la
/usr/lib/libanthydic.so
/usr/lib/libanthydic.so.0
/usr/lib/libanthydic.so.0.1.0
/usr/lib/libanthyinput.a
/usr/lib/libanthyinput.la
/usr/lib/libanthyinput.so
/usr/lib/libanthyinput.so.0
/usr/lib/libanthyinput.so.0.0.0
/usr/lib/pkgconfig/anthy.pc
/usr/share/anthy/anthy.dic
/usr/share/anthy/dic-tool-usage.txt
/usr/share/anthy/typetab
/usr/share/anthy/zipcode.t
