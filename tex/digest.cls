\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{digest}
\RequirePackage{graphicx}
\RequirePackage{tcolorbox}
\RequirePackage{tabularx,array,booktabs}
\LoadClass[twocolumn]{article}

\newcommand{\insertfig}[1] {
      \IfFileExists{./I-RIM_2019_#1.pdf}{\includegraphics[width=0.5\textwidth]{I-RIM_2019_#1}
}{\begin{tcolorbox}[t, colback = red]
        MISSING ID: #1
    \end{tcolorbox}}
}


\newcommand{\pitch}[9] {
\begin{figure}[htp]
  \centering

  \label{figure}

  \begin{tabular}{m{0.5\textwidth}m{0.5\textwidth}}
    \begin{tcolorbox}[t]
        #1: #2
        \tcblower
        #3 \\
        Chair: #4
    \end{tcolorbox}&
    
    %Ciao&

    \insertfig{#5}\\
    
    \insertfig{#6}&

    \insertfig{#7}\\

    \insertfig{#8}&

    \insertfig{#9}\\
  \end{tabular}

\end{figure}
\clearpage
}

\newcommand{\posterfirst}[8] {
\begin{figure}[htp]
  \centering

  \label{figure}

  \begin{tabular}{m{0.5\textwidth}m{0.5\textwidth}}
    \begin{tcolorbox}[t]
        #1: #2
        \tcblower
        #3
    \end{tcolorbox}&
    
    %Ciao&

    \insertfig{#4}\\
    
    \insertfig{#5}&

    \insertfig{#6}\\

    \insertfig{#7}&

    \insertfig{#8}\\
  \end{tabular}

\end{figure}
\clearpage
}

\newcommand{\postersix}[6] {
\begin{figure}[htp]
  \centering

  \label{figure}
    \begin{tabular}{m{0.5\textwidth}m{0.5\textwidth}}

      \insertfig{#1}&
    

     \insertfig{#2}\\
    
     \insertfig{#3}&

    \insertfig{#4}\\

    \insertfig{#5}&

     \insertfig{#6}\\
  \end{tabular}

\end{figure}
\clearpage
}

\newcommand{\posterfive}[5] {
\begin{figure}[htp]
  \centering

  \label{figure}
\begin{tabular}{m{0.5\textwidth}m{0.5\textwidth}}
  \insertfig{#1}&
    

     \insertfig{#2}\\
    
    \insertfig{#3}&

    \insertfig{#4}\\

     \insertfig{#5}&

   \\
  \end{tabular}

\end{figure}
\clearpage
}

\newcommand{\posterfour}[4] {
\begin{figure}[htp]
  \centering

  \label{figure}
\begin{tabular}{m{0.5\textwidth}m{0.5\textwidth}}
  \insertfig{#1}&
    

    \insertfig{#2}\\
    
     \insertfig{#3}&

    \insertfig{#4}\\
  \end{tabular}

\end{figure}
\clearpage
}

\newcommand{\posterthree}[3] {
\begin{figure}[htp]
  \centering

  \label{figure}
\begin{tabular}{m{0.5\textwidth}m{0.5\textwidth}}
 \insertfig{#1}&
    

    \insertfig{#2}\\
    
    \insertfig{#3}&

    \\
  \end{tabular}

\end{figure}
\clearpage
}

\newcommand{\postertwo}[2] {
\begin{figure}[htp]
  \centering

  \label{figure}
\begin{tabular}{m{0.5\textwidth}m{0.5\textwidth}}
  \insertfig{#1}&
    

     \insertfig{#2}\\
  \end{tabular}

\end{figure}
\clearpage
}

\newcommand{\posterone}[1] {
\begin{figure}[htp]
  \centering

  \label{figure}
\begin{tabular}{m{0.5\textwidth}m{0.5\textwidth}}
  \insertfig{#1}&
    
    \\
  \end{tabular}

\end{figure}
\clearpage
}