# revision 29260
# category Package
# catalog-ctan /macros/latex/contrib/simplecd
# catalog-date 2013-02-28 20:37:57 +0100
# catalog-license lppl1.2
# catalog-version 1.4
Name:		texlive-simplecd
Version:	1.4
Release:	1
Summary:	Simple CD, DVD covers for printing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/simplecd
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplecd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplecd.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplecd.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides printable cut-outs for various CD, DVD and
other disc holders. The name of the package comes from its
implementation and ease of use; it was designed just for text
content, but since the text is placed in a \parbox in a tabular
environment cell, a rather wide range of things may be placed.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/simplecd/simplecd.sty
%doc %{_texmfdistdir}/doc/latex/simplecd/README
%doc %{_texmfdistdir}/doc/latex/simplecd/examples.pdf
%doc %{_texmfdistdir}/doc/latex/simplecd/examples.tex
%doc %{_texmfdistdir}/doc/latex/simplecd/simplecd.pdf
#- source
%doc %{_texmfdistdir}/source/latex/simplecd/simplecd.dtx
%doc %{_texmfdistdir}/source/latex/simplecd/simplecd.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
