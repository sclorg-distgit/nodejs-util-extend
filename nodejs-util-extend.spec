%{?scl:%scl_package nodejs-util-extend}
%{!?scl:%global pkg_name %{name}}

%global enable_tests 1

%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-util-extend
Version:    1.0.3
Release:    1%{?dist}
Summary:        Node's internal object extension function
License:        MIT
Url:            https://github.com/isaacs/util-extend
Source:         http://registry.npmjs.org/util-extend/-/util-extend-%{version}.tgz
Source1:        https://raw.githubusercontent.com/kasicka/util-extend/72ad112332507572d2c4dbe55f30b584a0d70878/LICENSE
# https://github.com/isaacs/util-extend/pull/7
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
BuildRequires:	%{?scl_prefix}nodejs-devel

%description
The object extending function used with Node.js.

%prep
%setup -q -n package

cp -p %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/util-extend
cp -pr package.json extend.js \
        %{buildroot}%{nodejs_sitelib}/util-extend/

%nodejs_symlink_deps

%check
%{?scl:scl enable %{scl} "}
%nodejs_symlink_deps --check
%__nodejs test.js
%{?scl:"}

%files
%doc README.md
%doc LICENSE
%{nodejs_sitelib}/util-extend

%changelog
* Wed Sep 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.3-1
- Updated with script

* Tue Feb 16 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-8
- Enable scl in %%check section

* Wed Sep 30 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-6
- Rebuilt

* Thu Sep 17 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-5
- Add %%check
- add missing BuildRequires

* Mon Aug 10 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-4
- Add license text

* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-3
- Remove undefined macro

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-2
- Add dist macro

* Tue Jan 06 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-1
- Initial build
