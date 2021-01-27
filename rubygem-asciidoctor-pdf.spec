%global gem_name asciidoctor-pdf

Name: rubygem-%{gem_name}
Version: 1.5.4
Release: 2%{?dist}
Summary: Converts AsciiDoc documents to PDF using Prawn
License: MIT
URL: https://github.com/asciidoctor/asciidoctor-pdf
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/asciidoctor/asciidoctor-pdf.git && cd asciidoctor-pdf
# git checkout v1.5.4
# tar -czf rubygem-asciidoctor-pdf-1.5.3-specs-examples.tgz spec/ examples/
Source1: %{name}-%{version}-specs-examples.tgz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel > 1.3.1
BuildRequires: ruby >= 1.9
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(asciidoctor)
BuildRequires: rubygem(prawn)
BuildRequires: rubygem(prawn-svg)
BuildRequires: rubygem(prawn-table)
BuildRequires: rubygem(prawn-templates)
BuildRequires: rubygem(prawn-icon)
BuildRequires: rubygem(treetop)
BuildRequires: rubygem(concurrent-ruby)
BuildRequires: rubygem(safe_yaml)
BuildRequires: rubygem(chunky_png)
BuildRequires: rubygem(pdf-inspector)
BuildRequires: rubygem(rouge)
BuildRequires: rubygem(coderay)
BuildRequires: rubygem(rexml)

BuildArch: noarch

%description
An extension for Asciidoctor that converts AsciiDoc documents to PDF using the
Prawn PDF library.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1
mv %{_builddir}/{spec,examples} .

# Regenerate the parser.
tt lib/asciidoctor/pdf/formatted_text/parser.treetop

%gemspec_remove_dep -g  ttfunk "~> 1.5.0", ">= 1.5.1"
%gemspec_remove_dep -g  prawn-icon "~> 2.5.0"
%gemspec_remove_dep -g  prawn "~> 2.2.0"
%gemspec_add_dep -g prawn "~> 2.4.0"

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check

GEM_HOME=/builddir/build/BUILD/%{gem_name}-%{version}/usr/share/gems rspec -t ~network

%files
%dir %{gem_instdir}
%{_bindir}/%{gem_name}
%{_bindir}/%{gem_name}-optimize
%license %{gem_instdir}/LICENSE.adoc
%doc %{gem_instdir}/README.adoc
%{gem_instdir}/bin
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/NOTICE.adoc
%doc %{gem_instdir}/CHANGELOG.adoc
%doc %{gem_instdir}/docs
%doc %{gem_instdir}/.yardopts
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Christopher Brown <chris.brown@redhat.com> - 1.5.4-1
- 1.5.4
- Remove bcond now network tests are handled in code
- Update spec and example instructions

* Mon Nov 16 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.3-8
- Relax prawn-icon gemspec dep

* Tue Nov 3 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.3-7
- Relax prawn-svg gemspec dep

* Fri Aug 21 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.3-6
- Patch broken rouge test

* Wed Aug 19 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.3-5
- Relax prawn and ttfunk gemspec dependencies

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 7 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.3-3
- Further test suite patches

* Wed May 6 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.3-2
- Patch test suite to fix numeric asssertions

* Tue May 5 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.3-1
- Bump to 1.5.3

* Fri Feb 7 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.0-0.14.beta.6
- Allow for additional failing test and warnings

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.13.beta.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Vít Ondruch <vondruch@redhat.com> - 1.5.0-0.12.beta.6
- Disable network depending tests.
- Relax Treetop dependency.

* Sat Oct 19 2019 Christopher Brown <chris.brown@redhat.com> - 1.5.0-0.11.beta.6
- Update to 1.5.0.beta.6
- Enable test suite

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.10.alpha.18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Christopher Brown <chris.brown@redhat.com> - 1.5.0-0.9.alpha.18
- Update to 1.5.0.alpha.18

* Mon Apr 22 2019 Sergi Jimenez <tripledes@gmail.com> - 1.5.0-0.9.alpha.16
- Revert depending on prawn-svg 0.29.0.

* Sun Apr 14 2019 Sergi Jimenez <tripledes@gmail.com> - 1.5.0-0.8.alpha.16
- Fix BZ#1699514

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.7.alpha.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 07 2018 Christopher Brown <chris.brown@redhat.com> - 1.5.0-0.6.alpha.16
- Update to 1.5.0.alpha.16

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.6.alpha.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.5.alpha.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.4.alpha.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.3.alpha.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 27 2016 Fabio Alessandro Locati <fale@redhat.com> - 1.5.0-0.2.alpha.13
- Update to 1.5.0.alpha.13

* Sun Aug 28 2016 Fabio Alessandro Locati <fale@redhat.com> - 1.5.0-0.2.alpha.12
- Update to 1.5.0.alpha.12

* Sun Aug 28 2016 Fabio Alessandro Locati <fale@redhat.com> - 1.5.0-0.2.alpha.11
- Provide asciidoctor-pdf for simpler searching

* Fri Jun 17 2016 Fabio Alessandro Locati <fale@redhat.com> - 1.5.0-0.1.alpha.11
- Initial package
