# version 0.1.2
# editor: Ekira Welkea
# date: 2016/09/30
# update: 2018/12/27 - ene@xxiong.me

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias ll='ls -lh --color=auto'
alias lla='ls -lah --color=auto'
alias llh='ls -lah --color=auto'
export GPG_TTY=`tty`

PATH=$PATH:$HOME/bin
GOPATH=$HOME/go
PATH=$PATH:$GOPATH/bin
export PATH

function git_branch {
    ref=$(git symbolic-ref HEAD 2> /dev/null) || return;
    echo "("${ref#refs/heads/}") ";
}

#function git_branch {
#    branch="`git branch 2>/dev/null | grep "^\*" | sed -e "s/^\*\ //"`"
#    if [ "${branch}" != "" ];then
#        if [ "${branch}" = "(no branch)" ];then
#            branch="(`git rev-parse --short HEAD`...)"
#        fi
#        echo "($branch)"
#    fi
#}

#PS1='\e[1;35mroot\e[m\e[1;34m@Linux\e[m\e[0;35m_\e[m\e[1;32m<\w>\e[m'
#PS1='\e[1;35mxxiong\e[m\e[1;34m@CQU611\e[m\e[0;35m_\e[m\e[1;32m<\w>\e[m\e[0;31m$(git_branch)\e[m'
PS1="\e[1;35m\u\e[m\e[1;37m@\e[m\e[1;36m\H\e[m\e[1;32m[\t]\e[m\e[1;33m<\W>\e[m\e[1;36m\$(git_branch)\e[m\\$ "



