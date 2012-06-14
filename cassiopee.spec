%global debug_package %{nil}

%define gem_name cassiopee
%define gem_dir /usr/%_lib/ruby/1.8

Name:    cassiopee
Version: 0.1.9
Release: 1%{?dist}
Summary: Text search with errors library
Group: Applications/System

BuildArch: noarch

License:  CeCILL
URL: http://rubygems.org/gems/cassiopee

#Source: http://gitlab.irisa.fr/gone/repository/archive?ref=centos
Source: %{name}-%{version}.gem

Autoreq: 0

#BuildRequires: rubygems-devel
Requires:  ruby(abi) = 1.8, rubygems, ruby-text

Patch0: cassiopee-userubygems.patch

%description
 Library and tools to search with errors in a string

%prep 
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}
%patch0

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
mkdir -p .%{gem_dir}
gem build %{gem_name}.gemspec

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install -V --local --install-dir ./%{gem_dir} --bindir ./%{_bindir} --force --rdoc %{gem_name}-%{version}.gem

%install
mkdir -p $RPM_BUILD_ROOT%{gem_dir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -a ./%{gem_dir}/* $RPM_BUILD_ROOT%{gem_dir}/

cp -a $RPM_BUILD_ROOT/%{gem_dir}/gems/%{gem_name}-%{version}/bin/cassie.rb $RPM_BUILD_ROOT%{_bindir}/cassie
chmod 755 $RPM_BUILD_ROOT%{_bindir}/cassie

%files
%defattr(-,root,root)
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/gems/%{gem_name}-%{version}
%{gem_dir}/doc/%{gem_name}-%{version}
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
/usr/bin/cassie

%changelog
* Wed Jun 13 2012 Olivier Sallou <olivier.sallou@irisa.fr> - 0.1.9-1
- Fedora packaging
