This list is not just a duplication of commands at <https://golem.ph.utexas.edu/~distler/blog/itex2MMLcommands.html>. It has been expanded to include additional changes introduced by this library.


## Environments

``` latex
\begin{env}...\end{env}
```

where `env` is one of

* `matrix`
* `pmatrix`
* `bmatrix`
* `Bmatrix`
* `vmatrix`
* `Vmatrix`
* `smallmatrix`
* `cases`
* `aligned`
* `gathered`
* `split`
* `array`
* `svg`

### Horizontal lines

You can type `\hline` or `\hlinedash` to insert a horizontal line or dashed horizontal line, respectively. For example:

``` latex
\begin{array}{cccc}
1 & 2 & 3 & 4\\
\hdashline
4 & 5 & 6 & 7\\
\hdash
7 & 8 & 9 & 10
\end{array}
```

### The `array` Environment

As in standard LaTeX, the `array` environment takes one optional
argument, indicating the alignment of the whole array with the respect
to the equation axis, and one mandatory argument, indicating the
alignment of the columns. Thus

``` latex
\begin{array}[t]{clrc}
  1 & 2 & 3 & 4 \\
  5 & 6 & 7 & 8 \\
  9 & 10& 11& 12
\end{array}
```

produces an array with four columns. The first and last column are
centered; the second and third are, respectively, left- and
right-aligned. The top line of the array is aligned with the equation
axis.

As in AMSLaTeX

``` latex
\begin{matrix}
   ...
\end{matrix}
```

is precisely equivalent to

```
\begin{array}{cc...c}
   ...
\end{array}
```

except that you don't have to explicitly state the number of columns.

#### Column separators

While defining columns, you can use `|` to indicate an unbroken vertical line, and `:` to indicate a dashed line. For example:

``` latex
\begin{array}[b]{c:c|c}
Bad & Good & Ugly
\end{array}
```

This creates a dashed column between `Bad & Good` and an unbroken line between `Good & Bad`.

Placing either a `:` or `|` as the first or last character creates a frame around the array. For example:


``` latex
\begin{array}[b]{|c:c|c}
Bad & Good & Ugly
\end{array}
```

This creates an unbroken frame around the array. It's also equivalent to


``` latex
\begin{array}[b]{c:c|c|}
Bad & Good & Ugly
\end{array}
```

### The `svg` Environment

Using the `svg` environment:

``` latex
\begin{svg}
   ...
\end{svg}
```

allows you to embed snippets of SVG in itex equations. To assist in [Instiki](http://golem.ph.utexas.edu/instiki/show/HomePage)'s LaTeX export feature, you can also include a `graphicx` command:

\begin{svg}
   ...
\end{svg}
\includegraphics[width=...]{foo}

where `foo.pdf` is a file containing a PDF version of the graphic. In itex, the `\includegraphics` command is defined as a NOOP, and the SVG is embedded in the MathML output. In Instiki's LaTeX export, the opposite is true: the `svg` environment is a NOOP, and the `\includegraphics` command is included in the output.

## WebTeX-style Arrays and Array Options

The [WebTeX notation for arrays](https://golem.ph.utexas.edu/~distler/WebTeX/docs/wtxsec7.html#ARRAY) is also supported.

The `\array{}` command allows much finer control over the layout of arrays than is available in the standard (AMS)LaTeX-style environments above.

<dl>
 <dt><code>\array</code></dt>
 <dd>
   <dl>
     <dt><code>\arrayopts</code></dt>
     <dd>
              <code>\collayout</code> (=<code>\colalign</code>)
              <code>\rowalign</code>
              <code>\align</code>
              <code>\equalcols</code>
              <code>\equalrows</code>
              <code>\collines</code>
              <code>\rowlines</code>
              <code>\frame</code>
              <code>\padding</code>
      </dd>
      <dt><code>\rowopts</code></dt>
      <dd>
             <code>\colalign</code>
             <code>\rowalign</code>
      </dd>
      <dt><code>\cellopts</code></dt>
      <dd>
             <code>\colalign</code>
             <code>\rowalign</code>
             <code>\rowspan</code>
              <code>\colspan</code>
      </dd>
   </dl>
 </dd>
</dl>

## Greek Letters

* `\alpha`
* `\beta`
* `\gamma`
* `\delta`
* `\epsilon`
* `\backepsilon`
* `\varepsilon`
* `\zeta`
* `\eta`
* `\theta`
* `\vartheta`
* `\iota`
* `\kappa`
* `\varkappa`
* `\lambda`
* `\mu`
* `\nu`
* `\xi`
* `\omicron`
* `\pi`
* `\varpi`
* `\rho`
* `\varrho`
* `\sigma`
* `\varsigma`
* `\tau`
* `\upsilon`
* `\phi`
* `\varphi`
* `\chi`
* `\psi`
* `\omega`
* `\Alpha`
* `\Beta`
* `\Gamma`
* `\Delta`
* `\Zeta`
* `\Eta`
* `\Theta`
* `\Iota`
* `\Kappa`
* `\Lambda`
* `\Mu`
* `\Nu`
* `\Xi`
* `\Pi`
* `\Rho`
* `\Sigma`
* `\Tau`
* `\Upsilon` (`\Upsi`)
* `\Phi`
* `\Psi`
* `\Omega`
* `\digamma`
* `\mho`

## Log-like Symbols

* `\arccos`
* `\arcsin`
* `\arctan`
* `\arg`
* `\cos`
* `\cosh`
* `\cot`
* `\coth`
* `\csc`
* `\deg`
* `\det`
* `\dim`
* `\exp`
* `\gcd`
* `\inf`
* `\hom`
* `\ker`
* `\lg`
* `\lim`
* `\liminf`
* `\limsup`
* `\ln`
* `\log`
* `\max`
* `\min`
* `\mod`
* `\pmod`
* `\Pr`
* `\sec`
* `\sin`
* `\sinh`
* `\sup`
* `\tan`
* `\tanh`

## Arrows

* `\rightarrow` (`\to`)
* `\longrightarrow`
* `\Rightarrow` (`\implies`)
* `\hookrightarrow` (`\embedsin`)
* `\mapsto` (`\\map`)
* `\leftarrow`
* `\longleftarrow`
* `\Leftarrow` (`\\impliedby`)
* `\hookleftarrow`
* `\leftrightarrow`
* `\Leftrightarrow`
* `\Longleftrightarrow` (`\iff`)
* `\nearrow` (`\nearr`)
* `\nwarrow` (`\nwarr`)
* `\searrow` (`\searr`)
* `\swarrow` (`\swarr`)
* `\neArrow` (`\neArr`)
* `\nwArrow` (`\nwArr`)
* `\seArrow` (`\seArr`)
* `\swArrow` (`\swArr`)
* `\darr`
* `\Downarrow`
* `\uparr`
* `\Uparrow`
* `\downuparrow` (`\duparr` and `\updarr`)
* `\leftsquigarrow`
* `\rightsquigarrow`
* `\leftrightsquigarrow`
* `\upuparrows`
* `\rightleftarrows`
* `\rightrightarrows`
* `\dashleftarrow`
* `\dashrightarrow`
* `\curvearrowleft`
* `\curvearrowbotright`
* `\downdownarrows`
* `\leftleftarrows`
* `\leftrightarrows`
* `\righttoleftarrow`
* `\lefttorightarrow`
* `\circlearrowleft`
* `\circlearrowright`
* `\curvearrowright`
* `\leftarrowtail`
* `\rightarrowtail`
* `\leftrightsquigarrow`
* `\Lleftarrow`
* `\Rrightarrow`
* `\looparrowleft`
* `\looparrowright`
* `\Lsh`
* `\Rsh`
* `\twoheadleftarrow`
* `\twoheadrightarrow`
* `\nLeftarrow`
* `\nleftarrow`
* `\nLeftrightarrow`
* `\nleftrightarrow`
* `\nRightarrow`
* `\nrightarrow`
* `\leftharpoonup`
* `\leftharpoondown`
* `\rightharpoonup`
* `\rightharpoondown`
* `\downharpoonleft`
* `\downharpoonright`
* `\leftrightharpoons`
* `\rightleftharpoons`
* `\upharpoonleft`
* `\upharpoonright`

### Extensible Arrows

While you can always put a superscript on an arrow, using `\overset{u}{\rightarrow}` (or both a subscript and a superscript, using `\underoverset{d}{u}{\rightarrow}`), these don't quite work right when exported to LaTeX (the arrows don't stretch). For LaTeX compatibility, one can use * `\xrightarrow{u}` and `\xrightarrow[d]{u}` respectively.

The set of extensible arrows is:

* `\xrightarrow`
* `\xleftarrow`
* `\xleftrightarrow`
* `\xLeftarrow`
* `\xRightarrow`
* `\xLeftrightarrow`
* `\xleftrightharpoons`
* `\xrightleftharpoons`
* `\xhookleftarrow`
* `\xhookrightarrow`
* `\xmapsto`

## Delimiters

* `(`
* `)`
* `[`
* `]`
* `\langle` (`\lang`)
* `\rangle` (`\rang`)
* `\llangle`
* `\rrangle`
* `\lbrace` (`\{`)
* `\rbrace` (`\}`)
* `\lceil`
* `\rceil`
* `\lmoustache`
* `\rmoustache`
* `\lfloor`
* `\rfloor`
* `\uparrow`
* `\downarrow`
* `\updownarrow`
* `\vert` (`\|`)
* `\Vert` (`\|`)
* `/`

In TeX, delimiters are non-stretchy, by default. Stretchy delimiters are obtained with `\left<delim>` and `\right<delim>`. Each `\left<delim>` must be matched with a corresponding `\right<delim>`. If you don't want a visible matching delimiter, you can match with the invisible delimiters
* `\left.` and `\right.` .

Fixed-size large delimiters are generated with the modifiers:

* `\big`
* `\Big`
* `\bigg`
* `\Bigg`
* `\bigl`
* `\Bigl`
* `\biggl`
* `\Biggl`
* `\bigr`
* `\Bigr`
* `\biggr`
* `\Biggr`.

For example
* `\Biggr)` generates a very large (3 * normal size) right parenthesis; `\bigl\vert` generates a large (1.2 * natural size) left vertical bar.

## Operators

* `\amalg`
* `\angle`
* `\measuredangle`
* `\sphericalangle`
* `\approx`
* `\approxeq`
* `\thickapprox`
* `\ast`
* `\asymp`
* `\backslash`
* `\because`
* `\between`
* `\bottom` (`\bot`)
* `\boxminus` (`\minusb`)
* `\boxplus` (`\plusb`)
* `\boxtimes` (`\timesb`)
* `\boxdot`
* `\bowtie`
* `\bullet`
* `\cap` (`\intersection`)
* `\cup` (`\union`)
* `\Cap`
* `\Cup`
* `\cdot`
* `\circledast`
* `\circledcirc`
* `\clubsuit`
* `\curlyvee`
* `\curlywedge`
* `\diamondsuit`
* `\divideontimes`
* `\dotplus`
* `\heartsuit`
* `\spadesuit`
* `\circ`
* `\bigcirc`
* `\cong`
* `\ncong`
* `\dagger`
* `\ddagger`
* `\dashv`
* `\Vdash`
* `\vDash`
* `\nvDash`
* `\VDash`
* `\nVDash`
* `\vdash`
* `\nvdash`
* `\Vvdash`
* `\Diamond`
* `\diamond`
* `\div`
* `\equiv`
* `\nequiv`
* `\eqcirc`
* `\neq` (`\ne`)
* `\Bumpeq`
* `\bumpeq`
* `\circeq`
* `\doteq`
* `\doteqdot`
* `\fallingdotseq`
* `\risingdotseq`
* `\exists`
* `\nexists`
* `\flat`
* `\forall`
* `\frown`
* `\smallfrown`
* `\gt`
* `\ngtr`
* `\gg`
* `\ggg`
* `\geq` (`\ge`)
* `\ngeq`
* `\geqq`
* `\ngeqq`
* `\geqslant`
* `\ngeqslant`
* `\eqslantgtr`
* `\gneq`
* `\gneqq`
* `\gnapprox`
* `\gnsim`
* `\gtrapprox`
* `\gtrsim`
* `\gtrdot`
* `\gtreqless`
* `\gtreqqless`
* `\gtrless`
* `\gvertneqq`
* `\in`
* `\notin`
* `\ni`
* `\notni`
* `\intercal`
* `\invamp` (`\parr`)
* `\lhd`
* `\unlhd`
* `\leftthreetimes`
* `\rightthreetimes`
* `\lt`
* `\nless`
* `\ll`
* `\lll`
* `\leq` (`\le`)
* `\nleq`
* `\leqq`
* `\nleqq`
* `\leqslant`
* `\nleqslant`
* `\eqslantless`
* `\lessapprox`
* `\lessdot`
* `\lesseqgtr`
* `\lesseqqgtr`
* `\lessgtr`
* `\lesssim`
* `\lnapprox`
* `\lneq`
* `\lneqq`
* `\lnsim`
* `\ltimes`
* `\lvertneqq`
* `\lozenge`
* `\blacklozenge`
* `\mid` (`\shortmid`)
* `\nmid`
* `\nshortmid`
* `\models`
* `\multimap`
* `\nabla` (`\Del`)
* `\natural`
* `\not` (`\neg`)
* `\odot`
* `\odash` (`\circleddash`)
* `\otimes`
* `\oplus`
* `\ominus`
* `\oslash`
* `\parallel`
* `\nparallel`
* `\shortparallel`
* `\nshortparallel`
* `\partial`
* `\Perp` (`\Vbar`)
* `\perp`
* `\pitchfork`
* `\pm`
* `\mp`
* `\prec`
* `\nprec`
* `\precapprox`
* `\precnapprox`
* `\preceq`
* `\npreceq`
* `\preccurlyeq`
* `\curlyeqprec`
* `\precsim`
* `\precnsim`
* `\prime`
* `\backprime`
* `\propto`
* `\varpropto`
* `\rhd`
* `\unrhd`
* `\rtimes`
* `\setminus`
* `\smallsetminus`
* `\sharp`
* `\sim`
* `\nsim`
* `\backsim`
* `\simeq`
* `\backsimeq`
* `\thicksim`
* `\smile`
* `\smallsmile`
* `\sslash`
* `\subset`
* `\nsubset`
* `\subseteq`
* `\nsubseteq`
* `\subseteqq`
* `\nsubseteqq`
* `\subsetneq`
* `\subsetneqq`
* `\varsubsetneq`
* `\varsubsetneqq`
* `\Subset`
* `\succ`
* `\nsucc`
* `\succeq`
* `\nsucceq`
* `\succapprox`
* `\succnapprox`
* `\succcurlyeq`
* `\curlyeqsucc`
* `\succsim`
* `\succnsim`
* `\supset`
* `\nsupset`
* `\supseteq`
* `\nsupseteq`
* `\supseteqq`
* `\supsetneq`
* `\supsetneqq`
* `\varsupsetneq`
* `\varsupsetneqq`
* `\Supset`
* `\square` (`\Box`)
* `\blacksquare` (`\qed`)
* `\sqcup`
* `\sqcap`
* `\sqsubset`
* `\sqsubseteq`
* `\sqsupset`
* `\sqsupseteq`
* `\star`
* `\bigstar`
* `\therefore`
* `\times`
* `\top`
* `\triangle`
* `\triangledown`
* `\triangleleft`
* `\triangleright`
* `\blacktriangle`
* `\blacktriangledown`
* `\bigtriangleup`
* `\bigtriangledown`
* `\blacktriangleleft`
* `\blacktriangleright`
* `\ntriangleleft`
* `\ntriangleright`
* `\ntrianglelefteq`
* `\ntrianglerighteq`
* `\trianglelefteq`
* `\trianglerighteq`
* `\triangleq`
* `\vartriangleleft`
* `\vartriangleright`
* `\uplus`
* `\vee`
* `\veebar`
* `\wedge`
* `\barwedge`
* `\doublebarwedge`
* `\wr`
* `\coloneqq`
* `\Coloneqq`
* `\coloneq`
* `\Coloneq`
* `\eqqcolon`
* `\Eqqcolon`
* `\eqcolon`
* `\Eqcolon`
* `\colonapprox`
* `\Colonapprox`
* `\colonsim`
* `\Colonsim`
* `\dblcolon`

In keeping with AMSLaTeX, rather than [MathML's conventions](http://www.w3.org/TR/2003/REC-MathML2-20031021/byalpha.html), `\smallsetminus` (U+FE68) is designated as a small (non-stretchy) reverse solidus, `\backslash` is a reverse solidus (U+05C), and `\setminus` (∖ = U+2216) is stretchy.

## Symbols

* `\aleph`
* `\beth`
* `\ell`
* `\hbar`
* `\Im`
* `\imath`
* `\jmath`
* `\eth`
* `\Re`
* `\wp`
* `\infty` (`\infinity`)
* `\emptyset` (`\varnothing)

## Dots

* `\dots`
* `\ldots`
* `\cdots`
* `\ddots`
* `\udots`
* `\vdots`
* `\colon`

While ":" is allowed in math mode, it doesn't (either in LaTeX or in itex) produce the desired spacing for text like f:A→B. Use `\colon` instead.

## Large Math Operators and Integrals

* `\bigcup` (`\Union`)
* `\bigcap` (`\Intersection`)
* `\bigodot`
* `\bigoplus` (`\Oplus`)
* `\bigotimes` (`\Otimes`)
* `\bigsqcup`
* `\bigsqcap`
* `\biginterleave`
* `\biguplus`
* `\bigwedge` (`\Wedge`)
* `\bigvee` (`\Vee`)
* `\coprod` (`\coproduct`)
* `\prod` (`\product`)
* `\sum`
* `\int` (`\integral`)
* `\iint` (`\doubleintegral`)
* `\iiint` (`\tripleintegral`)
* `\iiiint` (`\quadrupleintegral`)
* `\oint` (`\conint\` and `\contourintegral`)

## Sizes and Styles

* `\displaystyle`
* `\textstyle`
* `\textsize`
* `\scriptsize`
* `\scriptscriptsize`
* `\mathit`
* `\mathbf` (`\boldsymbol`)
* `\mathrm`
* `\mathbb`
* `\mathfrak` (`\mathfr`)
* `\mathcal`
* `\mathsf`
* `\mathtt`
* `\text`

## Spaces

* `\,` (`\thinspace`)
* `\:` (`\medspace`)
* `\;` (`\thickspace`)
* `\quad`
* `\qquad`
* `\!` (`\negthinspace`)
* `\negmedspace`
* `\negthickspace`
* `\phantom`
* `\mathrlap`
* `\mathllap`
* `\mathclap`
* `\space` (Taken from [WebTeX](https://golem.ph.utexas.edu/~distler/WebTeX/docs/wtxsec8.html#ARBSIZE "\space in the WebTeX Manual"))

## Accents

* `\bar`
* `\overline` (`\closure\` and `\widebar`)
* `\underline`
* `\vec`
* `\widevec`
* `\dot`
* `\ddot`
* `\dddot`
* `\ddddot`
* `\tilde`
* `\widetilde`
* `\check`
* `\widecheck`
* `\hat`
* `\widehat`
* `\slash`
* `\boxed`

## Fractions, Sub/Superscripts, and Roots

* `\frac`
* `\tfrac`
* `\binom`
* `\tbinom`
* `\over`
* `\atop`
* `\substack`
* `\overbrace`
* `\underbrace`
* `\underset`
* `\overset` (`\stackrel`)
* `\underoverset` (such as `\underoverset{subscript}{superscript}{symbol}`)
* `\tensor` (taken from [WebTex](https://golem.ph.utexas.edu/~distler/WebTeX/docs/wtxsec5.html#SUPER))
* `\multiscripts` (taken from [WebTex](https://golem.ph.utexas.edu/~distler/WebTeX/docs/wtxsec5.html#PRESCR))
* `\sqrt`
* `\root` (taken from [WebTex](https://golem.ph.utexas.edu/~distler/WebTeX/docs/wtxsec5.html#ROOT))
* `\operatorname`
* `\mathop`
* `\mathbin`
* `\mathrel`
* `\mathraisebox` (`\mathraisebox{voffset}[height][depth]{content}` works just like `\raisebox`)

As in LaTeX, `\sqrt` accepts an optional argument, so that `\sqrt[3]{n+1}` is equivalent to `\root{3}{n+1}`.

## Numbers

In MathML, numbers are represented as `<mn>127.3</mn>`. itex2MML does its best to intelligently parse what's a number and what's not. Unfortunately, conventions for things like [decimal markers](http://en.wikipedia.org/wiki/Decimal_separator) are very culture-dependent, and incompatibly-so. If you don't like the way itex2MML parses the would-be numbers in your input, you can force it to interpret a certain string as a number, using the `\itexnum{}` command.

## Colors

`\color{colourspec}` changes the current foreground colour. `colourspec` is either:

* An HTML named-color:
  * `aqua`
  * `black`
  * `blue`
  * `fuchsia`
  * `gray`
  * `green`
  * `lime`
  * `maroon`
  * `navy`
  * `olive`
  * `purple`
  * `red`
  * `silver`
  * `teal`
  * `white`
  * `yellow`
* An RGB colour value:
  * `#rgb` or `#rrggbb`, a three- or six-digit hexadecimal number.
  `#000000` is black `#FFFFFF` is white, and `#1AC=#11AACC`.

For example:

``` latex
a { b \color{red} c \color{#0F0} d } e
```

renders `a`, `b`, and `e` in the default colour (usually black), `c` in red, and `d` in green.

The alternate LaTeX syntax, involving specifying a color model is not supported:

``` latex
\color[cmyk]{0, 0.1, 0.5, 0.3}
```

A new command, `\bgcolor{colourspec}` works the same way, but changes the current background colour.

## Interactivity


<dl>
    <dt><code>\href{<i>url</i>}{<i>expression</i>}</code></dt>
    <dd>Turns a mathematical <i>expression</i> into a clickable link. This makes use of <a href="http://www.w3.org/TR/xlink/">Xlink</a>.</dd>

    <dt><code>\statusline{<i>message</i>}{<i>expression</i>}</code></dt>
    <dd>Displays the <i>message</i> text in the browser's status-line, when the user hovers his mouse over the mathematical <i>expression</i>.</dd>

    <dt><code>\tooltip{<i>message</i>}{<i>expression</i>}</code></dt>
    <dd>Displays the <i>message</i> text as a tooltip, when the user hovers his mouse over the mathematical <i>expression</i>.</dd>

    <dt><code>\fghilight{<i>colourspec</i>}{<i>expression</i>}</code> (<code>\fghighlight</code>)</dt>
    <dd>Change the foreground color of an expression when the user hovers over it.</dd>

    <dt><code>\bghilight{<i>colourspec</i>}{<i>expression</i>}</code> (<code>\bghighlight</code>)</dt>
    <dd>Change the background color of an expression when the user hovers over it.</dd>

    <dt><code>\toggle{<i>expression1</i>}{<i>expression2</i>}</code></dt>
    <dd>Toggle between these two expressions when the user clicks on them.</dd>

    <dt><code>\begintoggle{<i>expression1</i>}{<i>expression2</i>}...{<i>expressionN</i>}\endtoggle</code></dt>
    <dd>Toggle between these <i>n</i> expressions when the user clicks on them.</dd>
</dl>