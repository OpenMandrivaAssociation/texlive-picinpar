%global tl_name picinpar
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3a
Release:	%{tl_revision}.1
Summary:	Insert pictures into paragraphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex209/contrib/picinpar
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/picinpar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/picinpar.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A legacy package for creating 'windows' in paragraphs, for inserting
graphics, etc. (including "dropped capitals"). Users should note that
Pieter van Oostrum (in a published review of packages of this sort) does
not recommend this package; Picins is recommended instead.

