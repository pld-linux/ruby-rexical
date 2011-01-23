
%define gitrev 151da0e
%define gitauthor tenderlove
%define gitname rexical

Summary:	rexical is a lexical scanner generator for ruby
Name:		ruby-rexical
Version:	0
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://download.github.com/%{gitauthor}-%{gitname}-%{gitrev}.tar.gz
# Source0-md5:	a8dc0324db28d5b5f25329a89b498857
Patch0:		%{name}-nogems.patch
URL:		http://github.com/tenderlove/rexical
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
BuildRequires:	ruby-modules
BuildRequires:	setup.rb >= 3.4.1
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rexical is a lexical scanner generator for ruby.

%prep
%setup -q -n %{gitauthor}-%{gitname}-%{gitrev}
%patch0 -p1
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--installdirs=std
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rex
%{ruby_rubylibdir}/rexical.rb
%{ruby_rubylibdir}/rexical
