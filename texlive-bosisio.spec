# revision 16989
# category Package
# catalog-ctan /macros/latex/contrib/bosisio
# catalog-date 2010-02-10 21:47:34 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-bosisio
Version:	20100210
Release:	6
Summary:	A collection of packages by Francesco Bosisio
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bosisio
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bosisio.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bosisio.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bosisio.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of packages containing: accenti dblfont; envmath;
evenpage; graphfig; mathcmd; quotes; and sobolev.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bosisio/accenti.sty
%{_texmfdistdir}/tex/latex/bosisio/dblfont.sty
%{_texmfdistdir}/tex/latex/bosisio/envmath.sty
%{_texmfdistdir}/tex/latex/bosisio/evenpage.sty
%{_texmfdistdir}/tex/latex/bosisio/graphfig.sty
%{_texmfdistdir}/tex/latex/bosisio/mathcmd.sty
%{_texmfdistdir}/tex/latex/bosisio/quotes.sty
%{_texmfdistdir}/tex/latex/bosisio/sobolev.sty
%doc %{_texmfdistdir}/doc/latex/bosisio/README
%doc %{_texmfdistdir}/doc/latex/bosisio/accenti.html
%doc %{_texmfdistdir}/doc/latex/bosisio/accenti.pdf
%doc %{_texmfdistdir}/doc/latex/bosisio/dblfont.html
%doc %{_texmfdistdir}/doc/latex/bosisio/dblfont.pdf
%doc %{_texmfdistdir}/doc/latex/bosisio/envmath.html
%doc %{_texmfdistdir}/doc/latex/bosisio/envmath.pdf
%doc %{_texmfdistdir}/doc/latex/bosisio/evenpage.html
%doc %{_texmfdistdir}/doc/latex/bosisio/evenpage.pdf
%doc %{_texmfdistdir}/doc/latex/bosisio/graphfig.html
%doc %{_texmfdistdir}/doc/latex/bosisio/graphfig.pdf
%doc %{_texmfdistdir}/doc/latex/bosisio/index.html
%doc %{_texmfdistdir}/doc/latex/bosisio/makedoc
%doc %{_texmfdistdir}/doc/latex/bosisio/mathcmd.html
%doc %{_texmfdistdir}/doc/latex/bosisio/mathcmd.pdf
%doc %{_texmfdistdir}/doc/latex/bosisio/quotes.html
%doc %{_texmfdistdir}/doc/latex/bosisio/quotes.pdf
%doc %{_texmfdistdir}/doc/latex/bosisio/sobolev.html
%doc %{_texmfdistdir}/doc/latex/bosisio/sobolev.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bosisio/accenti.drv
%doc %{_texmfdistdir}/source/latex/bosisio/accenti.dtx
%doc %{_texmfdistdir}/source/latex/bosisio/dblfont.drv
%doc %{_texmfdistdir}/source/latex/bosisio/dblfont.dtx
%doc %{_texmfdistdir}/source/latex/bosisio/envmath.drv
%doc %{_texmfdistdir}/source/latex/bosisio/envmath.dtx
%doc %{_texmfdistdir}/source/latex/bosisio/evenpage.drv
%doc %{_texmfdistdir}/source/latex/bosisio/evenpage.dtx
%doc %{_texmfdistdir}/source/latex/bosisio/graphfig.drv
%doc %{_texmfdistdir}/source/latex/bosisio/graphfig.dtx
%doc %{_texmfdistdir}/source/latex/bosisio/mathcmd.drv
%doc %{_texmfdistdir}/source/latex/bosisio/mathcmd.dtx
%doc %{_texmfdistdir}/source/latex/bosisio/quotes.drv
%doc %{_texmfdistdir}/source/latex/bosisio/quotes.dtx
%doc %{_texmfdistdir}/source/latex/bosisio/sobolev.drv
%doc %{_texmfdistdir}/source/latex/bosisio/sobolev.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100210-2
+ Revision: 749844
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100210-1
+ Revision: 717975
- texlive-bosisio
- texlive-bosisio
- texlive-bosisio
- texlive-bosisio
- texlive-bosisio

