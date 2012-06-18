#
# spec file for package cassiopee
#
# Copyright (c) 2012 Olivier Sallou <osallou@irisa.fr>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%global debug_package %{nil}

%define gem_name cassiopee


%if 0%{?fedora} == 17
%define gem_dir /usr/share/gems
%else
%if 0%{?centos_version} || 0%{?fedora} || 0%{?mdkversion}
%define gem_dir /usr/lib/ruby/gems/1.8
%else
%define gem_dir /usr/%_lib/ruby/gems/1.8
%endif
%endif

Name:    cassiopee
Version: 0.1.10
Release: 1%{?dist}
Summary: Library to search in string with errors
Group: Applications/System

%if 0%{?fedora} == 17
BuildArch: noarch
%endif

License:  Ruby
URL: http://rubygems.org/gems/text

Source: %{gem_name}-%{version}.gem

Autoreq: 0

Patch0: cassiopee-userubygems.patch


%if (0%{?fedora} == 17 || 0%{?sles_version})
BuildRequires: ruby,rubygems, ruby-text
Requires:  ruby, rubygems, ruby-text
%else
BuildRequires: ruby(abi) = 1.8, rubygems, ruby-text
Requires:  ruby(abi) = 1.8, rubygems, ruby-text
%endif

%description
 Exact or error search in strings library and tool

%prep 
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}
%patch0
%if (0%{?suse_version} || 0%{?sles_version})
  gem spec %{SOURCE0} -l > %{gem_name}.gemspec
%else
  gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%endif

%build
mkdir -p .%{gem_dir}
gem build %{gem_name}.gemspec

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install -V --local --install-dir ./%{gem_dir} --bindir ./%{_bindir} --force --rdoc %{gem_name}-%{version}.gem

%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
cp -a ./%{gem_dir}/gems/%{gem_name}-%{version}/bin/cassie.rb %{buildroot}/usr/bin/cassie
chmod 755 %{buildroot}/usr/bin/cassie


%files
%defattr(-,root,root)
/usr/bin/cassie
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/gems/%{gem_name}-%{version}
%{gem_dir}/doc/%{gem_name}-%{version}
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec


%changelog
* Wed Jun 13 2012 Olivier Sallou <olivier.sallou@irisa.fr> - 0.1.10-1
- RPM packaging
