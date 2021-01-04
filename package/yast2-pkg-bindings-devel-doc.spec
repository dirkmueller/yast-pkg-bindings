#
# spec file for package yast2-pkg-bindings
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           yast2-pkg-bindings-devel-doc
Version:        4.2.14
Release:        0
License:        GPL-2.0-only
Group:          Documentation/HTML
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        yast2-pkg-bindings-%{version}.tar.bz2
Prefix:         %_prefix

# same as in the main package (because we use the same configure.in.in)
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libxslt
# zypp::VendorAttr API
BuildRequires:  libzypp-devel >= 17.25.0
BuildRequires:  yast2-core-devel
BuildRequires:  yast2-devtools >= 3.1.10

Buildarch: noarch
Requires:  yast2-pkg-bindings = %{version}
Summary:   YaST2 - Documentation for yast2-pkg-bindings package
Group:     Documentation/HTML

%description
This documenation package describes the package manager API (Pkg::
namespace) used in YaST scripts. The documentation is autogenerated
from the pkg-bindings sources.

%prep
%setup -n yast2-pkg-bindings-%{version}
# build only documentation, ignore all other directories
echo "doc" > SUBDIRS

%build
%yast_build

%install
%yast_install


%files
%defattr(-,root,root)
# do not use yast_docdir macro as it use wrong pkg name
%dir %{_datadir}/doc/packages/yast2-pkg-bindings
%doc %{_datadir}/doc/packages/yast2-pkg-bindings/xml
%exclude %{_datadir}/doc/packages/yast2-pkg-bindings/COPYING
