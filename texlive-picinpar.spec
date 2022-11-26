Name:		texlive-picinpar
Version:	65097
Release:	1
Summary:	Insert pictures into paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex209/contrib/picinpar
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/picinpar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/picinpar.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A legacy package for creating 'windows' in paragraphs, for
inserting graphics, etc. (including "dropped capitals"). Users
should note that Piet van Oostrum (in a published review of
packages of this sort) does not recommend this package; Picins
is recommended instead.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/picinpar/picinpar.sty
%doc %{_texmfdistdir}/doc/latex/picinpar/picinpar-de.pdf
%doc %{_texmfdistdir}/doc/latex/picinpar/picinpar-de.tex
%doc %{_texmfdistdir}/doc/latex/picinpar/picinpar-en.pdf
%doc %{_texmfdistdir}/doc/latex/picinpar/picinpar-en.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
