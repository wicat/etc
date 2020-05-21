# version 0.1.3
# editor: Ekira Welkea
# date: 2016/09/30
# update: 2018/12/27 - ene@xxiong.me
# update: 2020/05/21 - ene@xxiong.me

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

alias ls='ls --color=auto'
alias ll='ls -lh --color=auto'
alias lla='ls -lah --color=auto'

alias fck='eval $(thefuck $(fc -ln -1)); history -r'

alias setproxyon='export ALL_PROXY=socks5://127.0.0.1:1080'
alias setproxyoff='unset ALL_PROXY'

export GPG_TTY=`tty`

PATH=$PATH:$HOME/bin
GOPATH=$HOME/go
PATH=$PATH:$GOPATH/bin
export PATH

function git_branch {
    ref=$(git symbolic-ref HEAD 2> /dev/null) || return;
    echo "("${ref#refs/heads/}")";
}
function git-branch-prompt {
    local branch=`git symbolic-ref HEAD 2>/dev/null | cut -d"/" -f 3`
    if [ $branch ]; then printf "[%s]" $branch; fi
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
#PS1="\e[1;35m\u\e[m\e[1;37m@\e[m\e[1;36m\H\e[m\e[1;32m[\t]\e[m\e[1;33m<\W>\e[m\e[1;31m\$(git_branch)\e[m\\$ "
PS1="\u@\H[\t]<\W>\$(git_branch)\\$ "

screen -S `date | awk -F' ' '{for(i=1;i<NF;i++) print $i}' | grep : | sed 's/://g'`


#############################################
# Mac OSX Settings
# Set ls color on Mac OSX
export CLICOLOR=1
export LSCOLORS=gxfxcxdxbxegedabagacad
export TERM=xterm-color
