%global modname pyudev

Name:             python-pyudev
Version:          0.15
Release:          9%{?dist}
Summary:          A libudev binding
Group:            Development/Languages
License:          LGPLv2+
URL:              http://pypi.python.org/pypi/pyudev
Source0:          http://pypi.python.org/packages/source/p/pyudev/pyudev-0.15.tar.gz
BuildArch:        noarch
Patch0:           python-pyudev-0.15-load-libudev-in-context.patch
# backported from upstream
Patch1:           python-pyudev-0.15-retry-interrupted-calls.patch
Requires:         systemd-libs
BuildRequires:    python-devel python-setuptools systemd-devel

%description
###### pyudev ######

pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.

The binding supports CPython_ 2 (2.6 or newer) and 3 (3.1 or newer), and
PyPy_ 1.5 or newer.  It is tested against udev 151 or newer, earlier
versions of udev as found on dated Linux systems may work, but are not
officially supported.

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc COPYING README.rst
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*


%changelog
* Wed Mar 22 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.15-9
- The libudev library loaded in context to workaround cleanup problems
  Resolves: rhbz#1252833
- Retry interrupted calls
  Resolves: rhbz#1108921

* Thu Dec  3 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.15-8
- Added systemd-libs requirement for libudev
  Resolves: rhbz#1287461

* Thu Apr  9 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.15-7
- Dropped unneeded explicit dependencies
  Resolves: rhbz#1095454

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.15-6
- Mass rebuild 2013-12-27

* Wed Jul 31 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.15-5
- Fixed license field

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Chris Lockfort <clockfort@redhat.com> 0.15-3
- Reflect rawhide merging udev into systemd
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Mon Jun 18 2012 Chris Lockfort <clockfort@redhat.com> 0.15-1
- initial package
