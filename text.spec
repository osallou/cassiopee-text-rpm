%global debug_package %{nil}

%define gem_name text
%define gem_dir /usr/share/rubygems

Name:    ruby-text
Version: 1.2.1
Release: 1%{?dist}
Summary: Collection of text algorithms
Group: Applications/System

BuildArch: noarch

License:  Ruby
URL: http://rubygems.org/gems/text

Source: %{gem_name}-%{version}.gem

Autoreq: 0

#BuildRequires: rubygems-devel
Requires:  ruby(abi) = 1.8, rubygems


%description
 Collection of text algorithms (Levenshtein, metaphone,
 Prter stemming, Soundex, White similarity)

%prep 
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}

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


%files
%defattr(-,root,root)
/usr/share/rubygems/cache/%{gem_name}-%{version}.gem
/usr/share/rubygems/gems/%{gem_name}-%{version}
/usr/share/rubygems/doc/%{gem_name}-%{version}
/usr/share/rubygems/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Wed Jun 13 2012 Olivier Sallou <olivier.sallou@irisa.fr> - 1.2.1-1
- Fedora packaging
 
