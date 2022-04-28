#
# spec file for package salt-netapi-client
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#
#!BuildRequires: jboss-websocket-1.0-api

Name:           salt-netapi-client
Version:        0.20.0
Release:        0
Summary:        Java bindings for the Salt API
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/SUSE/salt-netapi-client
Source0:        https://github.com/SUSE/salt-netapi-client/archive/v0.20.0/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  xz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  javapackages-tools
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(javax.websocket:javax.websocket-api)
BuildRequires:  mvn(org.apache.httpcomponents:httpasyncclient)
BuildArch:      noarch
Requires:       java >= 1.8

# This package has been renamed with version 0.7.0
Provides:       saltstack-netapi-client-java == %{version}
Obsoletes:      saltstack-netapi-client-java < %{version}

%description
Java bindings for the Salt API

%package javadoc
Summary:        API docs for %{name}

%description javadoc
This package contains the API Documentation for %{name}.


%prep
%autosetup -p1 -n "%{name}-%{version}"
find \( -name '*.jar' -o -name '*.class' \) -delete
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%build
%{mvn_build} -f -- -Dsource=8


%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}


%files -f .mfiles
%doc LICENSE README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog

