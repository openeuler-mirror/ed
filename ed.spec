Summary: A line-oriented text editor
Name: ed
Version: 1.17
Release: 1
License: GPLv3+ and GFDL-1.3
# Note:  Upstream provides only lzip compressed tarballs so we repacked from:
#Source: https://download.savannah.gnu.org/releases/ed/%{name}-%{version}.tar.lz
Source: %{name}-%{version}.tar.xz
URL:    http://www.gnu.org/software/ed/
BuildRequires: gcc
Requires(post): info
Requires(preun): info

%description
GNU ed is a line-oriented text editor. It is used to create, display, modify and 
otherwise manipulate text files, both interactively and via shell scripts. 

A restricted version of ed, red, can only edit files in the current directory 
and cannot execute shell commands. Ed is the "standard" text editor in the sense 
that it is the original editor for Unix, and thus widely available. 

For most purposes, however, it is superseded by full-screen editors such as GNU 
Emacs or GNU Moe.

%package        help
Summary:        Documents for ed
Buildarch:      noarch

%description    help
Man pages and other related documents.

%prep
%setup -q

%build
%configure
%make_build CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}"

%install
%make_install
rm -vrf %{buildroot}%{_infodir}/dir

%post help
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun help
if [ $1 = 0 ] ; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files
%license COPYING
%{_bindir}/ed
%{_bindir}/red

%files help
%doc ChangeLog NEWS README TODO AUTHORS
%{_mandir}/man1/ed.1*
%{_mandir}/man1/red.1*
%{_infodir}/ed.info*

%changelog
* Mon Feb 08 2021 shixuantng <shixuantong@huawei.com> - 1.17-1
- upgrade version to 1.17 and upgrade GFDL license

* Tue Jan 21 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.14.2-6
- resolve "rpm -ivh" err

* Tue Sep 17 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.14.2-5
- Package init
