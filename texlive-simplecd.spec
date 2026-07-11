%global tl_name simplecd
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Simple CD, DVD covers for printing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/simplecd
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simplecd.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simplecd.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simplecd.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides printable cut-outs for various CD, DVD and other
disc holders. The name of the package comes from its implementation and
ease of use; it was designed just for text content, but since the text
is placed in a \parbox in a tabular environment cell, a rather wide
range of things may be placed.

