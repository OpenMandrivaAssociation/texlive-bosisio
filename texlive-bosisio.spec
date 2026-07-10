%global tl_name bosisio
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A collection of packages by Francesco Bosisio
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bosisio
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bosisio.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bosisio.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bosisio.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of packages containing: accenti dblfont; envmath; evenpage;
graphfig; mathcmd; quotes; and sobolev.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bosisio
%dir %{_datadir}/texmf-dist/source/latex/bosisio
%dir %{_datadir}/texmf-dist/tex/latex/bosisio
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/README
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/accenti.html
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/accenti.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/dblfont.html
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/dblfont.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/envmath.html
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/envmath.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/evenpage.html
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/evenpage.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/graphfig.html
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/graphfig.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/index.html
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/makedoc
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/mathcmd.html
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/mathcmd.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/quotes.html
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/quotes.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/sobolev.html
%doc %{_datadir}/texmf-dist/doc/latex/bosisio/sobolev.pdf
%doc %{_datadir}/texmf-dist/source/latex/bosisio/accenti.drv
%doc %{_datadir}/texmf-dist/source/latex/bosisio/accenti.dtx
%doc %{_datadir}/texmf-dist/source/latex/bosisio/dblfont.drv
%doc %{_datadir}/texmf-dist/source/latex/bosisio/dblfont.dtx
%doc %{_datadir}/texmf-dist/source/latex/bosisio/envmath.drv
%doc %{_datadir}/texmf-dist/source/latex/bosisio/envmath.dtx
%doc %{_datadir}/texmf-dist/source/latex/bosisio/evenpage.drv
%doc %{_datadir}/texmf-dist/source/latex/bosisio/evenpage.dtx
%doc %{_datadir}/texmf-dist/source/latex/bosisio/graphfig.drv
%doc %{_datadir}/texmf-dist/source/latex/bosisio/graphfig.dtx
%doc %{_datadir}/texmf-dist/source/latex/bosisio/mathcmd.drv
%doc %{_datadir}/texmf-dist/source/latex/bosisio/mathcmd.dtx
%doc %{_datadir}/texmf-dist/source/latex/bosisio/quotes.drv
%doc %{_datadir}/texmf-dist/source/latex/bosisio/quotes.dtx
%doc %{_datadir}/texmf-dist/source/latex/bosisio/sobolev.drv
%doc %{_datadir}/texmf-dist/source/latex/bosisio/sobolev.dtx
%{_datadir}/texmf-dist/tex/latex/bosisio/accenti.sty
%{_datadir}/texmf-dist/tex/latex/bosisio/dblfont.sty
%{_datadir}/texmf-dist/tex/latex/bosisio/envmath.sty
%{_datadir}/texmf-dist/tex/latex/bosisio/evenpage.sty
%{_datadir}/texmf-dist/tex/latex/bosisio/graphfig.sty
%{_datadir}/texmf-dist/tex/latex/bosisio/mathcmd.sty
%{_datadir}/texmf-dist/tex/latex/bosisio/quotes.sty
%{_datadir}/texmf-dist/tex/latex/bosisio/sobolev.sty
