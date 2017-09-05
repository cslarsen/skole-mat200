TARGETS := \
	ov1.pdf \
	ov3.pdf

all: $(TARGETS)

open: all
	open ov3.pdf

%.eps: %.gp data.txt
	gnuplot $<

ov1.pdf: ov1.tex ov1-3iii.tex preamble.tex

ov3.pdf: ov3.tex preamble.tex

%.pdf: %.tex
	pdflatex $<
	pdflatex $<

clean:
	rm -f $(TARGETS) $(TARGETS:.pdf=.aux) $(TARGETS:.pdf=.log) $(TARGETS:.pdf=.out)
