# revision 20374
# category Package
# catalog-ctan /macros/latex209/contrib/picinpar
# catalog-date 2010-11-05 12:43:21 +0100
# catalog-license gpl
# catalog-version 1.2a
Name:		texlive-picinpar
Version:	1.2a
Release:	1
Summary:	Insert pictures into paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex209/contrib/picinpar
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/picinpar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/picinpar.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A legacy package for creating 'windows' in paragraphs, for
inserting graphics, etc. (including "dropped capitals"). Users
should note that Piet van Oostrum (in a published review of
packages of this sort) does not recommend this package; Picins
is recommended instead.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/picinpar/picinpar.sty
%doc %{_texmfdistdir}/doc/latex/picinpar/picinpar-de.pdf
%doc %{_texmfdistdir}/doc/latex/picinpar/picinpar-de.tex
%doc %{_texmfdistdir}/doc/latex/picinpar/picinpar-en.pdf
%doc %{_texmfdistdir}/doc/latex/picinpar/picinpar-en.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
