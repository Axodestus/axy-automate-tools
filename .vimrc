set nocompatible              " be iMproved, required
filetype off                  " required

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'

Plugin 'https://github.com/ycm-core/YouCompleteMe.git'
Plugin 'https://github.com/doums/darcula.git'
Plugin 'https://github.com/jiangmiao/auto-pairs.git'
Plugin 'https://github.com/kien/ctrlp.vim'
Plugin 'https://github.com/scrooloose/nerdtree'
Plugin 'tpope/vim-fugitive'
Plugin 'https://github.com/airblade/vim-gitgutter.git'
Plugin 'https://github.com/powerline/powerline.git'
Plugin 'aserebryakov/vim-todo-lists'

call vundle#end()            " required

filetype plugin indent on    " required

syntax on

set number
let g:ycm_global_ycm_extra_conf = '/home/alex/ycm_extra_conf.py'
let g:ycm_confirm_extra_conf = 1
set completeopt-=preview
let g:ycm_global_ycm_extra_conf = "~/.ycm_extra_conf.py"
let g:airline#extensions#tabline#enabled = 1
colorscheme darcula

set tabstop=4
set shiftwidth=4
set smarttab
set expandtab
set smartindent
imap jj <Esc>
map <C-n> :NERDTreeToggle<CR>
let g:VimTodoListsUndoneItem = '- [X]'
let g:VimTodoListsDoneItem = '- [V]'
nmap <Space> $
nmap <backspace> ^



